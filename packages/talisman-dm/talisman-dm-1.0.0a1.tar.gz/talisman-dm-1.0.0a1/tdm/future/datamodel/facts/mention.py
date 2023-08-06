from typing import Optional

from tdm.future.datamodel.mention import AbstractNodeMention
from .abstract import AbstractFact, FactStatus, FactType
from .value import AtomValueFact


class MentionFact(AbstractFact):
    __slots__ = ('_mention', '_value')

    def __init__(self, status: FactStatus, mention: AbstractNodeMention, value: AtomValueFact, *, id_: Optional[str] = None):
        super().__init__(FactType.MENTION, status, id_=id_)
        self._mention = mention
        self._value = value

    @property
    def mention(self) -> AbstractNodeMention:
        return self._mention

    @property
    def value(self) -> AtomValueFact:
        return self._value

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, MentionFact):
            return NotImplemented
        return self._id == o._id and self._status == o._status and self._mention == o._mention and self._value == o._value
