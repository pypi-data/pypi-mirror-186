import logging
import os
import os.path
import posixpath
import shutil
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple

import yaml

from dql.client import Client
from dql.data_storage import AbstractDataStorage
from dql.listing import Listing
from dql.node import NodeWithPath
from dql.storage import Status, Storage
from dql.utils import DQLDir, dql_paths_join

logger = logging.getLogger("dql")

DEFAULT_DATASET_DIR = "dataset"
DATASET_FILE_SUFFIX = ".dql"

TTL_INT = 4 * 60 * 60


class PendingIndexingError(Exception):
    pass


class DataSource:
    def __init__(self, listing, node):
        self.listing = listing
        self.node = node

    def get_full_path(self):
        return posixpath.join(self.listing.storage.uri, self.node.full_path)

    def get_node_full_path(self, node):
        return posixpath.join(self.listing.storage.uri, node.full_path)


@dataclass
class NodeGroup:
    """Class for a group of nodes from the same source"""

    listing: Listing
    nodes: Iterable[NodeWithPath]

    # The source path within the bucket
    # (not including the bucket name or s3:// prefix)
    source_path: str = ""


def check_output_dataset_file(
    output: str,
    force: bool = False,
    dataset_filename: Optional[str] = None,
    skip_check_output: bool = False,
    skip_check_dql: bool = False,
) -> str:
    """
    Checks the output directory and dataset filename for existence or if they
    should be force-overwritten.
    """
    if not skip_check_output:
        if os.path.exists(output):
            if force:
                shutil.rmtree(output)
            else:
                raise RuntimeError(
                    f"Output directory already exists: {output}"
                )

    dataset_file = (
        dataset_filename if dataset_filename else output + DATASET_FILE_SUFFIX
    )
    if not skip_check_dql:
        if os.path.exists(dataset_file):
            if force:
                os.remove(dataset_file)
            else:
                raise RuntimeError(
                    f"Output dataset file already exists: {dataset_file}"
                )
    return dataset_file


def parse_dql_file(filename: str) -> List[Dict[str, Any]]:
    with open(filename, encoding="utf-8") as f:
        contents = yaml.safe_load(f)

    if not isinstance(contents, list):
        contents = [contents]

    for entry in contents:
        if not isinstance(entry, dict):
            raise ValueError(
                "Failed parsing DQL file, "
                "each data source entry must be a dictionary"
            )
        if "data-source" not in entry or "files" not in entry:
            raise ValueError(
                "Failed parsing DQL file, "
                "each data source entry must contain the "
                '"data-source" and "files" keys'
            )

    return contents


def trim_node_path(node: NodeWithPath) -> NodeWithPath:
    return node._replace(
        path=node.path[:-1]  # type: ignore[call-arg,attr-defined]
    )


def find_column_to_str(
    node: NodeWithPath, src: DataSource, column: str
) -> str:
    if column == "du":
        return str(src.listing.du(node)[0])
    if column == "name":
        return node.name or ""
    if column == "owner":
        return node.owner_name or ""
    if column == "path":
        return posixpath.join(src.get_full_path(), node.full_path)
    if column == "size":
        return str(node.size)
    if column == "type":
        return "d" if node.is_dir else "f"
    return ""


