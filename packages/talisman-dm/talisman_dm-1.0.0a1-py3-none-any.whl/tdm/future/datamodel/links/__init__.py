__all__ = [
    'AbstractNodeLink', 'NodeLinkType',
    'ChildNodeLink',
    'ReferenceNodeLink', 'SameNodeLink', 'TranslationNodeLink',
    'NODE_LINK_TYPES'
]

from .abstract import AbstractNodeLink, NodeLinkType
from .child import ChildNodeLink
from .reference import ReferenceNodeLink, SameNodeLink, TranslationNodeLink

NODE_LINK_TYPES = {
    NodeLinkType.same: SameNodeLink,
    NodeLinkType.reference: ReferenceNodeLink,
    NodeLinkType.translation: TranslationNodeLink
}
