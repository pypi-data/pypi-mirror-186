from typing import List, Optional
from uuid import UUID

from hrthy_core.security.exceptions import MissingPermissionException, MissingScopeConfiguration
from hrthy_core.security.scopes_hierarchy import HIERARCHY_SCOPES
from hrthy_core.security.security import Requester, RequesterType
from hrthy_core.security.types import ScopeType


class ScopeChecker:
    @staticmethod
    def is_service_user(requester: Requester) -> bool:
        return requester.requester_type == RequesterType.service

    @staticmethod
    def has_all_permissions(requester: Requester, scopes: List[str]) -> bool:
        return all(s in requester.scopes for s in scopes)

    @staticmethod
    def has_at_least_one_permission(requester: Requester, scopes: List[str]) -> bool:
        return any(s in requester.scopes for s in scopes)

    @staticmethod
    def get_first_match_permission(requester: Requester, scopes: List[str]) -> Optional[str]:
        for s in scopes:
            if s in requester.scopes:
                return s
        return None

    @staticmethod
    def get_target_company(requester: Requester, priority_scopes: List[str], company_id: UUID = None) -> UUID:
        scope = ScopeChecker.get_first_match_permission(requester=requester, scopes=priority_scopes)
        if scope:
            scope_configuration = HIERARCHY_SCOPES.get(scope, None)
            if not scope_configuration:
                raise MissingScopeConfiguration()
            if scope_configuration.get('type') != ScopeType.GLOBAL \
                    and company_id is not None \
                    and company_id != requester.company_id:
                raise MissingPermissionException()
            return company_id if company_id is not None else requester.company_id
        raise MissingPermissionException()

    @staticmethod
    def get_target_user(requester: Requester, priority_scopes: List[str], user_id: UUID) -> UUID:
        for scope in priority_scopes:
            if not ScopeChecker.has_all_permissions(requester=requester, scopes=[scope]):
                continue
            scope_configuration = HIERARCHY_SCOPES.get(scope, None)
            if not scope_configuration:
                raise MissingScopeConfiguration()
            if scope_configuration.get('type') == ScopeType.PERSONAL \
                    and user_id == requester.requester_id:
                return user_id
            if scope_configuration.get('type') != ScopeType.PERSONAL \
                    and user_id != requester.requester_id:
                return user_id
        raise MissingPermissionException()

    @staticmethod
    def get_target_role(requester: Requester, priority_scopes: List[str], role_id: UUID) -> UUID:
        for scope in priority_scopes:
            if not ScopeChecker.has_all_permissions(requester=requester, scopes=[scope]):
                continue
            scope_configuration = HIERARCHY_SCOPES.get(scope, None)
            if not scope_configuration:
                raise MissingScopeConfiguration()
            if scope_configuration.get('type') == ScopeType.PERSONAL \
                    and role_id == requester.role_id:
                return role_id
            if scope_configuration.get('type') != ScopeType.PERSONAL:
                return role_id
        raise MissingPermissionException()

    @staticmethod
    def get_target_candidate(requester: Requester, priority_scopes: List[str], candidate_id: UUID) -> UUID:
        for scope in priority_scopes:
            if not ScopeChecker.has_all_permissions(requester=requester, scopes=[scope]):
                continue
            scope_configuration = HIERARCHY_SCOPES.get(scope, None)
            if not scope_configuration:
                raise MissingScopeConfiguration()
            if scope_configuration.get('type') == ScopeType.PERSONAL \
                    and candidate_id == requester.requester_id:
                return candidate_id
            if scope_configuration.get('type') != ScopeType.PERSONAL \
                    and candidate_id != requester.requester_id:
                return candidate_id
        raise MissingPermissionException()

    @staticmethod
    def get_target_pipeline_manager(
        requester: Requester,
        global_scopes: List[str],
        manager_scopes: List[str]
    ) -> Optional[UUID]:
        has_global_permissions = ScopeChecker.has_at_least_one_permission(
            requester=requester,
            scopes=global_scopes
        )
        has_manager_permissions = ScopeChecker.has_all_permissions(
            requester=requester,
            scopes=manager_scopes
        )
        if has_global_permissions:
            return None
        if has_manager_permissions:
            return requester.requester_id
        raise MissingPermissionException()
