from typing import Iterable, Optional, Tuple, Union

from .abstract import AbstractFact, FactStatus, FactType


class AtomValueFact(AbstractFact):
    __slots__ = ('_type_id', '_value')

    def __init__(self, status: FactStatus, type_id: str, value: Union[dict, Iterable[dict]], *, id_: Optional[str] = None):
        super().__init__(FactType.ATOM_VALUE, status, id_=id_)
        self._type_id = type_id
        self._value = dict(value) if isinstance(value, dict) else tuple(dict(v) for v in value)  # here shallow copy for now

    @property
    def type_id(self) -> str:
        return self._type_id

    @property
    def value(self) -> Union[dict, Tuple[dict, ...]]:
        return self._value

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, AtomValueFact):
            return NotImplemented
        return self._id == o._id and self._status == o._status and self._type_id == o._type_id and self._value == o._value


class CompositeValueFact(AbstractFact):
    __slots__ = ('_type_id',)

    def __init__(self, status: FactStatus, type_id: str, *, id_: Optional[str] = None):
        super().__init__(FactType.COMPOSITE_VALUE, status, id_=id_)
        self._type_id = type_id

    @property
    def type_id(self) -> str:
        return self._type_id

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, CompositeValueFact):
            return NotImplemented
        return self._id == o._id and self._status == o._status and self._type_id == o._type_id
