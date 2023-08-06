import pytest

from dql.cli import index, ls


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_ls_no_args(cloud_test_catalog, capsys):
    # These tests re-use the same database for better performance
    conn = cloud_test_catalog.catalog.data_storage.db
    conn.execute("DELETE FROM buckets")
    conn.commit()
    src = str(cloud_test_catalog.src).rstrip("/")
    catalog = cloud_test_catalog.catalog
    conf = cloud_test_catalog.client_config
    index([src], catalog=catalog, client_config=conf)
    ls(
        [],
        catalog=catalog,
        client_config=conf,
    )
    captured = capsys.readouterr()
    assert captured.out == f"{src}\n"


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_ls_root(cloud_test_catalog, capsys):
    src = str(cloud_test_catalog.src).rstrip("/")
    root = src[: src.find("://") + 3]
    src_name = src.replace(root, "", 1)
    ls(
        [root],
        catalog=cloud_test_catalog.catalog,
        client_config=cloud_test_catalog.client_config,
    )
    captured = capsys.readouterr()
    buckets = captured.out.split("\n")
    assert src_name in buckets


ls_sources_output = """\
cats/
dogs/
description

dogs/others:
dog4

dogs:
dog1
dog2
dog3
"""


@pytest.mark.parametrize("cloud_test_catalog", ["s3", "gcs"], indirect=True)
def test_ls_sources(cloud_test_catalog, capsys):
    src = str(cloud_test_catalog.src).rstrip("/")
    ls(
        [src, f"{src}/dogs/*"],
        catalog=cloud_test_catalog.catalog,
        client_config=cloud_test_catalog.client_config,
    )
    captured = capsys.readouterr()
    assert captured.out == ls_sources_output
