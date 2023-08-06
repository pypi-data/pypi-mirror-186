from typing import Callable, Dict, ForwardRef, Generic, Iterable, Optional, Tuple, Type, TypeVar, Union

from frozendict import frozendict
from pydantic import root_validator
from pydantic.generics import GenericModel
from typing_extensions import Literal

from tdm.future.datamodel.nodes import AbstractContentNode, AbstractNode, NodeType, NodeTypes
from tdm.future.datamodel.nodes.abstract import BaseNodeMetadata
from tdm.future.json_schema.nodes.metadata import AbstractNodeMetadataModel, create_metadata_model

_NT = TypeVar('_NT', bound=NodeType)
_MM = TypeVar('_MM', bound=AbstractNodeMetadataModel)

NodeModel_ = ForwardRef('NodeModel_')


class NodeModel(GenericModel, Generic[_NT, _MM]):
    id: str
    type: _NT
    metadata: _MM
    children: Optional[Tuple['NodeModel_', ...]] = ()

    @classmethod
    def node_type(cls) -> NodeType:
        return cls.__fields__['type'].type_.__args__[0]  # here we assume _NT is Literal[...]

    @root_validator(pre=True)
    def _set_type_runtime(cls, values):  # noqa: N805
        values['type'] = cls.node_type()
        return values

    def node(self) -> AbstractNode:
        return NodeTypes[self.type](self.metadata.metadata(), id_=self.id)

    @classmethod
    def model(cls, node: AbstractNode) -> 'NodeModel':
        return cls.construct(id=node.id, type=node.node_type(), metadata=cls._convert_metadata(node.metadata))

    @classmethod
    def _convert_metadata(cls, metadata: BaseNodeMetadata) -> AbstractNodeMetadataModel:
        metadata_factory = cls.__fields__['metadata'].type_.model
        return metadata_factory(metadata)


class ContentNodeModel(NodeModel[_NT, _MM], Generic[_NT, _MM]):
    content: str

    def node(self) -> AbstractContentNode:
        return NodeTypes[self.type](self.content, self.metadata.metadata(), id_=self.id)

    @classmethod
    def model(cls, node: AbstractContentNode) -> 'ContentNodeModel':
        return cls.construct(id=node.id, type=node.node_type(), metadata=cls._convert_metadata(node.metadata), content=node.content)


def create_model_for_node(node_type: Type[AbstractNode]) -> Type[NodeModel]:
    mt = create_metadata_model(node_type.__orig_bases__[0].__args__[0], node_type)
    nt = node_type.node_type()
    result = (ContentNodeModel if issubclass(node_type, AbstractContentNode) else NodeModel)[Literal[nt], mt]
    return result


def update_forward_refs(model_types: Iterable[Type[NodeModel]]) -> Tuple[Type, Dict[NodeType, Type[NodeModel]]]:
    global NodeModel_
    result: Dict[NodeType, Type[NodeModel]] = {}
    for model_type in model_types:
        result[model_type.node_type()] = model_type
    NodeModel_ = Union[tuple(result.values())]
    for model_type in result.values():
        model_type.update_forward_refs()
    return NodeModel_, frozendict(result)


def serialize_node_factory(type2model: Dict[NodeType, Type[NodeModel]]) -> Callable[[AbstractNode], NodeModel]:
    def serialize_node(node: AbstractNode) -> NodeModel:
        return type2model[node.node_type()].model(node)

    return serialize_node
