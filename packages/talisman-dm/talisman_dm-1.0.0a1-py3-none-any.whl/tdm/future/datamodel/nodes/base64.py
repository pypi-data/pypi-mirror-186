from dataclasses import dataclass
from typing import Optional

from .abstract import AbstractContentNode, BaseNodeMetadata, NodeType


@dataclass(frozen=True)
class Base64NodeMetadata(BaseNodeMetadata):
    content_type: Optional[str] = None


class Base64Node(AbstractContentNode[Base64NodeMetadata, str]):
    __slots__ = ()

    def __init__(self, text: str, metadata: Base64NodeMetadata = None, *, id_: Optional[str] = None):
        super().__init__(NodeType.BASE64, text, metadata if metadata is not None else Base64NodeMetadata(), id_=id_)

    @classmethod
    def node_type(cls) -> NodeType:
        return NodeType.BASE64
