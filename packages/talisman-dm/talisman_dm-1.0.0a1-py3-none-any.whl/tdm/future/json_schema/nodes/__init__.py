__all__ = [
    'NodeModel', 'serialize_node', 'construct_tree'
]

from tdm.future.datamodel.nodes import NodeTypes
from .abstract import create_model_for_node, serialize_node_factory, update_forward_refs
from .serialize import construct_tree

NodeModel, type2model = update_forward_refs([
    create_model_for_node(node_type) for node_type in NodeTypes.values()
])

serialize_node = serialize_node_factory(type2model)
