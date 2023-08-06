__all__ = [
    'AbstractNodeMentionModel', 'MentionModel',
    'NodeMentionModel', 'ImageNodeMentionModel', 'TextNodeMentionModel',
    'serialize_mention'
]

from typing import Union

from tdm.future.datamodel.mention import ImageNodeMention, NodeMention, TextNodeMention
from .abstract import AbstractNodeMentionModel, create_mention_model
from .serialize import serialize_mention_factory

NodeMentionModel = create_mention_model(NodeMention)
ImageNodeMentionModel = create_mention_model(ImageNodeMention)
TextNodeMentionModel = create_mention_model(TextNodeMention)

_mention_models = (
    NodeMentionModel,
    ImageNodeMentionModel,
    TextNodeMentionModel
)

MentionModel = Union[_mention_models]

serialize_mention = serialize_mention_factory({
    mt.get_type(): mt for mt in _mention_models
})
