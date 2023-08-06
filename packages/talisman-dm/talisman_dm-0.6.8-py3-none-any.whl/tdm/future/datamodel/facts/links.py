from typing import Optional, Union

from .abstract import AbstractLinkFact, FactStatus, FactType
from .concept import ConceptFact
from .value import AtomValueFact, CompositeValueFact


class RelationFact(AbstractLinkFact[ConceptFact, ConceptFact]):
    def __init__(self, status: FactStatus, type_id: str, source: ConceptFact, target: ConceptFact, value: Optional[str] = None,
                 *, id_: Optional[str] = None):
        super().__init__(FactType.RELATION, status, type_id, source, target, value, id_=id_)


ValueFact = Union[AtomValueFact, CompositeValueFact]


class PropertyFact(AbstractLinkFact[ConceptFact, ValueFact]):
    def __init__(self, status: FactStatus, type_id: str, source: ConceptFact, target: ValueFact, value: Optional[str] = None,
                 *, id_: Optional[str] = None):
        super().__init__(FactType.PROPERTY, status, type_id, source, target, value, id_=id_)


class RelationPropertyFact(AbstractLinkFact[RelationFact, ValueFact]):
    def __init__(self, status: FactStatus, type_id: str, source: RelationFact, target: ValueFact, value: Optional[str] = None,
                 *, id_: Optional[str] = None):
        super().__init__(FactType.R_PROPERTY, status, type_id, source, target, value, id_=id_)


class SlotFact(AbstractLinkFact[CompositeValueFact, ValueFact]):
    def __init__(self, status: FactStatus, type_id: str, source: CompositeValueFact, target: ValueFact, value: Optional[str] = None,
                 *, id_: Optional[str] = None):
        super().__init__(FactType.SLOT, status, type_id, source, target, value, id_=id_)
