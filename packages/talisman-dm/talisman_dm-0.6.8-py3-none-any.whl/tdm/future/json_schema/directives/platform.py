from tdm.future.datamodel.directives import CreatePlatformDirective, DirectiveType
from .abstract import AbstractDirectiveModel


class CreatePlatformDirectiveModel(AbstractDirectiveModel):
    key: str
    name: str
    platform_type: str
    url: str

    def directive(self, type_: DirectiveType) -> CreatePlatformDirective:
        return CreatePlatformDirective(self.key, self.name, self.platform_type, self.url, id_=self.id)

    @classmethod
    def model(cls, directive: CreatePlatformDirective) -> 'CreatePlatformDirectiveModel':
        cls(id=directive.id, key=directive.key, name=directive.name, platform_type=directive.platform_type, url=directive.url)
