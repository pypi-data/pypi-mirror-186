from dataclasses import dataclass

from tdm.future.datamodel.nodes import NodeType
from .abstract import AbstractNodeMention


@dataclass(frozen=True)
class TextNodeMention(AbstractNodeMention):
    start: int
    end: int

    def __post_init__(self):
        if self.node.node_type() not in {NodeType.TEXT, NodeType.KEY}:
            raise ValueError(f"Text mention could be applied only for text nodes (got <{self.node.node_type()}>)")
        if self.start < 0 or self.end <= self.start:
            raise ValueError(f"Incorrect span [{self.start}, {self.end})")
