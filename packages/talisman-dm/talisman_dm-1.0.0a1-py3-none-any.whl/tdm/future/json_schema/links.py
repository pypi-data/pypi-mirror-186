from typing import Dict, Generic, Tuple, Type, TypeVar

from pydantic import create_model
from pydantic.generics import GenericModel

from tdm.future.datamodel.links import AbstractNodeLink, NodeLinkType
from tdm.future.datamodel.nodes import AbstractNode
from .mention import AbstractNodeMentionModel, MentionModel, serialize_mention

_S = TypeVar('_S', bound=AbstractNodeMentionModel)
_T = TypeVar('_T', bound=AbstractNodeMentionModel)


class NodeLinkModel(GenericModel, Generic[_S, _T]):
    id: str
    source: _S
    target: _T

    def link(self, type_: Type[AbstractNodeLink], nodes: Dict[str, AbstractNode]) -> AbstractNodeLink:
        return type_(source=self.source.mention(nodes), target=self.target.mention(nodes), id_=self.id)  # link type specified by type_

    @classmethod
    def model(cls, link: AbstractNodeLink) -> 'NodeLinkModel':
        return cls(id=link.id, source=serialize_mention(link.source), target=serialize_mention(link.target))


_AnyLinkModel = NodeLinkModel[MentionModel, MentionModel]

_fields = {nlt.value: (Tuple[_AnyLinkModel, ...], None) for nlt in NodeLinkType}
del _fields[NodeLinkType.child]

NodeLinksModel = create_model('NodeLinksModel', **_fields)
