from typing import Iterable, Optional, Tuple, Union

from .abstract import AbstractFact, FactStatus, FactType


class ConceptFact(AbstractFact):
    __slots__ = ('_type_id', '_value')

    def __init__(self, status: FactStatus, type_id: str, value: Union[str, Iterable[str]], *, id_: Optional[str] = None):
        super().__init__(FactType.CONCEPT, status, id_=id_)
        self._type_id = type_id
        self._value = value if isinstance(value, str) else tuple(value)

    @property
    def type_id(self) -> str:
        return self._type_id

    @property
    def value(self) -> Union[str, Tuple[str, ...]]:
        return self._value

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ConceptFact):
            return not NotImplemented
        return self._id == o._id and self._status == o._status and self._type_id == o._type_id and self._value == o._value
