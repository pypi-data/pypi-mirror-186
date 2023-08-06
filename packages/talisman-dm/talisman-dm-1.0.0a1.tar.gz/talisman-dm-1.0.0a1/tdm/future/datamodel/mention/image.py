from dataclasses import dataclass

from tdm.future.datamodel.nodes import NodeType
from .abstract import AbstractNodeMention


@dataclass(frozen=True)
class ImageNodeMention(AbstractNodeMention):
    top: int
    bottom: int
    left: int
    right: int

    def __post_init__(self):
        if self.node.node_type() is not NodeType.IMAGE:
            raise ValueError(f"Image node mention could be applied only for image nodes (got <{self.node.node_type()}>)")
        if self.top < 0 or self.bottom <= self.top or self.left < 0 or self.right <= self.left:
            raise ValueError(f"Incorrect bbox [({self.top}, {self.left}); ({self.bottom}, {self.right})]")
