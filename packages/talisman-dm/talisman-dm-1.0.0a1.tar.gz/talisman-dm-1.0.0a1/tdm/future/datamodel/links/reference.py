from typing import Optional, TypeVar

from tdm.future.datamodel.mention import AbstractNodeMention
from .abstract import AbstractNodeLink, NodeLinkType

_ST = TypeVar('_ST', bound=AbstractNodeMention)
_TT = TypeVar('_TT', bound=AbstractNodeMention)


class SameNodeLink(AbstractNodeLink[_ST, _TT]):
    def __init__(self, source: _ST, target: _TT, *, id_: Optional[str] = None):
        super().__init__(NodeLinkType.same, source, target, id_=id_)


class TranslationNodeLink(AbstractNodeLink[_ST, _TT]):
    def __init__(self, source: _ST, target: _TT, *, id_: Optional[str] = None):
        super().__init__(NodeLinkType.translation, source, target, id_=id_)


class ReferenceNodeLink(AbstractNodeLink[_ST, _TT]):
    def __init__(self, source: _ST, target: _TT, *, id_: Optional[str] = None):
        super().__init__(NodeLinkType.translation, source, target, id_=id_)
