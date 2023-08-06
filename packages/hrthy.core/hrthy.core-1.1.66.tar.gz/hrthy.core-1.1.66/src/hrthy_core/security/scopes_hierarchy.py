from hrthy_core.security.scopes import (
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_CREATE, SCOPE_CANDIDATE_ADDITIONAL_FIELDS_DELETE,
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_LIST, SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_CREATE,
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_DELETE, SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_LIST,
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_UPDATE, SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_CREATE,
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_DELETE, SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_LIST,
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_CREATE, SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_DELETE,
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_LIST, SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_UPDATE,
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_UPDATE, SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_VALUE_MY_UPDATE,
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_VALUE_UPDATE, SCOPE_CANDIDATE_ADDITIONAL_FIELDS_UPDATE,
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_MY_UPDATE, SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_UPDATE,
    SCOPE_CANDIDATE_CREATE, SCOPE_CANDIDATE_DELETE, SCOPE_CANDIDATE_LIST, SCOPE_CANDIDATE_MYSELF_GET,
    SCOPE_CANDIDATE_MYSELF_UPDATE, SCOPE_CANDIDATE_MY_CREATE, SCOPE_CANDIDATE_MY_DELETE, SCOPE_CANDIDATE_MY_LIST,
    SCOPE_CANDIDATE_MY_UPDATE, SCOPE_CANDIDATE_UPDATE, SCOPE_COMPANY_CREATE, SCOPE_COMPANY_DELETE, SCOPE_COMPANY_LIST,
    SCOPE_COMPANY_MYSELF_GET, SCOPE_COMPANY_MY_DELETE, SCOPE_COMPANY_MY_UPDATE, SCOPE_COMPANY_RESTORE,
    SCOPE_COMPANY_UPDATE, SCOPE_LICENSE_POOL_CREATE, SCOPE_LICENSE_POOL_DELETE, SCOPE_LICENSE_POOL_LIST,
    SCOPE_LICENSE_POOL_MY_LIST, SCOPE_LICENSE_POOL_UPDATE, SCOPE_MANAGER_PIPELINE_MY_DELETE,
    SCOPE_MANAGER_PIPELINE_MY_LIST, SCOPE_MANAGER_PIPELINE_MY_UPDATE,
    SCOPE_PAYMENT_LIST, SCOPE_PAYMENT_MY_CREATE, SCOPE_PAYMENT_MY_LIST, SCOPE_PIPELINE_ADDITIONAL_FIELDS_LIST,
    SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_LIST, SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_UPDATE,
    SCOPE_PIPELINE_ADDITIONAL_FIELDS_UPDATE, SCOPE_PIPELINE_CANDIDATE_CREATE, SCOPE_PIPELINE_CANDIDATE_DELETE,
    SCOPE_PIPELINE_CANDIDATE_LIST, SCOPE_PIPELINE_CANDIDATE_MY_CREATE, SCOPE_PIPELINE_CANDIDATE_MY_DELETE,
    SCOPE_PIPELINE_CANDIDATE_MY_LIST, SCOPE_PIPELINE_CREATE,
    SCOPE_PIPELINE_DELETE, SCOPE_PIPELINE_LIST, SCOPE_PIPELINE_MANAGER_CREATE, SCOPE_PIPELINE_MANAGER_DELETE,
    SCOPE_PIPELINE_MANAGER_LIST, SCOPE_PIPELINE_MANAGER_MY_CREATE, SCOPE_PIPELINE_MANAGER_MY_DELETE,
    SCOPE_PIPELINE_MANAGER_MY_LIST, SCOPE_PIPELINE_MYSELF_GET, SCOPE_PIPELINE_MY_CREATE, SCOPE_PIPELINE_MY_DELETE,
    SCOPE_PIPELINE_MY_LIST,
    SCOPE_PIPELINE_MY_UPDATE, SCOPE_PIPELINE_UPDATE, SCOPE_ROLE_CREATE, SCOPE_ROLE_DELETE, SCOPE_ROLE_LIST,
    SCOPE_ROLE_MYSELF_GET, SCOPE_ROLE_MY_ASSIGN_GLOBAL, SCOPE_ROLE_MY_CREATE, SCOPE_ROLE_MY_DELETE, SCOPE_ROLE_MY_LIST,
    SCOPE_ROLE_MY_UPDATE, SCOPE_ROLE_UPDATE, SCOPE_USER_CREATE, SCOPE_USER_DELETE, SCOPE_USER_LIST,
    SCOPE_USER_MYSELF_DELETE, SCOPE_USER_MYSELF_GET, SCOPE_USER_MYSELF_UPDATE, SCOPE_USER_MY_CREATE,
    SCOPE_USER_MY_DELETE, SCOPE_USER_MY_LIST, SCOPE_USER_MY_UPDATE, SCOPE_USER_UPDATE,
)
from hrthy_core.security.types import ConditionType, ScopeType

