from typing import Tuple

from pydantic import create_model

from tdm.future.datamodel.facts import AbstractFact, FactType
from .abstract import AbstractFactModel
from .concept import ConceptFactModel
from .links import LinkFactModel
from .mention import MentionFactModel
from .value import AtomValueFactModel, CompositeValueFactModel


def serialize_fact(fact: AbstractFact) -> AbstractFactModel:
    return _TYPE2MODEL[fact.type].model(fact)


_TYPE2MODEL = {
    FactType.CONCEPT: ConceptFactModel,
    FactType.ATOM_VALUE: AtomValueFactModel,
    FactType.COMPOSITE_VALUE: CompositeValueFactModel,

    FactType.MENTION: MentionFactModel,

    FactType.RELATION: LinkFactModel,
    FactType.PROPERTY: LinkFactModel,
    FactType.R_PROPERTY: LinkFactModel,
    FactType.SLOT: LinkFactModel
}

_fields = {t.value: (Tuple[v, ...], None) for t, v in _TYPE2MODEL.items()}

FactsModel = create_model('FactsModel', **_fields)

FACTS_DESERIALIZATION_ORDER = (
    FactType.CONCEPT, FactType.RELATION,
    FactType.ATOM_VALUE, FactType.COMPOSITE_VALUE, FactType.SLOT,
    FactType.MENTION, FactType.PROPERTY, FactType.R_PROPERTY
)
