from abc import ABC, abstractmethod
from datetime import datetime
from typing import ClassVar, Iterator, NamedTuple, Optional, Tuple, Type


class Bucket(NamedTuple):
    name: str
    uri: str
    created: Optional[datetime]


class Client(ABC):
    name: str
    protocol: ClassVar[str]

    @staticmethod
    def get_implementation(url: str) -> Type["Client"]:
        from .gcs import GCSClient
        from .s3 import ClientS3

        if url.startswith(ClientS3.PREFIX):
            return ClientS3
        if url.startswith(GCSClient.PREFIX):
            return GCSClient
        raise RuntimeError(f"Unsupported data source format '{url}'")

    @staticmethod
    def parse_url(source: str, **kwargs) -> Tuple["Client", str]:
        cls = Client.get_implementation(source)
        return cls._parse_url(  # pylint:disable=protected-access
            source, **kwargs
        )

    @classmethod
    @abstractmethod
    def is_root_url(cls, url) -> bool:
        ...

    @classmethod
    @abstractmethod
    def _parse_url(cls, source: str, **kwargs) -> Tuple["Client", str]:
        ...

    @classmethod
    @abstractmethod
    def ls_buckets(cls, **kwargs) -> Iterator[Bucket]:
        ...

    @property
    @abstractmethod
    def uri(self) -> str:
        ...
