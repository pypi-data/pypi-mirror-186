from typing import Tuple

from pydantic import create_model

from tdm.future.datamodel.directives import AbstractDirective, DirectiveType
from .abstract import AbstractDirectiveModel
from .account import CreateAccountDirectiveModel
from .concept import CreateConceptDirectiveModel
from .platform import CreatePlatformDirectiveModel


def serialize_directive(directive: AbstractDirective) -> AbstractDirectiveModel:
    return _TYPE2MODEL[directive.directive_type].model(directive)


_TYPE2MODEL = {
    DirectiveType.CREATE_ACCOUNT: CreateAccountDirectiveModel,
    DirectiveType.CREATE_PLATFORM: CreatePlatformDirectiveModel,

    DirectiveType.CREATE_CONCEPT: CreateConceptDirectiveModel
}

_fields = {t.value: (Tuple[v, ...], None) for t, v in _TYPE2MODEL.items()}

DirectivesModel = create_model('DirectivesModel', **_fields)
