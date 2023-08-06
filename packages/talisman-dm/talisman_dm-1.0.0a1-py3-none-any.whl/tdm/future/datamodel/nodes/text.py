from dataclasses import dataclass
from typing import Optional

from .abstract import AbstractContentNode, BaseNodeMetadata, NodeType


@dataclass(frozen=True)
class TextNodeMetadata(BaseNodeMetadata):
    language: Optional[str] = None


class TextNode(AbstractContentNode[TextNodeMetadata, str]):
    __slots__ = ()

    def __init__(self, text: str, metadata: TextNodeMetadata = None, *, id_: Optional[str] = None):
        super().__init__(NodeType.TEXT, text, metadata if metadata is not None else TextNodeMetadata(), id_=id_)

    @classmethod
    def node_type(cls) -> NodeType:
        return NodeType.TEXT


class KeyNode(AbstractContentNode[TextNodeMetadata, str]):
    __slots__ = ()

    def __init__(self, key: str, metadata: TextNodeMetadata = None, *, id_: Optional[str] = None):
        super().__init__(NodeType.KEY, key, metadata if metadata is not None else TextNodeMetadata(), id_=id_)

    @classmethod
    def node_type(cls) -> NodeType:
        return NodeType.KEY
