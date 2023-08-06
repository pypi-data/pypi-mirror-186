from typing import List

from hrthy_core.security.constants import DEFAULT_SCOPES
from hrthy_core.security.exceptions import (
    WrongScopesConfigurationHiddenScope, WrongScopesConfigurationMissingDependency,
    WrongScopesConfigurationScopeNotFound,
)
from hrthy_core.security.scopes_hierarchy import HIERARCHY_SCOPES
from hrthy_core.security.types import ConditionType


class ScopesConfiguration:
    scopes: List[str] = []

    def __init__(self, scopes: List[str], current_scopes: List[str]):
        super().__init__()
        self.scopes = ScopesConfiguration._check_configuration_permission(scopes, current_scopes)
        self.scopes = ScopesConfiguration._add_default_scopes(self.scopes)

    @classmethod
    def _check_configuration_permission(cls, scopes: List[str], current_scopes: List[str]) -> List[str]:
        for scope in scopes:
            if scope not in HIERARCHY_SCOPES.keys():
                raise WrongScopesConfigurationScopeNotFound(scope)
            scope_to_check = HIERARCHY_SCOPES.get(scope.strip().lower())
            # Check visibility. If false, this scope cannot be assigned
            if scope_to_check['visible'] is False:
                raise WrongScopesConfigurationHiddenScope(scope)
            # If not true, we need to check if the scopes defined are already assigned
            if scope_to_check['visible'] is not True:
                for visible_scope in scope_to_check['visible']:
                    # If the scope is not in the list of my scopes already assigned, return false
                    if visible_scope not in current_scopes:
                        raise WrongScopesConfigurationHiddenScope(scope)

            # If not true, we need to check if the scopes defined are already assigned
            if scope_to_check['depends']:
                evaluation = ScopesConfiguration._check_dependent_scopes(scope_to_check['depends'], scopes)
                if evaluation is False:
                    raise WrongScopesConfigurationMissingDependency(scope, scope_to_check['depends'])
        return scopes

    @classmethod
    def _check_dependent_scopes(cls, dependent_scopes: dict, scopes) -> bool:
        evaluations = []
        for condition_type, conditions in dependent_scopes.items():
            for condition in conditions:
                if isinstance(condition, dict):
                    evaluations.append(ScopesConfiguration._check_dependent_scopes(condition, scopes))
                else:
                    evaluations.append(condition in scopes)
            return any(evaluations) if condition_type == ConditionType.OR else all(evaluations)

    @classmethod
    def _add_default_scopes(cls, scopes: List[str]) -> List[str]:
        return list(set(scopes + DEFAULT_SCOPES))
