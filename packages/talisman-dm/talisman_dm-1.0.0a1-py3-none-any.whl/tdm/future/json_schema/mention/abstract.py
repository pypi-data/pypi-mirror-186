import dataclasses
from dataclasses import asdict, fields
from typing import Any, Dict, Generic, Type, TypeVar

from pydantic import Extra, Field, create_model
from pydantic.generics import GenericModel

from tdm.future.datamodel.mention import AbstractNodeMention
from tdm.future.datamodel.nodes import AbstractNode

_NM = TypeVar('_NM', bound=AbstractNodeMention)


class AbstractNodeMentionModel(GenericModel, Generic[_NM]):
    class Config:
        extra = Extra.forbid

        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type['AbstractNodeMentionModel']) -> None:
            # remove special field from json schema
            schema['properties'].pop('type')

    # this is special field to get runtime type info. This field is excluded both from json/dict and from json_schema
    type: Type[_NM] = Field(None, exclude=True)

    node_id: str

    def mention(self, nodes: Dict[str, AbstractNode]) -> _NM:
        params = self.dict()
        params['node'] = nodes[params.pop('node_id')]
        return self.get_type()(**params)

    @classmethod
    def model(cls, mention: _NM) -> 'AbstractNodeMentionModel':
        params = asdict(mention)
        params['node_id'] = params.pop('node').id
        return cls(**params)

    @classmethod
    def get_type(cls) -> Type[_NM]:
        return cls.__fields__['type'].type_.__args__[0]


def create_mention_model(type_: Type[AbstractNodeMention]) -> Type[AbstractNodeMentionModel]:
    model_fields = {
        field.name: (field.type, field.default if field.default is not dataclasses.MISSING else ...) for field in fields(type_)
    }
    model_fields.pop('node')
    model = create_model(f"{type_.__name__}Model", __base__=AbstractNodeMentionModel[type_], **model_fields)
    return model
