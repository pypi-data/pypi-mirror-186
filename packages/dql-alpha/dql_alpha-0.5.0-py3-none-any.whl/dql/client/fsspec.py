import asyncio
import multiprocessing
from abc import abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING, ClassVar, Iterator, Tuple, Type

from fsspec.asyn import get_loop
from tqdm import tqdm

from dql.client.base import Bucket, Client
from dql.data_storage import AbstractDataStorage
from dql.nodes_fetcher import NodesFetcher
from dql.nodes_thread_pool import NodeChunk

if TYPE_CHECKING:
    from fsspec.spec import AbstractFileSystem

FETCH_WORKERS = 100


class FSSpecClient(Client):
    MAX_THREADS = multiprocessing.cpu_count()
    FS_CLASS: ClassVar[Type["AbstractFileSystem"]]
    PREFIX: ClassVar[str]

    def __init__(self, name, fs):
        self.name = name
        self.fs = fs

    @classmethod
    def create_fs(cls, **kwargs) -> "AbstractFileSystem":
        kwargs.setdefault("version_aware", True)
        return cls.FS_CLASS(**kwargs)

    @classmethod
    def ls_buckets(cls, **kwargs) -> Iterator[Bucket]:
        for entry in cls.create_fs(**kwargs).ls(cls.PREFIX, detail=True):
            name = entry["name"].rstrip("/")
            yield Bucket(
                name=name,
                uri=f"{cls.PREFIX}{name}",
                created=entry.get("CreationDate"),
            )

    @classmethod
    def is_root_url(cls, url) -> bool:
        return url == cls.PREFIX

    @property
    def uri(self):
        return f"{self.PREFIX}{self.name}"

    @classmethod
    def _parse_url(
        cls,
        source: str,
        **kwargs,
    ) -> Tuple["FSSpecClient", str]:
        """
        Returns storage representation of bucket and the rest of the path
        in source.
        E.g if the source is s3://bucket_name/dir1/dir2/dir3 this method would
        return Storage object of bucket_name and a path which is dir1/dir2/dir3
        """
        fill_path = source[len(cls.PREFIX) :]
        path_split = fill_path.split("/", 1)
        storage = path_split[0]
        path = path_split[1] if len(path_split) > 1 else ""
        client = cls(storage, **kwargs)
        return client, path

    async def fetch(self, listing):
        data_storage = listing.data_storage.clone()
        root_id = await listing.insert_root(data_storage=data_storage)
        progress_bar = tqdm(desc=f"Listing {self.uri}", unit=" objects")
        loop = get_loop()

        queue = asyncio.Queue()
        queue.put_nowait((root_id, ""))

        async def worker(queue, data_storage):
            while True:
                dir_id, prefix = await queue.get()
                try:
                    subdirs = await self._fetch_dir(
                        dir_id,
                        prefix,
                        "/",
                        progress_bar,
                        listing,
                        data_storage,
                    )
                    for subdir in subdirs:
                        queue.put_nowait(subdir)
                finally:
                    queue.task_done()

        workers = []
        for _ in range(FETCH_WORKERS):
            workers.append(loop.create_task(worker(queue, data_storage)))

        await queue.join()
        for worker in workers:
            worker.cancel()
        await asyncio.gather(*workers)

    async def _fetch_dir(
        self, dir_id, prefix, delimiter, pbar, listing, data_storage
    ):
        path = f"{self.name}/{prefix}"
        # pylint:disable-next=protected-access
        infos = await self.fs._ls(path, detail=True, versions=True)
        files = []
        subdirs = set()
        for info in infos:
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
        if files:
            await data_storage.insert_entries(files)
        pbar.update(len(subdirs) + len(files))
        return subdirs

    @classmethod
    @abstractmethod
    def _dict_from_info(cls, v, parent_id, delimiter, path):
        ...

    def fetch_nodes(
        self,
        file_path,
        nodes,
        cache,
        data_storage: AbstractDataStorage,
        total_size=None,
        cls=NodesFetcher,
        pb_descr="Download",
    ):
        fetcher = cls(
            self,
            data_storage,
            file_path,
            self.MAX_THREADS,
            cache,
        )

        chunk_gen = NodeChunk(nodes)
        target_name = self.visual_file_name(file_path)
        pb_descr = f"{pb_descr} {target_name}"
        return fetcher.run(chunk_gen, pb_descr, total_size)

    def iter_object_chunks(self, bucket, path, version=None):
        with self.fs.open(f"{bucket}/{path}", version_id=version) as f:
            chunk = f.read()
            while chunk:
                yield chunk
                chunk = f.read()

    @staticmethod
    def visual_file_name(file_path):
        target_name = file_path.rstrip("/").split("/")[-1]
        max_len = 25
        if len(target_name) > max_len:
            target_name = "..." + target_name[max_len - 3 :]
        return target_name
