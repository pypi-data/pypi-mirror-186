import uuid
from abc import ABCMeta
from enum import Enum
from functools import total_ordering
from typing import Generic, Optional, TypeVar


@total_ordering
class FactStatus(str, Enum):
    def __new__(cls, name: str, priority: int):
        obj = str.__new__(cls, name)
        obj._value_ = name
        obj.priority = priority
        return obj

    APPROVED = ("approved", 0)
    DECLINED = ("declined", 1)
    AUTO = ("auto", 2)
    HIDDEN = ("hidden", 3)
    NEW = ("new", 4)

    def __lt__(self, other: 'FactStatus'):
        if not isinstance(other, FactStatus):
            return NotImplemented
        return self.priority < other.priority


class FactType(str, Enum):
    MENTION = "mention"
    ATOM_VALUE = "atom"
    COMPOSITE_VALUE = "composite"

    SLOT = "slot"
    RELATION = "relation"
    PROPERTY = "property"
    R_PROPERTY = "r_property"

    CONCEPT = "concept"


class AbstractFact(metaclass=ABCMeta):
    __slots__ = ('_id', '_type', '_status')

    def __init__(self, type_: FactType, status: FactStatus, *, id_: Optional[str]):
        self._id = id_ or self.generate_id()
        self._type = type_
        self._status = status

    @property
    def id(self) -> str:
        return self._id

    @property
    def type(self) -> FactType:
        return self._type

    @property
    def status(self) -> FactStatus:
        return self._status

    @staticmethod
    def generate_id() -> str:
        return str(uuid.uuid4())

    def __hash__(self) -> int:
        return hash((self._id, self._type, self._status))


_ST = TypeVar('_ST', bound=AbstractFact)
_TT = TypeVar('_TT', bound=AbstractFact)


class AbstractLinkFact(AbstractFact, Generic[_ST, _TT]):
    __slots__ = ('_type_id', '_source', '_target', '_value')

    def __init__(self, type_: FactType, status: FactStatus, type_id: str, source: _ST, target: _TT, value: Optional[str] = None,
                 *, id_: Optional[str] = None):
        super().__init__(type_, status, id_=id_)
        self._type_id = type_id
        self._source = source
        self._target = target
        self._value = value

    @property
    def type_id(self) -> str:
        return self._type_id

    @property
    def source(self) -> _ST:
        return self._source

    @property
    def target(self) -> _TT:
        return self._target

    @property
    def value(self) -> Optional[str]:
        return self._value

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, AbstractLinkFact):
            return NotImplemented
        return self._id == o._id and self._type == o._type and self._status == o._status and self._type_id == o._type_id \
            and self._source == o._source and self._target == o._target and self._value == o._value
