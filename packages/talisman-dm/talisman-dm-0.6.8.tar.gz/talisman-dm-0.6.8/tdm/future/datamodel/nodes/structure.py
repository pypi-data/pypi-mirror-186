from dataclasses import dataclass
from typing import Optional

from .abstract import AbstractNode, BaseNodeMetadata, NodeType


@dataclass(frozen=True)
class ListNodeMetadata(BaseNodeMetadata):
    bullet: Optional[str] = None


class ListNode(AbstractNode[ListNodeMetadata]):
    __slots__ = ()

    def __init__(self, metadata: ListNodeMetadata = None, *, id_: Optional[str] = None):
        super().__init__(NodeType.LIST, metadata if metadata is not None else ListNodeMetadata(), id_=id_)

    @classmethod
    def node_type(cls) -> NodeType:
        return NodeType.LIST


class JSONNode(AbstractNode[BaseNodeMetadata]):
    __slots__ = ()

    def __init__(self, metadata: BaseNodeMetadata = None, *, id_: Optional[str] = None):
        super().__init__(NodeType.JSON, metadata if metadata is not None else BaseNodeMetadata(), id_=id_)

    @classmethod
    def node_type(cls) -> NodeType:
        return NodeType.JSON


class TableNode(AbstractNode[BaseNodeMetadata]):
    __slots__ = ()

    def __init__(self, metadata: BaseNodeMetadata = None, *, id_: Optional[str] = None):
        super().__init__(NodeType.TABLE, metadata if metadata is not None else BaseNodeMetadata(), id_=id_)

    @classmethod
    def node_type(cls) -> NodeType:
        return NodeType.TABLE


@dataclass(frozen=True)
class TableRowNodeMetadata(BaseNodeMetadata):
    header: Optional[bool] = None


class TableRowNode(AbstractNode[TableRowNodeMetadata]):
    __slots__ = ()

    def __init__(self, metadata: TableRowNodeMetadata = None, *, id_: Optional[str] = None):
        super().__init__(NodeType.ROW, metadata if metadata is not None else TableRowNodeMetadata(), id_=id_)

    @classmethod
    def node_type(cls) -> NodeType:
        return NodeType.ROW


@dataclass(frozen=True)
class TableCellNodeMetadata(BaseNodeMetadata):
    colspan: Optional[int] = None
    rowspan: Optional[int] = None


class TableCellNode(AbstractNode[TableCellNodeMetadata]):
    __slots__ = ()

    def __init__(self, metadata: TableCellNodeMetadata = None, *, id_: Optional[str] = None):
        super().__init__(NodeType.CELL, metadata if metadata is not None else TableCellNodeMetadata(), id_=id_)

    @classmethod
    def node_type(cls) -> NodeType:
        return NodeType.CELL
