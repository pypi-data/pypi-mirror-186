from datetime import datetime
from typing import cast

from dql.vendored.s3fs import S3FileSystem  # type: ignore[attr-defined]

from .fsspec import FSSpecClient

FETCH_CHUNKSIZE = 1000


class ClientS3(FSSpecClient):
    FS_CLASS = S3FileSystem
    PREFIX = "s3://"
    protocol = "s3"

    def __init__(self, name, **kwargs):
        super().__init__(name, self.create_fs(**kwargs))

    @classmethod
    def create_fs(cls, **kwargs) -> S3FileSystem:
        if "aws_anon" in kwargs:
            kwargs.setdefault("anon", kwargs.pop("aws_anon"))
        if "aws_endpoint_url" in kwargs:
            kwargs.setdefault("client_kwargs", {}).setdefault(
                "endpoint_url", kwargs.pop("aws_endpoint_url")
            )
        if "aws_key" in kwargs:
            kwargs.setdefault("key", kwargs.pop("aws_key"))
        if "aws_secret" in kwargs:
            kwargs.setdefault("secret", kwargs.pop("aws_secret"))
        if "aws_token" in kwargs:
            kwargs.setdefault("token", kwargs.pop("aws_token"))

        return cast(S3FileSystem, super().create_fs(**kwargs))

    async def _fetch_dir(
        self, dir_id, prefix, delimiter, pbar, listing, data_storage
    ):
        if prefix:
            prefix = prefix.lstrip("/") + "/"
        files = []
        subdirs = set()
        # pylint:disable-next=protected-access
        async for info in self.fs._iterdir(
            self.name, prefix=prefix, versions=True
        ):
            full_path = info["name"]
            _, subprefix, _ = self.fs.split_path(info["name"])
            if info["type"] == "directory":
                name = full_path.split(delimiter)[-1]
                new_dir_id = await listing.insert_dir(
                    dir_id,
                    name,
                    datetime.max,
                    subprefix,
                    data_storage=data_storage,
                )
                subdirs.add((new_dir_id, subprefix))
            else:
                files.append(
                    self._dict_from_info(info, dir_id, delimiter, subprefix)
                )
                if len(files) >= FETCH_CHUNKSIZE:
                    await data_storage.insert_entries(files)
                    pbar.update(len(files))
                    files = []
        if files:
            await data_storage.insert_entries(files)
            pbar.update(len(files))
        pbar.update(len(subdirs))
        return subdirs

    @staticmethod
    def clean_s3_version(ver):
        return ver if ver != "null" else ""

    @classmethod
    def _dict_from_info(cls, v, parent_id, delimiter, path):
        return {
            "is_dir": False,
            "parent_id": parent_id,
            "path": path,
            "name": v.get("Key", "").split(delimiter)[-1],
            # 'expires': expires,
            "checksum": "",
            "etag": v.get("ETag", "").strip('"'),
            "version": ClientS3.clean_s3_version(v.get("VersionId", "")),
            "is_latest": v.get("IsLatest", True),
            "last_modified": v.get("LastModified", ""),
            "size": v.get("Size", ""),
            # 'storage_class': v.get('StorageClass'),
            "owner_name": v.get("Owner", {}).get("DisplayName", ""),
            "owner_id": v.get("Owner", {}).get("ID", ""),
            "anno": None,
        }
