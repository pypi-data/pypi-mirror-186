from dataclasses import dataclass

from .abstract import AbstractNodeMention


# @final
@dataclass(frozen=True)
class NodeMention(AbstractNodeMention):
    pass
