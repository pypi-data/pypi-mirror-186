from typing import Dict, Iterable, Optional, Set, Tuple

from pydantic import BaseModel

from tdm.future.datamodel.document import TalismanDocument
from tdm.future.datamodel.facts import AbstractFact
from tdm.future.datamodel.links import AbstractNodeLink, ChildNodeLink, NODE_LINK_TYPES, NodeLinkType
from tdm.future.datamodel.mention import NodeMention
from tdm.future.datamodel.nodes import AbstractNode
from tdm.json_schema import DocumentMetadataModel
from .directives import DirectivesModel, serialize_directive
from .facts import FACTS_DESERIALIZATION_ORDER, FactsModel, serialize_fact
from .links import NodeLinkModel, NodeLinksModel
from .nodes import NodeModel, construct_tree, serialize_node


class TalismanDocumentModel(BaseModel):
    id: str
    main_node: str
    content: Tuple[NodeModel, ...]
    links: NodeLinksModel
    facts: FactsModel
    directives: DirectivesModel

    metadata: Optional[DocumentMetadataModel]  # should be removed in future

    def document(self) -> TalismanDocument:
        links: Set[AbstractNodeLink]
        id2node, links = self._collect_nodes()
        for nlt, link_models in self.links.__dict__.items():
            if not link_models:
                continue
            links.update(link_model.link(NODE_LINK_TYPES[nlt], id2node) for link_model in link_models)
        id2fact: Dict[str, AbstractFact] = {}
        for fact_type in FACTS_DESERIALIZATION_ORDER:
            id2fact.update(
                {fact.id: fact for fact in map(lambda fm: fm.fact(fact_type, id2fact, id2node), getattr(self.facts, fact_type) or tuple())}
            )
        directives = set()
        for dt, directive_models in self.directives.__dict__.items():
            if not directive_models:
                continue
            directives.update(directive_model.directive(dt) for directive_model in directive_models)

        return TalismanDocument(
            content=id2node.values(),
            root=id2node[self.main_node],
            links=links,
            facts=id2fact.values(),
            directives=directives,
            metadata=self.metadata.to_metadata() if self.metadata is not None else None,
            id_=self.id
        )

    def _collect_nodes(self) -> Tuple[Dict[str, AbstractNode], Set[ChildNodeLink]]:
        # try to avoid recursion
        parent = {}
        id2node = {}

        to_be_processed = list(self.content)

        for node_model in to_be_processed:
            id2node[node_model.id] = node_model.node()
            for child in node_model.children:
                parent[child.id] = node_model.id
            to_be_processed.extend(node_model.children)
        links = set()
        for child_id, parent_id in parent.items():
            links.add(ChildNodeLink(source=NodeMention(id2node[parent_id]), target=NodeMention(id2node[child_id])))

        return id2node, links

    @classmethod
    def model(cls, document: TalismanDocument) -> 'TalismanDocumentModel':
        id2node_models = {id_: serialize_node(node) for id_, node in document.content.items()}
        links = dict(document.links)
        children_links: Iterable[ChildNodeLink] = links.pop(NodeLinkType.child)
        return cls.construct(
            id=document.id,
            main_node=document.root.id,
            content=construct_tree(id2node_models, children_links),
            links=NodeLinksModel(**{lt: tuple(map(NodeLinkModel.model, links)) for lt, links in links.items()}),
            facts=FactsModel(**{ft: tuple(map(serialize_fact, facts)) for ft, facts in document.facts.items()}),
            directives=DirectivesModel(**{dt: tuple(map(serialize_directive, d)) for dt, d in document.directives.items()}),
            metadata=DocumentMetadataModel(**document._metadata) if document._metadata is not None else None
        )
