import uuid
from enum import Enum
from typing import Generic, Optional, TypeVar

from tdm.future.datamodel.mention import AbstractNodeMention


class NodeLinkType(str, Enum):
    child = "child"
    same = "same"
    translation = "translation"
    reference = "reference"


_ST = TypeVar('_ST', bound=AbstractNodeMention)
_TT = TypeVar('_TT', bound=AbstractNodeMention)


class AbstractNodeLink(Generic[_ST, _TT]):
    __slots__ = ('_id', '_type', '_source', '_target')

    def __init__(self, type_: NodeLinkType, source: _ST, target: _TT, *, id_: Optional[str]):
        self._id = id_ or self.generate_id()
        self._type = type_
        self._source = source
        self._target = target

    @property
    def id(self) -> str:
        return self._id

    @property
    def type(self) -> NodeLinkType:
        return self._type

    @property
    def source(self) -> _ST:
        return self._source

    @property
    def target(self) -> _TT:
        return self._target

    def __hash__(self) -> int:
        return hash((self._id, self._type, self._source, self._type))

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, AbstractNodeLink):
            return NotImplemented
        return self._id == o._id and self._type == o._type and self._source == o._source and self._target == o._target

    @staticmethod
    def generate_id():
        return str(uuid.uuid4())
