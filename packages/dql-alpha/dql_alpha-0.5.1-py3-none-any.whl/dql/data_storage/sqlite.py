import hashlib
import logging
import posixpath
import sqlite3
from datetime import datetime, timezone
from functools import wraps
from time import sleep
from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple

from dql import utils
from dql.data_storage.abstract import AbstractDataStorage
from dql.error import DQLError
from dql.jmes_sql.transpiler import Transpiler
from dql.node import DirType, Node, NodeWithPath
from dql.storage import Status as StorageStatus
from dql.storage import Storage
from dql.utils import GLOB_CHARS, DQLDir, sql_file_filter

logger = logging.getLogger("dql")

NODE_FIELDS = [
    "dir_type",
    "parent_id",
    "name",
    "checksum",
    "etag",
    "version",
    "is_latest",
    "last_modified",
    "size",
    "owner_name",
    "owner_id",
    "path_str",
    "anno",
]
NODE_FIELDS_NO_ID = ", ".join(NODE_FIELDS)
NODE_FIELDS_ALL = f"id, {NODE_FIELDS_NO_ID}"
NODE_QMARKS_NO_ID = ", ".join("?" for _ in NODE_FIELDS)
PATH_STR_INDEX = NODE_FIELDS.index("path_str") + 1
RETRY_START_SEC = 0.01
RETRY_MAX_TIMES = 10
RETRY_FACTOR = 2


def get_retry_sleep_sec(retry_count: int) -> int:
    return RETRY_START_SEC * (RETRY_FACTOR**retry_count)


def retry_sqlite_locks(func):
    # This retries the database modification in case of concurrent access
    @wraps(func)
    def wrapper(*args, **kwargs):
        exc = None
        for retry_count in range(RETRY_MAX_TIMES):
            try:
                return func(*args, **kwargs)
            except sqlite3.OperationalError as operror:
                exc = operror
                sleep(get_retry_sleep_sec(retry_count))
        raise exc

    return wrapper


def retry_sqlite_locks_async(func):
    # This retries the database modification in case of concurrent access
    # (For async code)
    @wraps(func)
    async def wrapper(*args, **kwargs):
        exc = None
        for retry_count in range(RETRY_MAX_TIMES):
            try:
                return await func(*args, **kwargs)
            except sqlite3.OperationalError as operror:
                exc = operror
                sleep(get_retry_sleep_sec(retry_count))
        raise exc

    return wrapper


