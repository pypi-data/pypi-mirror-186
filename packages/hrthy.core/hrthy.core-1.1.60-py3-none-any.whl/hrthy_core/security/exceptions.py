class MissingPermissionException(Exception):
    pass


class MissingScopeConfiguration(Exception):
    pass


class WrongScopesConfigurationMissingDependency(Exception):
    scope: str
    parent_scopes: dict

    def __init__(self, scope: str, parent_scopes: dict) -> None:
        super().__init__()
        self.scope = scope
        self.parent_scopes = parent_scopes

    def get_parent_scopes(self):
        return self._get_readable_parent_scopes(parent_scopes=self.parent_scopes)

    def _get_readable_parent_scopes(self, parent_scopes: dict):
        text = '('
        for condition_type, conditions in parent_scopes.items():
            subtexts = []
            for condition in conditions:
                if isinstance(condition, dict):
                    subtexts.append(self._get_readable_parent_scopes(condition))
                else:
                    subtexts.append(condition)
            condition_type_text = ' ' + condition_type + ' '
            text += condition_type_text.join(subtexts)
        text += ')'
        return text


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
