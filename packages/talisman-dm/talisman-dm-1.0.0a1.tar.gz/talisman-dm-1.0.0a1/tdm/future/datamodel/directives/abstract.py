import uuid
from abc import ABCMeta
from enum import Enum
from typing import Optional


class DirectiveType(str, Enum):
    CREATE_CONCEPT = 'create_concept'
    CREATE_ACCOUNT = 'create_account'
    CREATE_PLATFORM = 'create_platform'


class AbstractDirective(metaclass=ABCMeta):
    __slots__ = ('_directive_type', '_id')

    def __init__(self, directive_type: DirectiveType, *, id_: Optional[str] = None):
        self._id = id_ or self.generate_id()
        self._directive_type = directive_type

    @property
    def id(self):
        return self._id

    @property
    def directive_type(self) -> DirectiveType:
        return self._directive_type

    def __hash__(self) -> int:
        return hash(self._directive_type)

    @staticmethod
    def generate_id() -> str:
        return str(uuid.uuid4())
