from typing import List


class MissingPermissionException(Exception):
    pass


class MissingScopeConfiguration(Exception):
    pass


class WrongScopesConfigurationMissingDependency(Exception):
    scope: str
    parent_scopes: List

    def __init__(self, scope: str, parent_scopes: List) -> None:
        super().__init__()
        self.scope = scope
        self.parent_scopes = parent_scopes


class WrongScopesConfigurationHiddenScope(Exception):
    scope: str

    def __init__(self, scope: str) -> None:
        super().__init__()
        self.scope = scope


class WrongScopesConfigurationScopeNotFound(Exception):
    scope: str

    def __init__(self, scope: str) -> None:
        super().__init__()
        self.scope = scope
