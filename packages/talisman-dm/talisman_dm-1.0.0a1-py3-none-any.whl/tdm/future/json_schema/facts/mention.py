from typing import Dict

from tdm.future.datamodel.facts import AbstractFact, AtomValueFact, FactType, MentionFact
from tdm.future.datamodel.nodes import AbstractNode
from tdm.future.json_schema.mention import MentionModel, serialize_mention
from .abstract import AbstractFactModel


class MentionFactModel(AbstractFactModel):
    mention: MentionModel
    value: str

    def fact(self, fact_type: FactType, facts: Dict[str, AbstractFact], nodes: Dict[str, AbstractNode]) -> MentionFact:
        if fact_type is not FactType.MENTION:
            raise ValueError
        value = facts[self.value]
        if not isinstance(value, AtomValueFact):
            raise ValueError
        return MentionFact(self.status, self.mention.mention(nodes), value, id_=self.id)

    @classmethod
    def model(cls, fact: MentionFact) -> 'MentionFactModel':
        return cls(id=fact.id, status=fact.status, mention=serialize_mention(fact.mention), value=fact.value.id)
