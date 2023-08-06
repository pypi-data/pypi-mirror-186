import logging
import os
import sys
import traceback
from argparse import Action, ArgumentParser, ArgumentTypeError, Namespace
from itertools import chain
from typing import Iterator, List, Optional, Tuple, Union

import shtab

from dql import __version__, utils
from dql.catalog import Catalog
from dql.client import Client
from dql.data_storage import SQLiteDataStorage
from dql.node import long_line_str

logger = logging.getLogger("dql")

TTL_HUMAN = "4h"
TTL_INT = 4 * 60 * 60
FIND_COLUMNS = ["du", "name", "owner", "path", "size", "type"]


def human_time_type(
    value_str: str, can_be_none: bool = False
) -> Optional[int]:
    value = utils.human_time_to_int(value_str)

    if value:
        return value
    if can_be_none:
        return None

    raise ArgumentTypeError(
        "This option supports only a human-readable time "
        "interval like 12h or 4w."
    )


def parse_find_column(column: str) -> str:
    column_lower = column.strip().lower()
    if column_lower in FIND_COLUMNS:
        return column_lower
    raise ArgumentTypeError(
        f"Invalid column for find: '{column}' "
        f"Options are: {','.join(FIND_COLUMNS)}"
    )


def find_columns_type(
    columns_str: str,
    default_colums_str: str = "path",
) -> List[str]:
    if not columns_str:
        columns_str = default_colums_str

    return [parse_find_column(c) for c in columns_str.split(",")]


def add_sources_arg(
    parser: ArgumentParser, nargs: Union[str, int] = "+"
) -> Action:
    return parser.add_argument(
        "sources",
        type=str,
        nargs=nargs,
        help="Data sources - paths to cloud storage dirs",
    )


def get_parser() -> ArgumentParser:
    parser = ArgumentParser(description="DQL: Data Query Language", prog="dql")

    parser.add_argument(
        "-V", "--version", action="version", version=__version__
    )

    parent_parser = ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "--aws-endpoint-url",
        type=str,
        help="AWS endpoint URL",
    )
    parent_parser.add_argument(
        "--aws-anon",
        action="store_true",
        help="AWS anon (aka awscli's --no-sign-request)",
    )
    parent_parser.add_argument(
        "--ttl",
        type=human_time_type,
        default=TTL_HUMAN,
        help="Time-to-live of data source cache. Negative equals forever.",
    )
    parent_parser.add_argument(
        "-u", "--update", action="count", default=0, help="Update cache"
    )
    parent_parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Verbose"
    )
    parent_parser.add_argument(
        "-q", "--quiet", action="count", default=0, help="Be quiet"
    )

    subp = parser.add_subparsers(help="Sub-command help", dest="command")
    parse_get = subp.add_parser(
        "get", parents=[parent_parser], help="Fetch a dataset"
    )
    parse_get.add_argument(
        "source", type=str, help="Data source - a path to a cloud storage dir"
    )
    parse_get.add_argument(  # type: ignore[attr-defined]
        "-o", "--output", type=str, help="Output"
    ).complete = shtab.DIR
    parse_get.add_argument(
        "-f",
        "--force",
        action="count",
        default=0,
        help="Force creating outputs",
    )
    parse_get.add_argument("-d", "--descr", type=str, help="Description")

    parse_cp = subp.add_parser(
        "cp", parents=[parent_parser], help="Copy data files from the cloud"
    )
    add_sources_arg(parse_cp).complete = shtab.DIR  # type: ignore[attr-defined] # noqa: E501
    parse_cp.add_argument("output", type=str, help="Output")
    parse_cp.add_argument(
        "-f",
        "--force",
        default=False,
        action="store_true",
        help="Force creating outputs",
    )
    parse_cp.add_argument(
        "-r",
        "-R",
        "--recursive",
        default=False,
        action="store_true",
        help="Copy directories recursively",
    )
    parse_cp.add_argument(
        "--dql-file",
        help="Use a different filename for the resulting DQL file",
    )
    parse_cp.add_argument(
        "--dql-only",
        default=False,
        action="store_true",
        help=(
            "Only create the resulting DQL file, "
            "do not download or copy files"
        ),
    )
    parse_cp.add_argument(
        "--no-glob",
        default=False,
        action="store_true",
        help="Do not expand globs (such as * or ?)",
    )
    parse_cp.add_argument(
        "--no-dql-file",
        default=False,
        action="store_true",
        help="Do not write a .dql file",
    )

    parse_ls = subp.add_parser(
        "ls", parents=[parent_parser], help="List storage contents"
    )
    add_sources_arg(parse_ls, nargs="*")
    parse_ls.add_argument(
        "-l",
        "--long",
        action="count",
        default=0,
        help="List files in the long format",
    )

    parse_du = subp.add_parser(
        "du", parents=[parent_parser], help="Display space usage"
    )
    add_sources_arg(parse_du)
    parse_du.add_argument(
        "-b",
        "--bytes",
        default=False,
        action="store_true",
        help="Display sizes in bytes instead of human-readable sizes",
    )
    parse_du.add_argument(
        "-d",
        "--depth",
        "--max-depth",
        default=0,
        type=int,
        metavar="N",
        help=(
            "Display sizes for N directory depths below the given directory, "
            "the default is 0 (summarize provided directory only)."
        ),
    )
    parse_du.add_argument(
        "--si",
        default=False,
        action="store_true",
        help="Display sizes using powers of 1000 not 1024",
    )

    parse_find = subp.add_parser(
        "find", parents=[parent_parser], help="Search in a directory hierarchy"
    )
    add_sources_arg(parse_find)
    parse_find.add_argument(
        "-name",
        "--name",
        type=str,
        action="append",
        help="Filename to match pattern.",
    )
    parse_find.add_argument(
        "-iname",
        "--iname",
        type=str,
        action="append",
        help="Like -name but case insensitive.",
    )
    parse_find.add_argument(
        "-path",
        "--path",
        type=str,
        action="append",
        help="Path to match pattern.",
    )
    parse_find.add_argument(
        "-ipath",
        "--ipath",
        type=str,
        action="append",
        help="Like -path but case insensitive.",
    )
    parse_find.add_argument(
        "-size",
        "--size",
        type=str,
        help=(
            "Filter by size (+ is greater or equal, - is less or equal). "
            "Specified size is in bytes, or use a suffix like K, M, G for "
            "kilobytes, megabytes, gigabytes, etc."
        ),
    )
    parse_find.add_argument(
        "-type",
        "--type",
        type=str,
        help='File type: "f" - regular, "d" - directory',
    )
    parse_find.add_argument(
        "-jmespath",
        "--jmespath",
        type=str,
        action="append",
        help="JMESPath query to annotation (not supported currently)",
    )
    parse_find.add_argument(
        "-c",
        "--columns",
        type=find_columns_type,
        default=None,
        help=(
            "A comma-separated list of columns to print for each result. "
            f"Options are: {','.join(FIND_COLUMNS)} (Default: path)"
        ),
    )

    parse_index = subp.add_parser(
        "index", parents=[parent_parser], help="Index storage location"
    )
    add_sources_arg(parse_index)
    add_completion_parser(subp, [parent_parser])
    return parser