# Scopes hierarchy:
# type -> Scope type from GLOBAL, COMPANY, PERSONAL
# includes -> List of lower permissions that are included in the selected one
# depends -> List of permissions that are mandatory to assign the selected one
# visible -> List of permissions already assigned to the user role, that are needed to show the selected one
HIERARCHY_SCOPES = {
    # region GLOBAL
    SCOPE_ROLE_MY_ASSIGN_GLOBAL: {
        'type': ScopeType.GLOBAL,
        'includes': [],
        'depends': None,
        'visible': False
    },
    # endregion

    # region COMPANY
    SCOPE_COMPANY_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [],
        'depends': None,
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_COMPANY_CREATE: {
        'type': ScopeType.GLOBAL,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_COMPANY_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_COMPANY_UPDATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_COMPANY_MY_UPDATE],
        'depends': {ConditionType.AND: [SCOPE_COMPANY_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_COMPANY_DELETE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_COMPANY_MY_DELETE],
        'depends': {ConditionType.AND: [SCOPE_COMPANY_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_COMPANY_RESTORE: {
        'type': ScopeType.GLOBAL,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_COMPANY_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_COMPANY_MY_UPDATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': None,
        'visible': True
    },
    SCOPE_COMPANY_MY_DELETE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': None,
        'visible': True
    },
    SCOPE_COMPANY_MYSELF_GET: {
        'type': ScopeType.PERSONAL,
        'includes': [],
        'depends': None,
        'visible': False
    },
    # endregion

    # region USER
    SCOPE_USER_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_USER_MY_LIST],
        'depends': None,
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_USER_CREATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_USER_MY_CREATE],
        'depends': {ConditionType.AND: [SCOPE_USER_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_USER_UPDATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_USER_MY_UPDATE],
        'depends': {ConditionType.AND: [SCOPE_USER_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_USER_DELETE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_USER_MY_DELETE],
        'depends': {ConditionType.AND: [SCOPE_USER_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_USER_MY_LIST: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': None,
        'visible': True
    },
    SCOPE_USER_MY_CREATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_USER_MY_LIST]},
        'visible': True
    },
    SCOPE_USER_MY_UPDATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_USER_MY_LIST]},
        'visible': True
    },
    SCOPE_USER_MY_DELETE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_USER_MY_LIST]},
        'visible': True
    },
    SCOPE_USER_MYSELF_GET: {
        'type': ScopeType.PERSONAL,
        'includes': [],
        'depends': None,
        'visible': False
    },
    SCOPE_USER_MYSELF_UPDATE: {
        'type': ScopeType.PERSONAL,
        'includes': [],
        'depends': None,
        'visible': True
    },
    SCOPE_USER_MYSELF_DELETE: {
        'type': ScopeType.PERSONAL,
        'includes': [],
        'depends': None,
        'visible': True
    },
    # endregion

    # region ROLE
    SCOPE_ROLE_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_ROLE_MY_LIST],
        'depends': None,
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_ROLE_CREATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_ROLE_MY_CREATE],
        'depends': {ConditionType.AND: [SCOPE_ROLE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_ROLE_UPDATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_ROLE_MY_UPDATE],
        'depends': {ConditionType.AND: [SCOPE_ROLE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_ROLE_DELETE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_ROLE_MY_DELETE],
        'depends': {ConditionType.AND: [SCOPE_ROLE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_ROLE_MY_LIST: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': None,
        'visible': True
    },
    SCOPE_ROLE_MY_CREATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_ROLE_MY_LIST]},
        'visible': True
    },
    SCOPE_ROLE_MY_UPDATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_ROLE_MY_LIST]},
        'visible': True
    },
    SCOPE_ROLE_MY_DELETE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_ROLE_MY_LIST]},
        'visible': True
    },
    SCOPE_ROLE_MYSELF_GET: {
        'type': ScopeType.PERSONAL,
        'includes': [],
        'depends': None,
        'visible': False
    },
    # endregion

    # region LICENSE
    SCOPE_LICENSE_POOL_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_LICENSE_POOL_MY_LIST],
        'depends': None,
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_LICENSE_POOL_CREATE: {
        'type': ScopeType.GLOBAL,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_LICENSE_POOL_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_LICENSE_POOL_UPDATE: {
        'type': ScopeType.GLOBAL,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_LICENSE_POOL_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_LICENSE_POOL_DELETE: {
        'type': ScopeType.GLOBAL,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_LICENSE_POOL_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_LICENSE_POOL_MY_LIST: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': None,
        'visible': True
    },
    # endregion

    # region CANDIDATE
    SCOPE_CANDIDATE_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_ROLE_MY_LIST],
        'depends': None,
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_CREATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_MY_CREATE],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_UPDATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_MY_UPDATE],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_DELETE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_MY_DELETE],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_MY_LIST: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': None,
        'visible': True
    },
    SCOPE_CANDIDATE_MY_CREATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_MY_LIST]},
        'visible': True
    },
    SCOPE_CANDIDATE_MY_UPDATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_MY_LIST]},
        'visible': True
    },
    SCOPE_CANDIDATE_MY_DELETE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_MY_LIST]},
        'visible': True
    },
    SCOPE_CANDIDATE_MYSELF_GET: {
        'type': ScopeType.PERSONAL,
        'includes': [],
        'depends': None,
        'visible': False
    },
    SCOPE_CANDIDATE_MYSELF_UPDATE: {
        'type': ScopeType.PERSONAL,
        'includes': [],
        'depends': None,
        'visible': True
    },
    # endregion

    # region CANDIDATE ADD. FIELDS
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_LIST],
        'depends': None,
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_CREATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_CREATE],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_UPDATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_UPDATE],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_DELETE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_DELETE],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_LIST],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_CREATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_CREATE],
        'depends': {
            ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_CREATE,
                                SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_LIST]
        },
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_UPDATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_UPDATE],
        'depends': {
            ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_UPDATE,
                                SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_LIST]
        },
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_DELETE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_DELETE],
        'depends': {
            ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_DELETE,
                                SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_LIST]
        },
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_UPDATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_MY_UPDATE],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_LIST, SCOPE_CANDIDATE_UPDATE]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_VALUE_UPDATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_VALUE_MY_UPDATE],
        'depends': {
            ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_LIST,
                                SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_UPDATE]
        },
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_LIST: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': None,
        'visible': True
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_CREATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_LIST]},
        'visible': True
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_UPDATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_LIST]},
        'visible': True
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_DELETE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_LIST]},
        'visible': True
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_LIST: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_LIST]},
        'visible': True
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_CREATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {
            ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_LIST,
                                SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_CREATE]
        },
        'visible': True
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_UPDATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {
            ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_LIST,
                                SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_UPDATE]
        },
        'visible': True
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_DELETE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {
            ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_LIST,
                                SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_DELETE]
        },
        'visible': True
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_MY_UPDATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_LIST, SCOPE_CANDIDATE_MY_UPDATE]},
        'visible': True
    },
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_VALUE_MY_UPDATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {
            ConditionType.AND: [SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_LIST, SCOPE_CANDIDATE_MY_UPDATE]
        },
        'visible': True
    },
    # endregion

    # region PIPELINE
    SCOPE_PIPELINE_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_MY_LIST],
        'depends': None,
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PIPELINE_CREATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_MY_CREATE],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PIPELINE_UPDATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_MY_UPDATE],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PIPELINE_DELETE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_MY_DELETE],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PIPELINE_MY_LIST: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': None,
        'visible': True
    },
    SCOPE_PIPELINE_MY_CREATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.OR: [SCOPE_PIPELINE_MY_LIST, SCOPE_MANAGER_PIPELINE_MY_LIST]},
        'visible': True
    },
    SCOPE_PIPELINE_MY_UPDATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_MY_LIST]},
        'visible': True
    },
    SCOPE_PIPELINE_MY_DELETE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_MY_LIST]},
        'visible': True
    },
    SCOPE_PIPELINE_MYSELF_GET: {
        'type': ScopeType.PERSONAL,
        'includes': [],
        'depends': None,
        'visible': False
    },
    # endregion

    # region MANAGER - PIPELINE
    SCOPE_MANAGER_PIPELINE_MY_LIST: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': None,
        'visible': True
    },
    SCOPE_MANAGER_PIPELINE_MY_UPDATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_MANAGER_PIPELINE_MY_LIST]},
        'visible': True
    },
    SCOPE_MANAGER_PIPELINE_MY_DELETE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_MANAGER_PIPELINE_MY_LIST]},
        'visible': True
    },
    # endregion

    # region PIPELINE ADD. FIELDS
    SCOPE_PIPELINE_ADDITIONAL_FIELDS_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_LIST],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PIPELINE_ADDITIONAL_FIELDS_UPDATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_UPDATE],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_ADDITIONAL_FIELDS_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },

    SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_LIST: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.OR: [SCOPE_PIPELINE_MY_LIST, SCOPE_MANAGER_PIPELINE_MY_LIST]},
        'visible': True
    },
    SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_UPDATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_LIST]},
        'visible': True
    },
    # endregion

    # region PIPELINE - CANDIDATE
    SCOPE_PIPELINE_CANDIDATE_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_CANDIDATE_MY_LIST],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_LIST, SCOPE_CANDIDATE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PIPELINE_CANDIDATE_CREATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_CANDIDATE_MY_CREATE],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_CANDIDATE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PIPELINE_CANDIDATE_DELETE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_CANDIDATE_MY_DELETE],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_CANDIDATE_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PIPELINE_CANDIDATE_MY_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [],
        'depends': {
            ConditionType.AND: [
                {ConditionType.OR: [SCOPE_PIPELINE_MY_LIST, SCOPE_MANAGER_PIPELINE_MY_LIST]},
                SCOPE_CANDIDATE_MY_LIST
            ]
        },
        'visible': True
    },
    SCOPE_PIPELINE_CANDIDATE_MY_CREATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_CANDIDATE_MY_LIST]},
        'visible': True
    },
    SCOPE_PIPELINE_CANDIDATE_MY_DELETE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_CANDIDATE_MY_LIST]},
        'visible': True
    },
    # endregion

    # region PIPELINE - MANAGER
    SCOPE_PIPELINE_MANAGER_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_MANAGER_MY_LIST],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_LIST, SCOPE_USER_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PIPELINE_MANAGER_CREATE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_MANAGER_MY_CREATE],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_MANAGER_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PIPELINE_MANAGER_DELETE: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PIPELINE_MANAGER_MY_DELETE],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_MANAGER_LIST]},
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PIPELINE_MANAGER_MY_LIST: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_MY_LIST, SCOPE_USER_MY_LIST]},
        'visible': True
    },
    SCOPE_PIPELINE_MANAGER_MY_CREATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_MANAGER_MY_LIST]},
        'visible': True
    },
    SCOPE_PIPELINE_MANAGER_MY_DELETE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_PIPELINE_MANAGER_MY_LIST]},
        'visible': True
    },
    # endregion

    # region PAYMENT
    SCOPE_PAYMENT_LIST: {
        'type': ScopeType.GLOBAL,
        'includes': [SCOPE_PAYMENT_MY_LIST],
        'depends': None,
        'visible': [SCOPE_ROLE_MY_ASSIGN_GLOBAL]
    },
    SCOPE_PAYMENT_MY_LIST: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': None,
        'visible': True
    },
    SCOPE_PAYMENT_MY_CREATE: {
        'type': ScopeType.COMPANY,
        'includes': [],
        'depends': {ConditionType.AND: [SCOPE_PAYMENT_MY_LIST]},
        'visible': True
    },
    # endregion
}
