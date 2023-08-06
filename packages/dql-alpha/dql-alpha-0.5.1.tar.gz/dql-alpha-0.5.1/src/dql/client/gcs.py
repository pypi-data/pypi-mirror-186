from base64 import b64decode

from gcsfs import GCSFileSystem

from .fsspec import FSSpecClient

# Patch gcsfs for consistency with s3fs
# pylint:disable-next=protected-access
GCSFileSystem.set_session = GCSFileSystem._set_session


class GCSClient(FSSpecClient):
    FS_CLASS = GCSFileSystem
    PREFIX = "gcs://"
    protocol = "gcs"

    def __init__(self, name, **kwargs):
        super().__init__(name, self.create_fs(**kwargs))

    @classmethod
    def _dict_from_info(cls, v, parent_id, delimiter, path):
        return {
            "is_dir": False,
            "parent_id": parent_id,
            "path": path,
            "name": v.get("name", "").split(delimiter)[-1],
            # 'expires': expires,
            "checksum": b64decode(v.get("md5Hash", "")).hex(),
            "etag": v.get("etag", ""),
            "version": v.get("generation", ""),
            "is_latest": not v.get("timeDeleted"),
            "last_modified": v["updated"],
            "size": v.get("size", ""),
            # 'storage_class': v.get('StorageClass'),
            "owner_name": "",
            "owner_id": "",
            "anno": None,
        }