def add_completion_parser(subparsers, parents):
    parser = subparsers.add_parser(
        "completion",
        parents=parents,
        help="Output shell completion script",
    )
    parser.add_argument(
        "-s",
        "--shell",
        help="Shell syntax for completions.",
        default="bash",
        choices=shtab.SUPPORTED_SHELLS,
    )


def get_logging_level(args: Namespace) -> int:
    if args.quiet:
        return logging.CRITICAL
    elif args.verbose:
        return logging.DEBUG
    return logging.INFO


def get(source, output, **kwargs):
    data_storage = SQLiteDataStorage()
    catalog = Catalog(data_storage)
    catalog.get(source, output, **kwargs)


def cp(sources, output, **kwargs):
    data_storage = SQLiteDataStorage()
    catalog = Catalog(data_storage)
    catalog.cp(sources, output, **kwargs)


def ls_urls(
    sources,
    long: bool = False,
    *,
    client_config=None,
    catalog: Optional[Catalog] = None,
    **kwargs,
) -> Iterator[Tuple[str, Iterator[str]]]:
    if client_config is None:
        client_config = {}
    if catalog is None:
        catalog = Catalog(SQLiteDataStorage())

    curr_dir = None
    value_iterables = []
    for next_dir, values in _ls_urls_flat(
        sources, long, client_config, catalog, **kwargs
    ):
        if curr_dir is None or next_dir == curr_dir:  # type: ignore[unreachable] # noqa: E501
            value_iterables.append(values)
        else:
            yield curr_dir, chain(*value_iterables)  # type: ignore[unreachable] # noqa: E501
            value_iterables = [values]
        curr_dir = next_dir
    if curr_dir is not None:
        yield curr_dir, chain(*value_iterables)


def _ls_urls_flat(
    sources,
    long: bool,
    client_config,
    catalog: Catalog,
    **kwargs,
) -> Iterator[Tuple[str, Iterator[str]]]:
    for source in sources:
        client_cls = Client.get_implementation(source)
        if client_cls.is_root_url(source):
            buckets = client_cls.ls_buckets(**client_config)
            if long:
                values = (
                    long_line_str(b.name, b.created, "") for b in buckets
                )
            else:
                values = (b.name for b in buckets)
            yield source, values
        else:
            for data_source, nodes in catalog.ls(
                [source], client_config=client_config, **kwargs
            ):
                if long:
                    values = (n.long_line_str() for n in nodes)
                else:
                    values = (n.name_with_dir_ending for n in nodes)
                yield "/".join(data_source.node.path), values


