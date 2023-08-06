import posixpath
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from functools import cached_property
from typing import NamedTuple, Optional, Union
from urllib.parse import urlparse

from dateutil import tz
from dateutil.parser import isoparse

from dql.utils import time_to_str


class Status:
    CREATED = 1
    PENDING = 2
    FAILED = 3
    COMPLETE = 4


class AbstractStorage(ABC):
    @property
    @abstractmethod
    def uri(self) -> str:
        ...

    @property
    @abstractmethod
    def timestamp(self) -> Optional[Union[datetime, str]]:
        ...

    @property
    @abstractmethod
    def expires(self) -> Optional[Union[datetime, str]]:
        ...

    @property
    @abstractmethod
    def status(self) -> int:
        ...

    @property
    def type(self):
        return self._parsed_uri.scheme

    @property
    def name(self):
        return self._parsed_uri.netloc

    @cached_property
    def _parsed_uri(self):
        return urlparse(self.uri)


class StorageRecord(NamedTuple):
    uri: str
    timestamp: Optional[Union[datetime, str]] = None
    expires: Optional[Union[datetime, str]] = None
    status: int = Status.CREATED


class Storage(StorageRecord, AbstractStorage):
    @property
    def is_expired(self) -> bool:
        now = datetime.now()
        if self.expires:
            return self.time_to_local(self.expires) < self.time_to_local(now)

        return False

    @property
    def timestamp_str(self) -> Optional[str]:
        if not self.timestamp:
            return None
        return time_to_str(self.timestamp)

    @property
    def timestamp_to_local(self) -> Optional[str]:
        if not self.timestamp:
            return None
        return self.time_to_local_str(self.timestamp)

    @property
    def expires_to_local(self) -> Optional[str]:
        if not self.expires:
            return None
        return self.time_to_local_str(self.expires)

    @staticmethod
    def time_to_local_str(dt: Union[datetime, str]) -> str:
        return time_to_str(Storage.time_to_local(dt))

    @staticmethod
    def time_to_local(dt: Union[datetime, str]) -> datetime:
        # TODO check usage
        if isinstance(dt, str):
            dt = isoparse(dt)
        try:
            return dt.astimezone(tz.tzlocal())
        except (OverflowError, OSError, ValueError):
            return dt

    @staticmethod
    def get_expiration_time(timestamp: datetime, ttl: int):
        if ttl >= 0:
            try:
                return timestamp + timedelta(seconds=ttl)
            except OverflowError:
                return datetime.max
        else:
            return datetime.max

    def to_dict(self, file_path=""):
        uri = self.uri
        if file_path:
            uri = posixpath.join(uri, *file_path.rstrip("/").split("/"))
        return {
            "uri": uri,
            "timestamp": time_to_str(self.timestamp)
            if self.timestamp
            else None,
            "expires": time_to_str(self.expires) if self.expires else None,
        }
