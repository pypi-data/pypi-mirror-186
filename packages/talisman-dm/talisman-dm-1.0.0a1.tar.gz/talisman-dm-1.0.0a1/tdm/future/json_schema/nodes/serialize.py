from typing import Dict, Iterable, Tuple

from tdm.future.datamodel.links import ChildNodeLink
from .abstract import NodeModel


def construct_tree(id2node_model: Dict[str, NodeModel], links: Iterable[ChildNodeLink]) -> Tuple[NodeModel, ...]:
    roots = set(id2node_model)
    for link in links:
        roots.remove(link.target.node_id)
        children = id2node_model[link.source.node_id].children or tuple()
        id2node_model[link.source.node_id].children = (*children, id2node_model[link.target.node_id])
    return tuple(id2node_model.get(i) for i in roots)