def ls_indexed_storages(
    long: bool = False, catalog: Optional[Catalog] = None
) -> Iterator[str]:
    if catalog is None:
        catalog = Catalog(SQLiteDataStorage())
    storages = catalog.ls_storages()
    if long:
        for s in storages:
            # TODO: add Storage.created so it can be used here
            yield long_line_str(s.uri, None, "")
    else:
        for s in storages:
            yield s.uri


def ls(
    sources, long: bool = False, catalog: Optional[Catalog] = None, **kwargs
):
    if catalog is None:
        catalog = Catalog(SQLiteDataStorage())
    if sources:
        if len(sources) == 1:
            for _, entries in ls_urls(
                sources, long=long, catalog=catalog, **kwargs
            ):
                for entry in entries:
                    print(entry)
        else:
            first = True
            for source, entries in ls_urls(
                sources, long=long, catalog=catalog, **kwargs
            ):
                # print a newline between directory listings
                if first:
                    first = False
                else:
                    print()
                if source:
                    print(f"{source}:")
                for entry in entries:
                    print(entry)
    else:
        for entry in ls_indexed_storages(long=long, catalog=catalog):
            print(entry)


def du(sources, show_bytes=False, si=False, **kwargs):
    data_storage = SQLiteDataStorage()
    catalog = Catalog(data_storage)
    for path, size in catalog.du(sources, **kwargs):
        if show_bytes:
            print(f"{size} {path}")
        else:
            print(f"{utils.sizeof_fmt(size, si=si): >7} {path}")


def find(sources, **kwargs):
    data_storage = SQLiteDataStorage()
    catalog = Catalog(data_storage)
    yield from catalog.find(sources, **kwargs)


def index(sources, catalog: Optional[Catalog] = None, **kwargs):
    if catalog is None:
        catalog = Catalog(SQLiteDataStorage())
    catalog.index(sources, **kwargs)


def completion(shell: str) -> str:
    return shtab.complete(
        get_parser(),
        shell=shell,  # nosec B604
    )


def main(argv: Optional[List[str]] = None) -> int:  # noqa: C901
    parser = get_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 1

    logger.addHandler(logging.StreamHandler())
    logging_level = get_logging_level(args)
    logger.setLevel(logging_level)

    client_config = {
        "aws_endpoint_url": args.aws_endpoint_url,
        "aws_anon": args.aws_anon,
    }

    try:
        if args.command == "get":
            # TODO: descr = args.descr
            get(
                args.source,
                args.output,
                force=bool(args.force),
                update=bool(args.update),
                ttl=args.ttl,
                client_config=client_config,
            )
        elif args.command == "cp":
            cp(
                args.sources,
                args.output,
                force=bool(args.force),
                update=bool(args.update),
                recursive=bool(args.recursive),
                dql_file=args.dql_file,
                dql_only=args.dql_only,
                no_glob=args.no_glob,
                ttl=args.ttl,
                client_config=client_config,
            )
        elif args.command == "ls":
            ls(
                args.sources,
                ttl=args.ttl,
                update=bool(args.update),
                long=bool(args.long),
                client_config=client_config,
            )
        elif args.command == "du":
            du(
                args.sources,
                show_bytes=args.bytes,
                depth=args.depth,
                si=args.si,
                ttl=args.ttl,
                update=bool(args.update),
                client_config=client_config,
            )
        elif args.command == "find":
            results_found = False
            for result in find(
                args.sources,
                ttl=args.ttl,
                update=bool(args.update),
                names=args.name,
                inames=args.iname,
                paths=args.path,
                ipaths=args.ipath,
                size=args.size,
                typ=args.type,
                jmespath=args.jmespath,
                columns=args.columns,
                client_config=client_config,
            ):
                print(result)
                results_found = True
            if not results_found:
                print("No results")
        elif args.command == "index":
            index(
                args.sources,
                ttl=args.ttl,
                update=bool(args.update),
                client_config=client_config,
            )
        elif args.command == "completion":
            print(completion(args.shell))
        else:
            print(f"invalid command: {args.command}", file=sys.stderr)
            return 1
        return 0
    except BrokenPipeError:
        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown
        # See: https://docs.python.org/3/library/signal.html#note-on-sigpipe
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        return 141  # 128 + 13 (SIGPIPE)
    except Exception as exc:  # pylint: disable=broad-except
        print("Error:", exc, file=sys.stderr)
        if logging_level <= logging.DEBUG:
            traceback.print_exception(
                type(exc),
                exc,
                exc.__traceback__,
                file=sys.stderr,
            )
        return 1
