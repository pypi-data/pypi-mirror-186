import os
import os.path as osp
import stat
from typing import Iterable, Optional, Type, TypeVar

from dateutil.parser import isoparse

GLOB_CHARS = ["?", "*", "[", "]"]

T = TypeVar("T", bound="DQLDir")


class DQLDir:
    DEFAULT = ".dql"
    CACHE = "cache"
    TMP = "tmp"
    DB = "db"
    ENV_VAR = "DQL_DIR"

    def __init__(
        self,
        root: Optional[str] = None,
        cache: Optional[str] = None,
        tmp: Optional[str] = None,
        db: Optional[str] = None,
    ) -> None:
        self.root = (
            osp.abspath(root) if root is not None else self.default_root()
        )
        self.cache = (
            osp.abspath(cache)
            if cache is not None
            else osp.join(self.root, self.CACHE)
        )
        self.tmp = (
            osp.abspath(tmp)
            if tmp is not None
            else osp.join(self.root, self.TMP)
        )
        self.db = (
            osp.abspath(db) if db is not None else osp.join(self.root, self.DB)
        )

    def init(self):
        os.makedirs(self.root, exist_ok=True)
        os.makedirs(self.cache, exist_ok=True)
        os.makedirs(self.tmp, exist_ok=True)
        os.makedirs(osp.split(self.db)[0], exist_ok=True)

    @classmethod
    def default_root(cls) -> str:
        return osp.join(os.getcwd(), cls.DEFAULT)

    @classmethod
    def find(cls: Type[T], create: bool = True) -> T:
        try:
            root = os.environ[cls.ENV_VAR]
        except KeyError:
            root = cls.default_root()
        instance = cls(root)
        if not osp.isdir(root):
            if create:
                instance.init()
            else:
                NotADirectoryError(root)
        return instance


def human_time_to_int(time: str) -> Optional[int]:
    if not time:
        return None

    suffix = time[-1]
    try:
        num = int(time if suffix.isdigit() else time[:-1])
    except ValueError:
        return None
    return num * {
        "h": 60 * 60,
        "d": 60 * 60 * 24,
        "w": 60 * 60 * 24 * 7,
        "m": 31 * 24 * 60 * 60,
        "y": 60 * 60 * 24 * 365,
    }.get(suffix.lower(), 1)


def time_to_str(dt):
    if isinstance(dt, str):
        dt = isoparse(dt)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def sizeof_fmt(num, suffix="", si=False):
    power = 1000.0 if si else 1024.0
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z", "Y", "R"]:
        if abs(num) < power:
            if not unit:
                return f"{num:4.0f}{suffix}"
            return f"{num:3.1f}{unit}{suffix}"
        num /= power
    return f"{num:.1f}Q{suffix}"


def force_create_dir(name):
    if not os.path.exists(name):
        os.mkdir(name)
    elif not os.path.isdir(name):
        os.remove(name)
        os.mkdir(name)


def sql_str(s: str) -> str:
    s = s.replace("'", "''")
    return f"'{s}'"


SIZE_SUFFIXES = ["", "K", "M", "G", "T", "P", "E", "Z", "Y", "R", "Q"]


def suffix_to_number(num_str: str) -> Optional[int]:
    if not num_str:
        return None
    try:
        if len(num_str) > 1:
            suffix = num_str[-1].upper()
            if suffix in SIZE_SUFFIXES:
                suffix_idx = SIZE_SUFFIXES.index(suffix)
                return int(num_str[:-1]) * (1024**suffix_idx)
        return int(num_str)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid number/suffix for: {num_str}")


def sql_file_filter(
    names=None,
    inames=None,
    paths=None,
    ipaths=None,
    size=None,
    type=None,  # pylint: disable=redefined-builtin
    op="GLOB",
):
    all_filters = []

    names_sql = (
        [f"name {op} {sql_str(name)}" for name in names] if names else []
    )
    inames_sql = (
        [f"LOWER(name) {op} {sql_str(iname.lower())}" for iname in inames]
        if inames
        else []
    )
    name_filter = " OR ".join(names_sql + inames_sql)
    if name_filter:
        all_filters.append(name_filter)

    paths_sql = (
        [f"path_str {op} {sql_str(path)}" for path in paths] if paths else []
    )
    ipaths_sql = (
        [f"LOWER(path_str) {op} {sql_str(ipath.lower())}" for ipath in ipaths]
        if ipaths
        else []
    )
    path_filter = " OR ".join(paths_sql + ipaths_sql)
    if path_filter:
        all_filters.append(path_filter)

    size_limit = suffix_to_number(size)
    if size_limit:
        if size_limit < 0:
            all_filters.append(
                f"size <= {-size_limit}"  # pylint: disable=invalid-unary-operand-type # noqa: E501
            )
        else:
            all_filters.append(f"size >= {size_limit}")

    type_filter = None
    if type in ["f", "file", "files"]:
        type_filter = "dir_type = 0"
    elif type in ["d", "dir", "directory", "directories"]:
        type_filter = "dir_type > 0"

    if type and type_filter is None:
        raise RuntimeError(f"Not supported 'type': {type}")
    if type_filter:
        all_filters.append(type_filter)

    # This returns "" if no filters are specified
    return " AND ".join(f"({f})" for f in all_filters)


def dql_paths_join(
    source_path: str, file_paths: Iterable[str]
) -> Iterable[str]:
    source_parts = source_path.rstrip("/").split("/")
    if set(source_parts[-1]).intersection(GLOB_CHARS):
        # Remove last element if it is a glob match (such as *)
        source_parts.pop()
    source_stripped = "/".join(source_parts)
    return (f"{source_stripped}/{path.lstrip('/')}" for path in file_paths)


# From: https://docs.python.org/3/library/shutil.html#rmtree-example
def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)