class SQLiteDataStorage(AbstractDataStorage):
    """
    SQLite data storage uses SQLite3 for storing indexed data locally.
    This is currently used for the cli although could potentially support or
    be expanded for cloud storage as well.
    """

    TABLE_NAME_PREFIX = "dsrc_"
    TABLE_NAME_SHA_LIMIT = 12

    def __init__(self, db_file: Optional[str] = None, table_name: str = ""):
        self.table_name = table_name
        self.db_file = db_file if db_file else DQLDir.find().db

        try:
            if self.db_file == ":memory:":
                # Enable multithreaded usage of the same in-memory db
                self.db = sqlite3.connect(
                    "file::memory:?cache=shared", uri=True
                )
            else:
                self.db = sqlite3.connect(self.db_file)
            self.db.execute("PRAGMA foreign_keys = ON")
            self.db.execute("PRAGMA cache_size = -102400")  # 100 MiB
            # Enable Write-Ahead Log Journaling
            self.db.execute("PRAGMA journal_mode = WAL")
            self.db.execute("PRAGMA synchronous = NORMAL")
            self.db.execute("PRAGMA case_sensitive_like = ON")

            self._init_storage_table()
        except RuntimeError:
            raise DQLError("Can't connect to SQLite DB")

    def _init_storage_table(self):
        """Initialize only tables related to storage, e.g s3"""
        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS buckets
            (
                uri         TEXT PRIMARY KEY NOT NULL,
                timestamp   DATETIME,
                expires     DATETIME,
                status      INTEGER NOT NULL
            )
        """
        )

    def init_db(self):
        # Note that an index on the primary key (id) is automatically created
        self.db.executescript(
            f"""
            DROP TABLE IF EXISTS {self.table_name};

            CREATE TABLE {self.table_name}
            (
                id              INTEGER PRIMARY KEY,
                dir_type        INTEGER,
                parent_id       INTEGER,
                name            TEXT NOT NULL,
                checksum        TEXT,
                etag            TEXT,
                version         TEXT,
                is_latest       BOOL,
                last_modified   DATETIME,
                size            BIGINT NOT NULL,
                owner_name      TEXT,
                owner_id        TEXT,
                path_str        TEXT,
                anno            JSON
            );

            CREATE INDEX IF NOT EXISTS idx_dir_type_{self.table_name}
            ON {self.table_name} (dir_type);
            CREATE INDEX IF NOT EXISTS idx_parent_id_{self.table_name}
            ON {self.table_name} (parent_id);
            CREATE INDEX IF NOT EXISTS idx_name_{self.table_name}
            ON {self.table_name} (name);
            CREATE INDEX IF NOT EXISTS idx_path_str_{self.table_name}
            ON {self.table_name} (path_str);
        """
        )

    @classmethod
    def _table_name(cls, uri):
        sha = hashlib.sha256(uri.encode("utf-8")).hexdigest()
        return cls.TABLE_NAME_PREFIX + sha[: cls.TABLE_NAME_SHA_LIMIT]

    def clone(self, uri: Optional[str] = None) -> "SQLiteDataStorage":
        table_name = self._table_name(uri) if uri else self.table_name
        return SQLiteDataStorage(db_file=self.db_file, table_name=table_name)

    @staticmethod
    def _generate_sorting_sql(
        sort_by_parent_id: bool, sort_by_size: bool, sort_by_path: bool
    ) -> str:
        """Creates sorting sql command by parent_id, path, or size"""
        conditions = []
        if sort_by_parent_id:
            conditions.append("parent_id")

        if sort_by_size and sort_by_path:
            raise RuntimeError("Can't sort by size and path at the same time")
        if sort_by_size:
            conditions.append("size DESC")
        elif sort_by_path:
            conditions.append("path_str")

        sorting_sql = ""
        if conditions:
            sorting_sql = f"ORDER BY {', '.join(conditions)}"

        return sorting_sql

    @staticmethod
    def _generate_type_filter(
        type_filter: Optional[str] = None, add_and: bool = False
    ) -> str:
        """Creates type filter SQL for files or directories"""
        filter_sql = ""
        if type_filter in ["f", "file", "files"]:
            filter_sql = f"dir_type = {DirType.FILE}"
        elif type_filter in ["d", "dir", "directory", "directories"]:
            filter_sql = f"dir_type > {DirType.FILE}"

        if add_and and filter_sql:
            filter_sql = f" AND {filter_sql}"

        return filter_sql

    def _get_nodes_by_glob_path_pattern(
        self, path_list: List[str], glob_name: str
    ) -> Iterable[NodeWithPath]:
        """Finds all Nodes that correspond to GLOB like path pattern."""
        node = self._get_node_by_path_list(path_list)
        if not node.is_dir:
            raise RuntimeError(f"Can't resolve name {'/'.join(path_list)}")
        result = self.db.execute(
            f"""
            SELECT {NODE_FIELDS_ALL} FROM '{self.table_name}'
            WHERE parent_id = ? AND is_latest
                AND name GLOB ?
            """,
            [node.id, glob_name],
        )
        return (
            NodeWithPath(*row, path_list)  # type: ignore [call-arg]
            for row in result
        )

    def _get_node_by_path_list(self, path_list: List[str]) -> NodeWithPath:
        """
        Gets node that correspond some path list,
        e.g ["data-lakes", "dogs-and-cats"]
        """
        path_str = "/".join(path_list)
        res = self.db.execute(
            f"""
            SELECT {NODE_FIELDS_ALL} FROM {self.table_name}
            WHERE path_str = ? AND name = ? AND is_latest
            """,
            [path_str, path_list[-1] if len(path_list) > 0 else ""],
        ).fetchall()
        if not res:
            raise FileNotFoundError(f"Unable to resolve path {path_str}")
        assert (
            len(res) == 1
        ), f"Too many matches for path {path_str} : Results: {res}"

        return NodeWithPath(*res[0], path_list)  # type: ignore [call-arg]

    def _populate_nodes_by_path(
        self, path_list: List[str], num: int, res: List[NodeWithPath]
    ) -> None:
        """
        Puts all nodes found by path_list into the res input variable.
        Note that path can have GLOB like pattern matching which means that
        res can have multiple nodes as result.
        If there is no GLOB pattern, res should have one node as result that
        match exact path by path_list
        """
        if num >= len(path_list):
            res.append(self._get_node_by_path_list(path_list))
            return

        curr_name = path_list[num]
        if set(curr_name).intersection(GLOB_CHARS):
            nodes = self._get_nodes_by_glob_path_pattern(
                path_list[:num], curr_name
            )
            for node in nodes:
                if not node.is_dir:
                    res.append(node)
                else:
                    path = (
                        path_list[:num]
                        + [node.name or ""]
                        + path_list[num + 1 :]  # type: ignore [attr-defined]
                    )
                    self._populate_nodes_by_path(path, num + 1, res)
        else:
            self._populate_nodes_by_path(path_list, num + 1, res)
            return
        return

    def _get_jmespath_sql(self, jmespath: str) -> Optional[str]:
        # TODO: This will need to be updated for annotation support
        """Returns sql representation of jmespath query"""
        if not jmespath:
            return None
        if len(jmespath) > 1:
            raise ValueError("multiple jmespath filters are not supported")
        try:
            jmespath_sql = Transpiler.build_sql(
                jmespath[0], "WalkTree", "anno", NodeWithPath._fields
            )
        except Exception as ex:
            raise ValueError("jmespath parsing error - " + str(ex))
        return jmespath_sql

    @staticmethod
    def _dict_to_values(d: Dict[str, Any]) -> List[Any]:
        if d.get("dir_type") is None:
            if d.get("is_root"):
                dir_type = DirType.ROOT
            elif d.get("is_dir"):
                dir_type = DirType.DIR
            else:
                dir_type = DirType.FILE
            d["dir_type"] = dir_type

        if not d.get("path_str"):
            if d.get("path"):
                path = d["path"]
                if isinstance(path, list):
                    d["path_str"] = "/".join(path)
                else:
                    d["path_str"] = path
            elif d.get("dir_type") == DirType.ROOT:
                d["path_str"] = ""
            else:
                raise RuntimeError(f"No Path for node data: {d}")

        return [
            d.get("dir_type"),
            d.get("parent_id"),
            d.get("name") or "",
            d.get("checksum"),
            d.get("etag"),
            d.get("version"),
            d.get("is_latest", True),
            d.get("last_modified"),
            d.get("size", 0),
            d.get("owner_name"),
            d.get("owner_id"),
            d.get("path_str"),
            d.get("anno"),
        ]

    @retry_sqlite_locks_async
    async def insert_entry(self, entry: Dict[str, Any]) -> int:
        new_id = self.db.execute(
            f"""
                INSERT INTO {self.table_name} ({NODE_FIELDS_NO_ID})
                VALUES({NODE_QMARKS_NO_ID})
            """,
            SQLiteDataStorage._dict_to_values(entry),
        ).lastrowid
        self.db.commit()
        return new_id or 0

    @retry_sqlite_locks_async
    async def insert_entries(self, entries: List[Dict[str, Any]]) -> None:
        self.db.executemany(
            f"""
                INSERT INTO {self.table_name} ({NODE_FIELDS_NO_ID})
                VALUES({NODE_QMARKS_NO_ID})
            """,
            [SQLiteDataStorage._dict_to_values(e) for e in entries],
        )
        self.db.commit()

    async def insert_root(self) -> int:
        return await self.insert_entry({"dir_type": DirType.ROOT})

    def get_node_by_id(self, node_id: int) -> Optional[NodeWithPath]:
        """Gets node from database by id"""
        res = self.db.execute(
            f"""
            SELECT {NODE_FIELDS_ALL} FROM {self.table_name}
            WHERE id = ?
            """,
            [node_id],
        ).fetchall()
        if res and res[0]:
            return NodeWithPath(
                *res[0], res[PATH_STR_INDEX].split("/")
            )  # type: ignore [call-arg]

        return None

    def get_nodes_by_id(
        self, node_ids: Iterable[int]
    ) -> Iterable[NodeWithPath]:
        """Gets nodes from database by id"""
        rows = self.db.execute(
            f"""
            SELECT {NODE_FIELDS_ALL} FROM {self.table_name}
            WHERE id IN ?
            """,
            [node_ids],
        )
        return (
            NodeWithPath(
                *row, row[PATH_STR_INDEX].split("/")
            )  # type: ignore [call-arg]
            for row in rows
        )

    def get_node_by_name_and_parent(
        self, name: str, parent_id: int
    ) -> Optional[NodeWithPath]:
        """Gets node from database by name and parent_id"""
        res = self.db.execute(
            f"""
            SELECT {NODE_FIELDS_ALL} FROM {self.table_name}
            WHERE name = ? AND parent_id = ?
            """,
            [name, parent_id],
        ).fetchall()
        if res and res[0]:
            return NodeWithPath(
                *res[0], res[PATH_STR_INDEX].split("/")
            )  # type: ignore [call-arg]

        return None

    def get_nodes_by_parent_id(
        self,
        parent_id: int,
        type_filter: Optional[str] = None,
    ) -> Iterable[NodeWithPath]:
        """Gets nodes from database by parent_id, with optional filtering"""
        filter_sql = SQLiteDataStorage._generate_type_filter(type_filter, True)
        rows = self.db.execute(
            f"""
            SELECT {NODE_FIELDS_ALL} FROM {self.table_name}
            WHERE parent_id = ? {filter_sql}
            """,
            [parent_id],
        )
        return (
            NodeWithPath(
                *row, row[PATH_STR_INDEX].split("/")
            )  # type: ignore [call-arg]
            for row in rows
        )

    def get_storage_all(self) -> Iterator[Storage]:
        for values in self.db.execute(
            "SELECT uri, timestamp, expires, status FROM buckets"
        ):
            yield Storage(*values)

    def get_storage(self, uri: str) -> Optional[Storage]:
        res = self.db.execute(
            """
            SELECT uri, timestamp, expires, status
            FROM buckets
            WHERE uri = ?
            """,
            [uri],
        ).fetchall()
        if not res:
            return None

        assert len(res) == 1, f"Storage duplication: {uri}"

        return Storage(*res[0])

    @retry_sqlite_locks
    def create_storage_if_not_registered(
        self, uri: str, commit: bool = True
    ) -> None:
        self.db.execute(
            """
            INSERT INTO buckets(uri, status) VALUES (?, ?)
            ON CONFLICT(uri) DO NOTHING
            """,
            [uri, StorageStatus.CREATED],
        )
        if commit:
            self.db.commit()

    def register_storage_for_indexing(
        self, uri: str, force_update: bool = True
    ) -> Tuple[Storage, bool, bool]:
        """
        Prepares storage for indexing operation.
        This method should be called before index operation is started
        It returns:
            - storage, prepared for indexing
            - boolean saying if indexing is needed
            - boolean saying if indexing is currently pending (running)
        """
        # This ensures that all calls to the DB are in a single transaction
        # and commit is automatically called once this function returns
        with self.db:
            # Create storage if it doesn't exist
            self.create_storage_if_not_registered(uri, commit=False)
            saved_storage = self.get_storage(uri)

            assert (
                saved_storage is not None
            ), f"Unexpected error, storage for {uri} doesn't exist"
            storage: Storage = saved_storage

            if storage.status == StorageStatus.PENDING:
                return storage, False, True

            elif storage.is_expired:
                storage = self.mark_storage_pending(storage, commit=False)
                return storage, True, False

            elif storage.status == StorageStatus.COMPLETE and not force_update:
                return storage, False, False

            else:
                storage = self.mark_storage_pending(storage, commit=False)
                return storage, True, False

    @retry_sqlite_locks
    def mark_storage_pending(
        self, storage: Storage, commit: bool = True
    ) -> Storage:
        # Update status to pending and dates
        storage = storage._replace(
            status=StorageStatus.PENDING, timestamp=None, expires=None
        )

        self.db.execute(
            """
            UPDATE buckets
            SET timestamp = ?, expires = ?, status = ?
            WHERE uri = ?
            """,
            [
                storage.timestamp,
                storage.expires,
                storage.status,
                storage.uri,
            ],
        )
        if commit:
            self.db.commit()

        return storage

    @retry_sqlite_locks
    def mark_storage_indexed(
        self,
        uri: str,
        status: int,
        ttl: int,
        end_time: Optional[datetime] = None,
    ) -> None:
        if end_time is None:
            end_time = datetime.now(timezone.utc)
        self.db.execute(
            """
            UPDATE buckets
            SET timestamp = ?, expires = ?, status = ?
            WHERE uri = ?
            """,
            [
                end_time,
                Storage.get_expiration_time(end_time, ttl),
                status,
                uri,
            ],
        )
        self.db.commit()

    def get_node_by_path(self, path: str) -> NodeWithPath:
        path = path.lstrip("/")

        is_dir_required = False
        if path and path[-1] == "/":
            path = path.rstrip("/")
            is_dir_required = True

        path_list = path.split("/") if path != "" else []
        node = self._get_node_by_path_list(path_list)

        if is_dir_required and not node.is_dir:
            raise FileNotFoundError(f"Directory {path} is not found")

        return node

    def get_nodes_by_path(self, path: str) -> Iterable[NodeWithPath]:
        clean_path = path.strip("/")
        path_list = clean_path.split("/") if clean_path != "" else []

        res: List[NodeWithPath] = []
        self._populate_nodes_by_path(path_list, 0, res)
        return res

    def get_latest_files_by_parent_node(
        self, parent_node: Node
    ) -> Iterable[Node]:
        if not parent_node.is_dir:
            return [parent_node]

        result = self.db.execute(
            f"""
            SELECT {NODE_FIELDS_ALL} FROM '{self.table_name}'
            WHERE parent_id = ? AND is_latest
            """,
            [parent_node.id],
        ).fetchall()
        return map(Node._make, result)

    def size(self, node: NodeWithPath) -> Tuple[int, int]:
        if not node.is_dir:
            # Return node size if this is not a directory
            return node.size, 1

        parent_path_str = node.path_str

        results = self.db.execute(
            f"""
                SELECT SUM(size), SUM(dir_type = 0) FROM {self.table_name}
                WHERE path_str LIKE ? AND is_latest
            """,
            [posixpath.join(parent_path_str, "%")],
        ).fetchall()

        if not results:
            raise FileNotFoundError(
                f"Unable to resolve path {parent_path_str}"
            )
        if len(results) != 1 or len(results[0]) != 2:
            raise RuntimeError(
                f"Unexpected SQL size calculation result: {results}"
            )
        return results[0][0] or 0, results[0][1] or 0

    def walk_subtree(
        self,
        node: NodeWithPath,
        sort_by_parent_id: bool = False,
        sort_by_size: bool = False,
        sort_by_path: bool = False,
        type_filter: Optional[str] = None,
        custom_filter: Optional[str] = None,
    ) -> Iterable[NodeWithPath]:
        parent_path_str = node.path_str
        parent_path_len = len(parent_path_str)

        sorting_sql = SQLiteDataStorage._generate_sorting_sql(
            sort_by_parent_id, sort_by_size, sort_by_path
        )
        filter_sql = SQLiteDataStorage._generate_type_filter(type_filter, True)
        if custom_filter:
            filter_sql = f"AND {custom_filter} {filter_sql}"

        results = self.db.execute(
            f"""
                SELECT {NODE_FIELDS_ALL} FROM {self.table_name}
                WHERE path_str LIKE ? AND dir_type != {DirType.ROOT}
                AND is_latest
                {filter_sql} {sorting_sql}
            """,
            [posixpath.join(parent_path_str, "%")],
        ).fetchall()

        if not results:
            raise FileNotFoundError(
                f"Unable to resolve path {parent_path_str}"
            )
        return (
            NodeWithPath(
                *row,
                path=row[PATH_STR_INDEX][parent_path_len:]
                .lstrip("/")
                .split("/"),
            )  # type: ignore [call-arg]
            for row in results
        )

    def find(
        self,
        node: NodeWithPath,
        names=None,
        inames=None,
        paths=None,
        ipaths=None,
        size=None,
        type=None,  # pylint: disable=redefined-builtin
        jmespath="",
    ) -> Iterable[NodeWithPath]:
        if jmespath:
            raise NotImplementedError("jmespath queries not supported!")
        custom_filter = utils.sql_file_filter(
            names, inames, paths, ipaths, size, type
        )
        try:
            return self.walk_subtree(node, custom_filter=custom_filter)
        except FileNotFoundError:
            return []

    @retry_sqlite_locks
    def update_annotation(self, node: Node, annotation_content: str) -> None:
        # TODO: This will likely need to be updated for annotation support
        img_exts = ["jpg", "jpeg", "png"]
        names = (node.name_no_ext + "." + ext for ext in img_exts)
        filter_sql = sql_file_filter(inames=names, op="=")

        res = self.db.execute(
            f"""
            UPDATE '{self.table_name}'
            SET anno = ?
            WHERE parent_id = ?
                AND dir_type = {DirType.FILE}
                AND is_latest
                AND {filter_sql}
            """,
            [annotation_content, node.parent_id],
        ).fetchall()
        self.db.commit()

        if res is None or len(res) == 0:
            msg = f"no image file was found for annotation {node.name}"
            logger.warning(msg)
        elif res[0][0] > 1:
            msg = (
                f"multiple image files were updated for a single "
                f"annotation {node.name}"
            )
            logger.warning(msg)

    @retry_sqlite_locks
    def update_checksum(self, node: Node, checksum: str) -> None:
        self.db.execute(
            f"""
            UPDATE '{self.table_name}'
            SET checksum = ?
            WHERE id = ?
            """,
            [checksum, node.id],
        )
        self.db.commit()
