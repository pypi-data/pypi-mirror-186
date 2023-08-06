from dataclasses import asdict, fields
from typing import Any, Dict, Generic, Optional, Type, TypeVar

from pydantic import Extra, Field, create_model
from pydantic.generics import GenericModel

from tdm.future.datamodel.nodes import AbstractNode
from tdm.future.datamodel.nodes.abstract import BaseNodeMetadata

_NM = TypeVar('_NM', bound=BaseNodeMetadata)


class AbstractNodeMetadataModel(GenericModel, Generic[_NM]):
    class Config:
        extra = Extra.allow

        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type['AbstractNodeMetadataModel']) -> None:
            # remove special field from json schema
            schema['properties'].pop('type')

    # this is special field to get runtime type info. This field is excluded both from json/dict and from json_schema
    type: Type[_NM] = Field(None, exclude=True)

    def metadata(self) -> _NM:
        return self.__fields__['type'].type_.__args__[0](**self.dict())

    @classmethod
    def model(cls, metadata: _NM):
        return cls(**asdict(metadata))


def create_metadata_model(type_: Type[BaseNodeMetadata], node_type: Optional[Type[AbstractNode]]) -> Type[AbstractNodeMetadataModel]:
    # we should use node type class name to avoid pydantic class names collision (no json schema will be generated in that case)
    model_name = f"{node_type.__name__}MetadataModel" if node_type else f"{type_.__name__}Model"
    model_fields = {
        field.name: (field.type, field.default) for field in fields(type_)
    }
    model = create_model(model_name, __base__=AbstractNodeMetadataModel[type_], **model_fields)
    return model
