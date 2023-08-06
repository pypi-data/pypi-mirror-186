from typing import Optional, Tuple

from frozendict import frozendict

from tdm.future.datamodel.directives import CreateConceptDirective, DirectiveType
from .abstract import AbstractDirectiveModel


class CreateConceptDirectiveModel(AbstractDirectiveModel):
    name: str
    concept_type: str
    filters: Tuple[dict, ...]
    notes: Optional[str]
    markers: Optional[Tuple[str, ...]]
    access_level: Optional[str]

    def directive(self, type_: DirectiveType) -> CreateConceptDirective:
        filters = tuple(map(frozendict, self.filters))
        return CreateConceptDirective(self.name, self.concept_type, filters, self.notes, self.markers, self.access_level, id_=self.id)

    @classmethod
    def model(cls, directive: CreateConceptDirective) -> 'CreateConceptDirectiveModel':
        return cls(
            id=directive.id,
            name=directive.name,
            concept_type=directive.concept_type,
            filters=directive.filters,
            notes=directive.notes,
            markers=directive.markers,
            access_level=directive.access_level
        )
