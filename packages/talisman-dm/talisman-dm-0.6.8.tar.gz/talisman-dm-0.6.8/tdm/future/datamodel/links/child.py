from typing import Union

from tdm.future.datamodel.mention import NodeMention
from tdm.future.datamodel.nodes import AbstractNode
from .abstract import AbstractNodeLink, NodeLinkType


class ChildNodeLink(AbstractNodeLink[NodeMention, NodeMention]):
    def __init__(self, source: Union[NodeMention, AbstractNode], target: Union[NodeMention, AbstractNode]):
        if isinstance(source, AbstractNode):
            source = NodeMention(source)
        if isinstance(target, AbstractNode):
            target = NodeMention(target)
        super().__init__(NodeLinkType.child, source, target, id_=target.node_id)  # assume id of child is the same as target node