class Catalog:
    def __init__(
        self,
        data_storage,
        cache_dir=None,
        tmp_dir=None,
    ):
        from dvc_data.hashfile.db.local import LocalHashFileDB
        from dvc_objects.fs.local import LocalFileSystem

        dql_dir = DQLDir(cache=cache_dir, tmp=tmp_dir)
        self.data_storage = data_storage
        self.cache = LocalHashFileDB(
            LocalFileSystem(),
            dql_dir.cache,
            tmp_dir=dql_dir.tmp,
        )

    @staticmethod
    def enlist_source(
        data_storage: AbstractDataStorage,
        source: str,
        ttl: int,
        force_update=False,
        skip_indexing=False,
        to_fetch=True,
        client_config=None,
    ) -> Tuple[Listing, str]:

        if force_update and skip_indexing:
            raise ValueError(
                "Both force_update and skip_indexing flags"
                " cannot be True at the same time"
            )

        client_config = client_config or {}
        client, path = Client.parse_url(source, **client_config)
        source_data_storage = data_storage.clone(uri=client.uri)

        if skip_indexing:
            source_data_storage.create_storage_if_not_registered(client.uri)
            storage = source_data_storage.get_storage(client.uri)
            assert storage
            return (
                Listing(storage, source_data_storage, client),
                path,
            )

        (
            storage,
            need_index,
            in_progress,
        ) = source_data_storage.register_storage_for_indexing(
            client.uri, force_update
        )
        if in_progress:
            raise PendingIndexingError(
                f"Pending indexing operation: uri={storage.uri}"
            )

        lst = Listing(storage, source_data_storage, client)

        if not need_index:
            logger.debug(  # type: ignore[unreachable]
                f"Using cached listing {storage.uri}."
                + f" Valid till: {storage.expires_to_local}"
            )
            # Listing has to have correct version of data storage
            # initialized with correct Storage
            return lst, path

        if to_fetch:
            try:
                source_data_storage.init_db()
                lst.fetch()
                source_data_storage.mark_storage_indexed(
                    storage.uri, Status.COMPLETE, ttl
                )
            except:  # noqa: E722,B001
                source_data_storage.mark_storage_indexed(
                    storage.uri, Status.FAILED, ttl
                )
                raise
            lst.storage = storage
        else:
            source_data_storage.init_db()
        return lst, path

    @staticmethod
    def enlist_sources(
        data_storage: AbstractDataStorage,
        sources: List[str],
        ttl: int,
        update: bool,
        skip_indexing=False,
        client_config=None,
    ) -> List["DataSource"]:
        dsrc_all = []
        for src in sources:  # Opt: parallel
            listing, file_path = Catalog.enlist_source(
                data_storage,
                src,
                ttl,
                update,
                skip_indexing=skip_indexing,
                client_config=client_config,
            )

            nodes = listing.expand_path(file_path)
            for node in nodes:
                dsrc_all.append(DataSource(listing, node))

        return dsrc_all

    @staticmethod
    def enlist_sources_grouped(
        data_storage: AbstractDataStorage,
        sources: List[str],
        ttl: int,
        update: bool,
        no_glob: bool = False,
        client_config=None,
    ) -> Iterable[NodeGroup]:
        node_groups = []
        nodes: Iterable[NodeWithPath] = []
        for src in sources:  # Opt: parallel
            if src.endswith(DATASET_FILE_SUFFIX) and os.path.isfile(src):
                # TODO: Also allow using DQL files from cloud locations?
                dql_data = parse_dql_file(src)
                for ds in dql_data:
                    listing, source_path = Catalog.enlist_source(
                        data_storage,
                        ds["data-source"]["uri"],
                        ttl,
                        update,
                        client_config=client_config,
                    )

                    paths = dql_paths_join(
                        source_path, (f["name"] for f in ds["files"])
                    )

                    nodes = [
                        trim_node_path(listing.resolve_path(p)) for p in paths
                    ]

                    node_groups.append(NodeGroup(listing, nodes, source_path))

                # Done parsing these sources from the DQL file
                continue

            listing, source_path = Catalog.enlist_source(
                data_storage,
                src,
                ttl,
                update,
                client_config=client_config,
            )

            nodes = (
                trim_node_path(listing.resolve_path(source_path))
                if no_glob
                else listing.expand_path(source_path)
            )

            node_groups.append(NodeGroup(listing, nodes, source_path))

        return node_groups

    def ls(
        self,
        sources: List[str],
        ttl=TTL_INT,
        update=False,
        skip_indexing=False,
        *,
        client_config=None,
    ) -> Iterator[Tuple[DataSource, Iterator[NodeWithPath]]]:
        data_sources = Catalog.enlist_sources(
            self.data_storage,
            sources,
            ttl,
            update,
            skip_indexing=skip_indexing,
            client_config=client_config,
        )

        for source in data_sources:
            yield source, iter(source.listing.ls_path(source.node))

    def ls_storages(self) -> Iterator[Storage]:
        yield from self.data_storage.get_storage_all()

    def get(
        self,
        source,
        output,
        force=False,
        update=False,
        ttl=TTL_INT,
        *,
        client_config=None,
    ) -> None:
        listing, file_path = Catalog.enlist_source(
            self.data_storage, source, ttl, update, client_config=client_config
        )

        if not output:
            if file_path:
                output = os.path.basename(file_path.rstrip("/"))
            else:
                output = listing.storage.name

        dataset_file = check_output_dataset_file(output, force)

        node = listing.resolve_path(file_path)
        total_size, total_files = listing.du(node)
        listing.download_subtree(node, self.cache, total_size)
        listing.instantiate_subtree(node, output, self.cache, total_files)
        listing.metafile_for_subtree(file_path, node, dataset_file)

    def cp(
        self,
        sources: List[str],
        output: str,
        force: bool = False,
        update: bool = False,
        recursive: bool = False,
        dql_file: Optional[str] = None,
        dql_only: bool = False,
        no_glob: bool = False,
        no_dql_file: bool = False,
        ttl: int = TTL_INT,
        *,
        client_config=None,
    ) -> List[Dict[str, Any]]:
        node_groups = Catalog.enlist_sources_grouped(
            self.data_storage,
            sources,
            ttl,
            update,
            no_glob,
            client_config=client_config,
        )

        dataset_file = check_output_dataset_file(
            output, force, dql_file, dql_only, no_dql_file
        )

        metafile_data = []

        for node_group in node_groups:
            listing: Listing = node_group.listing
            source_path: str = node_group.source_path
            metafile_group = {
                "data-source": listing.storage.to_dict(source_path),
                "files": [],
            }
            valid_nodes: List[NodeWithPath] = []
            total_size: int = 0
            total_files: int = 0
            for node in node_group.nodes:
                if node.is_dir:
                    if not recursive:
                        print(
                            f"Not copying {node.full_path} "
                            "as it is a directory "
                            "(specify -r to copy directories recursively)"
                        )
                        continue
                    add_size, add_files = listing.du(node)
                    total_size += add_size
                    total_files += add_files
                    valid_nodes.append(node)
                else:
                    # This node is a file
                    total_size += node.size
                    total_files += 1
                    valid_nodes.append(node)

            if not valid_nodes:
                continue

            updated_nodes: List[NodeWithPath] = []

            if dql_only:
                # Skip downloading these nodes
                updated_nodes = valid_nodes
            else:
                updated_nodes = listing.download_nodes(
                    valid_nodes,
                    self.cache,
                    total_size,
                    recursive=recursive,
                )

            # This assert is hopefully not necessary, but is here mostly to
            # ensure this functionality stays consistent (and catch any bugs)
            assert len(valid_nodes) == len(updated_nodes)

            instantiated_nodes = listing.instantiate_nodes(
                updated_nodes,
                output,
                self.cache,
                total_files,
                recursive=recursive,
                copy_dir_contents=source_path.endswith("/"),
                virtual_only=dql_only,
                relative_path=source_path,
            )

            for node in instantiated_nodes:
                if not node.is_dir:
                    metafile_group["files"].append(node.get_metafile_data())
            if metafile_group["files"]:
                metafile_data.append(metafile_group)

        if not metafile_data or no_dql_file:
            # Don't write the metafile if nothing was copied (or skipped)
            return metafile_data

        print(f"Creating '{dataset_file}'")

        with open(dataset_file, "w", encoding="utf-8") as fd:
            yaml.dump(metafile_data, fd, sort_keys=False)

        return metafile_data

    def du(
        self,
        sources,
        depth=0,
        ttl=TTL_INT,
        update=False,
        *,
        client_config=None,
    ) -> Iterable[Tuple[str, float]]:
        sources = Catalog.enlist_sources(
            self.data_storage,
            sources,
            ttl,
            update,
            client_config=client_config,
        )

        def du_dirs(src, node, subdepth):
            if subdepth > 0:
                subdirs = src.listing.data_storage.get_nodes_by_parent_id(
                    node.id, type_filter="dir"
                )
                for sd in subdirs:
                    yield from du_dirs(src, sd, subdepth - 1)
            yield (src.get_node_full_path(node), src.listing.du(node)[0])

        for src in sources:
            yield from du_dirs(src, src.node, depth)

    def find(
        self,
        sources,
        ttl=TTL_INT,
        update=False,
        names=None,
        inames=None,
        paths=None,
        ipaths=None,
        size=None,
        typ=None,
        jmespath=None,
        columns=None,
        *,
        client_config=None,
    ) -> Iterable[str]:
        sources = Catalog.enlist_sources(
            self.data_storage,
            sources,
            ttl,
            update,
            client_config=client_config,
        )
        if not columns:
            columns = ["path"]
        for src in sources:
            nodes = src.listing.find(
                src.node, names, inames, paths, ipaths, size, typ, jmespath
            )
            for node in nodes:
                yield "\t".join(
                    [
                        find_column_to_str(node, src, column)
                        for column in columns
                    ]
                )

    def index(
        self, sources, ttl=TTL_INT, update=False, *, client_config=None
    ) -> List["DataSource"]:
        root_sources = [
            src
            for src in sources
            if Client.get_implementation(src).is_root_url(src)
        ]
        non_root_sources = [
            src
            for src in sources
            if not Client.get_implementation(src).is_root_url(src)
        ]

        client_config = client_config or {}

        # for root sources (e.g s3://) we are just getting all buckets and
        # saving them as storages, without further indexing in each bucket
        for source in root_sources:
            for bucket in Client.get_implementation(source).ls_buckets(
                **client_config
            ):
                client, _ = Client.parse_url(bucket.uri)
                print(f"Registering storage {client.uri}")
                self.data_storage.create_storage_if_not_registered(client.uri)

        return Catalog.enlist_sources(
            self.data_storage,
            non_root_sources,
            ttl,
            update,
            client_config=client_config,
        )
