from abc import abstractmethod
from typing import Dict

from pydantic import BaseModel, Extra

from tdm.future.datamodel.facts import AbstractFact, FactStatus, FactType
from tdm.future.datamodel.nodes import AbstractNode


class AbstractFactModel(BaseModel):
    class Config:
        extra = Extra.forbid

    id: str
    status: FactStatus

    @abstractmethod
    def fact(self, fact_type: FactType, facts: Dict[str, AbstractFact], nodes: Dict[str, AbstractNode]) -> AbstractFact:
        pass

    @classmethod
    @abstractmethod
    def model(cls, fact: AbstractFact) -> 'AbstractFactModel':
        pass
