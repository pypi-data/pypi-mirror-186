import logging
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple

from dql.node import Node, NodeWithPath
from dql.storage import Storage

DB_FILE_NAME = "db"


logger = logging.getLogger("dql")


class AbstractDataStorage(ABC):
    @abstractmethod
    def clone(self, uri: Optional[str]) -> "AbstractDataStorage":
        """Clones DataStorage implementation for some Storage input"""

    @abstractmethod
    def init_db(self):
        """Initializes database tables for data storage"""

    @abstractmethod
    async def insert_entry(self, entry: Dict[str, Any]) -> int:
        """
        Inserts file or directory node into the database
        and returns the id of the newly added node
        """

    @abstractmethod
    async def insert_entries(self, entries: List[Dict[str, Any]]) -> None:
        """Inserts file or directory nodes into the database"""

    @abstractmethod
    async def insert_root(self) -> int:
        """
        Inserts root directory and returns the id of the newly added root
        """

    @abstractmethod
    def get_node_by_id(self, node_id: int) -> Optional[NodeWithPath]:
        """Gets node from database by id"""

    @abstractmethod
    def get_nodes_by_id(
        self, node_ids: Iterable[int]
    ) -> Iterable[NodeWithPath]:
        """Gets nodes from database by id"""

    @abstractmethod
    def get_node_by_name_and_parent(
        self, name: str, parent_id: int
    ) -> Optional[NodeWithPath]:
        """Gets node from database by name and parent_id"""

    @abstractmethod
    def get_nodes_by_parent_id(
        self,
        parent_id: int,
        type_filter: Optional[str] = None,
    ) -> Iterable[NodeWithPath]:
        """Gets nodes from database by parent_id, with optional filtering"""

    @abstractmethod
    def create_storage_if_not_registered(self, uri: str) -> None:
        """
        Saves new storage if it doesn't exist in database
        """

    @abstractmethod
    def register_storage_for_indexing(
        self, uri: str, force_update: bool
    ) -> Tuple[Storage, bool, bool]:
        """
        Prepares storage for indexing operation.
        This method should be called before index operation is started
        It returns:
            - storage, prepared for indexing
            - boolean saying if indexing is needed
            - boolean saying if indexing is currently pending (running)
        """

    @abstractmethod
    def mark_storage_indexed(
        self,
        uri: str,
        status: int,
        ttl: int,
        end_time: Optional[datetime] = None,
    ) -> None:
        """
        Marks storage as indexed.
        This method should be called when index operation is finished
        """

    @abstractmethod
    def get_storage_all(self) -> Iterator[Storage]:
        pass

    @abstractmethod
    def get_storage(self, uri: str) -> Optional[Storage]:
        """
        Gets storage representation from database.
        E.g if s3 is used as storage this would be s3 bucket data
        """

    @abstractmethod
    def size(self, node: NodeWithPath) -> Tuple[int, int]:
        """
        Calculates size of some node (and subtree below node).
        Returns size in bytes as int and total files as int
        """

    @abstractmethod
    def get_node_by_path(self, path: str) -> NodeWithPath:
        """Gets node that correspond to some path"""

    @abstractmethod
    def get_nodes_by_path(self, path: str) -> Iterable[NodeWithPath]:
        """
        Gets all nodes that correspond to some path. Note that path
        can have GLOB like patterns so multiple nodes can be returned. If
        path is strict (without GLOB patterns) only one node will be returned.
        """

    @abstractmethod
    def walk_subtree(
        self,
        node: NodeWithPath,
        sort_by_parent_id: bool = False,
        sort_by_size: bool = False,
        sort_by_path: bool = False,
        type_filter: Optional[str] = None,
        custom_filter: Optional[str] = None,
    ) -> Iterable[NodeWithPath]:
        """
        Returns all directory and file nodes that are "below" some node.
        Nodes can be sorted or filtered as well.
        """

    @abstractmethod
    def get_latest_files_by_parent_node(
        self, parent_node: Node
    ) -> Iterable[Node]:
        """
        Gets latest-version file nodes from the provided parent node
        """

    @abstractmethod
    def find(
        self,
        node: NodeWithPath,
        names=None,
        inames=None,
        paths=None,
        ipaths=None,
        size=None,
        type=None,  # pylint: disable=redefined-builtin
        jmespath="",
    ) -> Iterable[NodeWithPath]:
        """
        Tries to find nodes that match certain criteria like name or jmespath
        """

    @abstractmethod
    def update_annotation(self, node: Node, annotation_content: str) -> None:
        """Updates annotation of a specific node in database"""

    @abstractmethod
    def update_checksum(self, node: Node, checksum: str) -> None:
        """Updates checksum of specific node in database"""
