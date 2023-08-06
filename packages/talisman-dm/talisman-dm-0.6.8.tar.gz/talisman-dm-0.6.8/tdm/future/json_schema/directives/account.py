from tdm.future.datamodel.directives import CreateAccountDirective, DirectiveType
from .abstract import AbstractDirectiveModel


class CreateAccountDirectiveModel(AbstractDirectiveModel):
    key: str
    platform: str
    name: str
    url: str

    def directive(self, type_: DirectiveType) -> CreateAccountDirective:
        return CreateAccountDirective(self.key, self.platform, self.name, self.url, id_=self.id)

    @classmethod
    def model(cls, directive: CreateAccountDirective) -> 'CreateAccountDirectiveModel':
        return cls(id=directive.id, key=directive.key, platform=directive.platform_key, name=directive.name, url=directive.url)
