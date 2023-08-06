from typing import Dict, Optional, Tuple, Union

from tdm.future.datamodel.facts import AbstractFact, ConceptFact, FactType
from tdm.future.datamodel.nodes import AbstractNode
from .abstract import AbstractFactModel


class ConceptFactModel(AbstractFactModel):
    type_id: str
    value: Optional[Union[str, Tuple[str, ...]]]

    def fact(self, fact_type: FactType, facts: Dict[str, AbstractFact], nodes: Dict[str, AbstractNode]) -> ConceptFact:
        if fact_type is not FactType.CONCEPT:
            raise ValueError(f"concept fact model contains '{fact_type}' type instead of '{FactType.CONCEPT}'")
        return ConceptFact(self.status, self.type_id, self.value, id_=self.id)

    @classmethod
    def model(cls, fact: ConceptFact) -> 'ConceptFactModel':
        return cls(id=fact.id, status=fact.status, type_id=fact.type_id, value=fact.value)
