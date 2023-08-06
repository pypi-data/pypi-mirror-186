from typing import Dict, Optional, Tuple, Union

from tdm.future.datamodel.facts import AbstractFact, AtomValueFact, CompositeValueFact, FactType
from tdm.future.datamodel.nodes import AbstractNode
from .abstract import AbstractFactModel


class AtomValueFactModel(AbstractFactModel):
    type_id: str
    value: Optional[Union[dict, Tuple[dict, ...]]]

    def fact(self, fact_type: FactType, facts: Dict[str, AbstractFact], nodes: Dict[str, AbstractNode]) -> AtomValueFact:
        return AtomValueFact(self.status, self.type_id, self.value, id_=self.id)

    @classmethod
    def model(cls, fact: AtomValueFact) -> 'AtomValueFactModel':
        return cls(id=fact.id, status=fact.status, type_id=fact.type_id, value=fact.value)


class CompositeValueFactModel(AbstractFactModel):
    type_id: str

    def fact(self, fact_type: FactType, facts: Dict[str, AbstractFact], nodes: Dict[str, AbstractNode]) -> CompositeValueFact:
        return CompositeValueFact(self.status, self.type_id, id_=self.id)

    @classmethod
    def model(cls, fact: CompositeValueFact) -> 'CompositeValueFactModel':
        return cls(id=fact.id, status=fact.status, type_id=fact.type_id)
