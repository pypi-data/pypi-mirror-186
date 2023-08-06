__all__ = [
    'AbstractFact', 'AbstractLinkFact', 'FactStatus', 'FactType',
    'ConceptFact',
    'PropertyFact', 'RelationFact', 'RelationPropertyFact', 'SlotFact',
    'MentionFact',
    'AtomValueFact', 'CompositeValueFact',
    'FACT_TYPES'
]

from .abstract import AbstractFact, AbstractLinkFact, FactStatus, FactType
from .concept import ConceptFact
from .links import PropertyFact, RelationFact, RelationPropertyFact, SlotFact
from .mention import MentionFact
from .value import AtomValueFact, CompositeValueFact

FACT_TYPES = {
    FactType.MENTION: MentionFact,
    FactType.ATOM_VALUE: AtomValueFact,
    FactType.COMPOSITE_VALUE: CompositeValueFact,
    FactType.SLOT: SlotFact,
    FactType.RELATION: RelationFact,
    FactType.PROPERTY: PropertyFact,
    FactType.R_PROPERTY: RelationPropertyFact,
    FactType.CONCEPT: ConceptFact
}
