from abc import abstractmethod

from pydantic import BaseModel

from tdm.future.datamodel.directives import AbstractDirective, DirectiveType


class AbstractDirectiveModel(BaseModel):
    id: str

    @abstractmethod
    def directive(self, type_: DirectiveType) -> AbstractDirective:
        pass

    @classmethod
    @abstractmethod
    def model(cls, directive: AbstractDirective) -> 'AbstractDirectiveModel':
        pass
