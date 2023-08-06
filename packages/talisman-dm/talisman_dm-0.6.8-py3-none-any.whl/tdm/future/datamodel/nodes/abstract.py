import uuid
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Generic, Optional, TypeVar


class NodeType(str, Enum):
    TEXT = "text"
    KEY = "key"
    IMAGE = "image"
    FILE = "file"
    BASE64 = "base64"
    LIST = "list"
    JSON = "json"
    TABLE = "table"
    ROW = "row"
    CELL = "cell"


@dataclass(frozen=True)
class BaseNodeMetadata:
    hidden: bool = False


_NodeMetadata = TypeVar("_NodeMetadata", bound=BaseNodeMetadata)


class AbstractNode(Generic[_NodeMetadata]):
    __slots__ = ('_id', '_type', '_metadata')

    def __init__(self, type_: NodeType, metadata: _NodeMetadata, *, id_: Optional[str]):
        self._id = id_ or self.generate_id()
        self._type = type_
        self._metadata = metadata

    @property
    def id(self) -> str:
        return self._id

    @property
    def type(self) -> NodeType:
        return self._type

    @property
    def metadata(self) -> _NodeMetadata:
        return self._metadata

    def __hash__(self) -> int:
        return hash((self._id, self._type))

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, AbstractNode):
            return NotImplemented
        return self._id == o._id and self._type == o._type and self._metadata == o._metadata

    @classmethod
    @abstractmethod
    def node_type(cls) -> NodeType:
        pass

    @staticmethod
    def generate_id():
        return str(uuid.uuid4())


_Content = TypeVar('_Content')


class AbstractContentNode(AbstractNode[_NodeMetadata], Generic[_NodeMetadata, _Content], metaclass=ABCMeta):
    __slots__ = ('_content',)

    def __init__(self, type_: NodeType, content: _Content, metadata: _NodeMetadata, *, id_: Optional[str]):
        super().__init__(type_, metadata, id_=id_)
        self._content = content

    @property
    def content(self) -> _Content:
        return self._content

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, AbstractContentNode):
            return NotImplemented
        return self._id == o._id and self._type == o._type and self._metadata == o._metadata and self._content == o._content
