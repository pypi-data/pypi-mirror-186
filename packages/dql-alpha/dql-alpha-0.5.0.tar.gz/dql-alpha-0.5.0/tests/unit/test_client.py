import pytest

from dql.client import Client


def test_parse_url():
    bucket = "whatever"
    s3_bucket = "s3://" + bucket
    path = "my/path"
    c, p = Client.parse_url(s3_bucket + "/" + path)
    assert p == path
    assert c.name == bucket

    c, p = Client.parse_url(s3_bucket + "/" + path + "/")
    assert p == path + "/"


def test_bad_url():
    bucket = "whatever"
    path = "my/path"
    with pytest.raises(RuntimeError):
        Client.parse_url(bucket + "/" + path + "/")
