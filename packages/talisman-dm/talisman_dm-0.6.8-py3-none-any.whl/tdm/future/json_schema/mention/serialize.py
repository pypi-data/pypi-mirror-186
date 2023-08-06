from typing import Callable, Dict, Type

from tdm.future.datamodel.mention import AbstractNodeMention
from .abstract import AbstractNodeMentionModel


def serialize_mention_factory(type2model: Dict[Type[AbstractNodeMention], Type[AbstractNodeMentionModel]]) \
        -> Callable[[AbstractNodeMention], AbstractNodeMentionModel]:
    def serialize_mention(mention: AbstractNodeMention) -> AbstractNodeMentionModel:
        return type2model[type(mention)].model(mention)

    return serialize_mention
