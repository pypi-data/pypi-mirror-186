from typing import Dict, Optional

from tdm.future.datamodel.facts import AbstractFact, AbstractLinkFact, FACT_TYPES, FactType
from tdm.future.datamodel.nodes import AbstractNode
from .abstract import AbstractFactModel


class LinkFactModel(AbstractFactModel):
    type_id: str
    source: str
    target: str
    value: Optional[str]

    def fact(self, fact_type: FactType, facts: Dict[str, AbstractFact], nodes: Dict[str, AbstractNode]) -> AbstractLinkFact:
        # TODO: add fact_type validation
        return FACT_TYPES[fact_type](self.status, self.type_id, facts[self.source], facts[self.target], self.value, id_=self.id)

    @classmethod
    def model(cls, fact: AbstractLinkFact) -> 'LinkFactModel':
        return cls(id=fact.id, status=fact.status, type_id=fact.type_id, source=fact.source.id, target=fact.target.id, value=fact.value)
