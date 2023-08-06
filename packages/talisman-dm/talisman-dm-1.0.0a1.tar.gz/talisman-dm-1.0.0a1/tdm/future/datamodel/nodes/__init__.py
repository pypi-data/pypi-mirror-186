__all__ = [
    'AbstractContentNode', 'AbstractNode', 'NodeType', 'NodeTypes',
    'Base64Node', 'Base64NodeMetadata',
    'FileNode', 'FileNodeMetadata', 'ImageNode', 'ImageNodeMetadata',
    'JSONNode', 'ListNode', 'ListNodeMetadata', 'TableCellNode', 'TableCellNodeMetadata', 'TableNode', 'TableRowNode',
    'TableRowNodeMetadata',
    'KeyNode', 'TextNode', 'TextNodeMetadata'
]

from frozendict import frozendict

from .abstract import AbstractContentNode, AbstractNode, NodeType
from .base64 import Base64Node, Base64NodeMetadata
from .file import FileNode, FileNodeMetadata, ImageNode, ImageNodeMetadata
from .structure import JSONNode, ListNode, ListNodeMetadata, TableCellNode, TableCellNodeMetadata, TableNode, TableRowNode, \
    TableRowNodeMetadata
from .text import KeyNode, TextNode, TextNodeMetadata

NodeTypes = frozendict({
    NodeType.BASE64: Base64Node,
    NodeType.FILE: FileNode,
    NodeType.IMAGE: ImageNode,
    NodeType.JSON: JSONNode,
    NodeType.LIST: ListNode,
    NodeType.TABLE: TableNode,
    NodeType.ROW: TableRowNode,
    NodeType.CELL: TableCellNode,
    NodeType.KEY: KeyNode,
    NodeType.TEXT: TextNode
})
