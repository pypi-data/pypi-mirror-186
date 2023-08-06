from dataclasses import dataclass
from typing import Optional

from .abstract import AbstractContentNode, BaseNodeMetadata, NodeType


@dataclass(frozen=True)
class FileNodeMetadata(BaseNodeMetadata):
    name: Optional[str] = None
    size: Optional[int] = None


class FileNode(AbstractContentNode[FileNodeMetadata, str]):
    __slots__ = ()

    def __init__(self, path: str, metadata: FileNodeMetadata = None, *, id_: Optional[str] = None):
        super().__init__(NodeType.FILE, path, metadata if metadata is not None else FileNodeMetadata(), id_=id_)

    @classmethod
    def node_type(cls) -> NodeType:
        return NodeType.FILE


@dataclass(frozen=True)
class ImageNodeMetadata(FileNodeMetadata):
    width: Optional[int] = None
    height: Optional[int] = None


class ImageNode(AbstractContentNode[ImageNodeMetadata, str]):
    __slots__ = ()

    def __init__(self, path: str, metadata: ImageNodeMetadata = None, *, id_: Optional[str] = None):
        super().__init__(NodeType.IMAGE, path, metadata if metadata is not None else ImageNodeMetadata(), id_=id_)

    @classmethod
    def node_type(cls) -> NodeType:
        return NodeType.IMAGE
