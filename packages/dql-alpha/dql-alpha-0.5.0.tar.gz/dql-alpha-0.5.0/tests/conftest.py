import os
from pathlib import PosixPath
from typing import Dict, Generator, NamedTuple, Type

import pytest
from pytest import MonkeyPatch, TempPathFactory
from upath.implementations.cloud import CloudPath

from dql.catalog import Catalog
from dql.data_storage import SQLiteDataStorage
from dql.utils import DQLDir

DEFAULT_DQL_BIN = "dql"
DEFAULT_DQL_GIT_REPO = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# JSON tests are currently ignored as they are a work in progress for SQLite
collect_ignore = ["setup.py", "unit/test_json.py"]


@pytest.fixture(scope="session")
def monkeypatch_session() -> Generator[MonkeyPatch, None, None]:
    """
    Like monkeypatch, but for session scope.
    """
    mpatch = pytest.MonkeyPatch()
    yield mpatch
    mpatch.undo()


@pytest.fixture(scope="session", autouse=True)
def clean_environment(
    monkeypatch_session: MonkeyPatch,  # pylint: disable=redefined-outer-name
    tmp_path_factory: TempPathFactory,
) -> None:
    """
    Make sure we have a clean environment and won't write to userspace.
    """
    working_dir = str(tmp_path_factory.mktemp("default_working_dir"))
    os.chdir(working_dir)
    monkeypatch_session.delenv(DQLDir.ENV_VAR, raising=False)

    def default_root(cls: Type[DQLDir]) -> str:
        return os.path.join(working_dir, cls.DEFAULT)

    monkeypatch_session.setattr(
        "dql.utils.DQLDir.default_root",
        classmethod(default_root),
    )


@pytest.fixture
def data_storage():
    _data_storage = SQLiteDataStorage(db_file=":memory:")
    yield _data_storage

    # Check that the DB isn't locked after the test
    conn = _data_storage.clone().db
    conn.execute("BEGIN IMMEDIATE")
    conn.commit()


@pytest.fixture
def tmp_dir(tmp_path_factory, monkeypatch):
    dpath = tmp_path_factory.mktemp("dql-test")
    monkeypatch.chdir(dpath)
    return dpath


def pytest_addoption(parser):
    parser.addoption(
        "--dql-bin",
        type=str,
        default=DEFAULT_DQL_BIN,
        help="Path to dql binary",
    )

    parser.addoption(
        "--dql-revs",
        type=str,
        help=(
            "Comma-separated list of DQL revisions to test "
            "(overrides `--dql-bin`)"
        ),
    )

    parser.addoption(
        "--dql-git-repo",
        type=str,
        default=DEFAULT_DQL_GIT_REPO,
        help="Path or url to dql git repo",
    )


class DQLTestConfig:
    def __init__(self):
        self.dql_bin = DEFAULT_DQL_BIN
        self.dql_revs = None
        self.dql_git_repo = DEFAULT_DQL_GIT_REPO


@pytest.fixture(scope="session")
def test_config(request):
    return request.config.dql_config


def pytest_configure(config):
    config.dql_config = DQLTestConfig()

    config.dql_config.dql_bin = config.getoption("--dql-bin")
    config.dql_config.dql_revs = config.getoption("--dql-revs")
    config.dql_config.dql_git_repo = config.getoption("--dql-git-repo")


class CloudTestCatalog(NamedTuple):
    src: CloudPath
    working_dir: PosixPath
    catalog: Catalog
    client_config: Dict[str, str]


class CloudTestServer(NamedTuple):
    src: CloudPath
    client_config: Dict[str, str]


# Test servers can be cached as they are not modified in these tests
cloud_server_cache: Dict[str, CloudTestServer] = {}


@pytest.fixture
def cloud_test_catalog(
    request,
    tmp_path,
    tmp_upath_factory,
    data_storage,  # pylint: disable=redefined-outer-name # noqa: E501
):
    cloud_type = request.param
    if cloud_type in cloud_server_cache:
        src_path = cloud_server_cache[cloud_type].src
        client_config = cloud_server_cache[cloud_type].client_config
    else:
        src_path = tmp_upath_factory.mktemp(cloud_type)
        fs = src_path._accessor._fs  # pylint:disable=protected-access
        if cloud_type == "s3":
            endpoint_url = fs.client_kwargs["endpoint_url"]
            client_config = {"aws_endpoint_url": endpoint_url}
        elif cloud_type == "gcs":
            endpoint_url = fs._endpoint  # pylint:disable=protected-access
            client_config = {"endpoint_url": endpoint_url}
        else:
            raise ValueError(f"invalid cloud_type: {cloud_type}")
        (src_path / "description").write_text("Cats and Dogs")
        (src_path / "cats" / "cat1").write_text("meow")
        (src_path / "cats" / "cat2").write_text("mrow")
        (src_path / "dogs" / "dog1").write_text("woof")
        (src_path / "dogs" / "dog2").write_text("arf")
        (src_path / "dogs" / "dog3").write_text("bark")
        (src_path / "dogs" / "others" / "dog4").write_text("ruff")
        cloud_server_cache[cloud_type] = CloudTestServer(
            src=src_path,
            client_config=client_config,
        )

    cache_dir = tmp_path / ".dql" / "cache"
    cache_dir.mkdir(parents=True)
    tmpfile_dir = tmp_path / ".dql" / "tmp"
    tmpfile_dir.mkdir()

    catalog = Catalog(
        data_storage, cache_dir=str(cache_dir), tmp_dir=str(tmpfile_dir)
    )

    return CloudTestCatalog(
        src=src_path,
        working_dir=tmp_path,
        catalog=catalog,
        client_config=client_config,
    )
