from abc import ABCMeta
from dataclasses import dataclass

from tdm.future.datamodel.nodes import AbstractNode


@dataclass(frozen=True)
class AbstractNodeMention(metaclass=ABCMeta):
    node: AbstractNode

    @property
    def node_id(self) -> str:
        return self.node.id
