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
    SCOPE_LICENSE_POOL_MY_LIST, SCOPE_LICENSE_POOL_UPDATE, SCOPE_MANAGER_PIPELINE_MY_DELETE, SCOPE_MANAGER_PIPELINE_MY_LIST, SCOPE_MANAGER_PIPELINE_MY_UPDATE,
    SCOPE_PAYMENT_LIST, SCOPE_PAYMENT_MY_CREATE, SCOPE_PAYMENT_MY_LIST, SCOPE_PIPELINE_ADDITIONAL_FIELDS_LIST,
    SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_LIST, SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_UPDATE,
    SCOPE_PIPELINE_ADDITIONAL_FIELDS_UPDATE, SCOPE_PIPELINE_CANDIDATE_CREATE, SCOPE_PIPELINE_CANDIDATE_DELETE,
    SCOPE_PIPELINE_CANDIDATE_LIST, SCOPE_PIPELINE_CANDIDATE_MY_CREATE, SCOPE_PIPELINE_CANDIDATE_MY_DELETE,
    SCOPE_PIPELINE_CANDIDATE_MY_LIST,
    SCOPE_PIPELINE_CREATE,
    SCOPE_PIPELINE_DELETE, SCOPE_PIPELINE_LIST, SCOPE_PIPELINE_MANAGER_CREATE, SCOPE_PIPELINE_MANAGER_DELETE,
    SCOPE_PIPELINE_MANAGER_LIST, SCOPE_PIPELINE_MANAGER_MY_CREATE, SCOPE_PIPELINE_MANAGER_MY_DELETE,
    SCOPE_PIPELINE_MANAGER_MY_LIST, SCOPE_PIPELINE_MY_CREATE, SCOPE_PIPELINE_MY_DELETE, SCOPE_PIPELINE_MY_LIST,
    SCOPE_PIPELINE_MY_UPDATE, SCOPE_PIPELINE_UPDATE, SCOPE_ROLE_CREATE, SCOPE_ROLE_DELETE, SCOPE_ROLE_LIST,
    SCOPE_ROLE_MYSELF_GET, SCOPE_ROLE_MY_ASSIGN_GLOBAL, SCOPE_ROLE_MY_CREATE, SCOPE_ROLE_MY_DELETE, SCOPE_ROLE_MY_LIST,
    SCOPE_ROLE_MY_UPDATE, SCOPE_ROLE_UPDATE, SCOPE_USER_CREATE, SCOPE_USER_DELETE, SCOPE_USER_LIST,
    SCOPE_USER_MYSELF_DELETE, SCOPE_USER_MYSELF_GET, SCOPE_USER_MYSELF_UPDATE, SCOPE_USER_MY_CREATE,
    SCOPE_USER_MY_DELETE, SCOPE_USER_MY_LIST, SCOPE_USER_MY_UPDATE, SCOPE_USER_UPDATE,
)

DESCRIPTIONS_SCOPES = {
    # region GLOBAL
    SCOPE_ROLE_MY_ASSIGN_GLOBAL: 'User can assign global permissions to the role',
    # endregion

    #  region COMPANY
    SCOPE_COMPANY_LIST: 'User can list all the companies',
    SCOPE_COMPANY_CREATE: 'User can create a new company',
    SCOPE_COMPANY_UPDATE: 'User can update a company',
    SCOPE_COMPANY_DELETE: 'User can delete a company',
    SCOPE_COMPANY_RESTORE: 'User can restore a company',
    SCOPE_COMPANY_MY_UPDATE: 'User can update its company',
    SCOPE_COMPANY_MY_DELETE: 'User can delete its company',
    SCOPE_COMPANY_MYSELF_GET: 'User can get its company',
    # endregion

    #  region USER
    SCOPE_USER_LIST: 'User can list all the users in other companies',
    SCOPE_USER_CREATE: 'User can create a new user in other companies',
    SCOPE_USER_UPDATE: 'User can update a user in other companies',
    SCOPE_USER_DELETE: 'User can delete a user in other companies',
    SCOPE_USER_MY_LIST: 'User can list all the users in its company',
    SCOPE_USER_MY_CREATE: 'User can create a new user its its company',
    SCOPE_USER_MY_UPDATE: 'User can update a user in its company',
    SCOPE_USER_MY_DELETE: 'User can delete a user in its company',
    SCOPE_USER_MYSELF_GET: 'User can get itself',
    SCOPE_USER_MYSELF_UPDATE: 'User can update itself',
    SCOPE_USER_MYSELF_DELETE: 'User can delete itself',
    # endregion

    # region ROLE
    SCOPE_ROLE_LIST: 'User can list all the roles in other companies',
    SCOPE_ROLE_CREATE: 'User can create a new role in other companies',
    SCOPE_ROLE_UPDATE: 'User can update a role in other companies',
    SCOPE_ROLE_DELETE: 'User can delete a role in other companies',
    SCOPE_ROLE_MY_LIST: 'User can list all the roles in its company',
    SCOPE_ROLE_MY_CREATE: 'User can create a new role in its company',
    SCOPE_ROLE_MY_UPDATE: 'User can update a role in its company',
    SCOPE_ROLE_MY_DELETE: 'User can delete a role in its company',
    SCOPE_ROLE_MYSELF_GET: 'User can get its role',
    # endregion

    # region LICENSE
    SCOPE_LICENSE_POOL_LIST: 'User can list all the license pool in other companies',
    SCOPE_LICENSE_POOL_CREATE: 'User can create a new license pool in other companies',
    SCOPE_LICENSE_POOL_UPDATE: 'User can update a license pool in other companies',
    SCOPE_LICENSE_POOL_DELETE: 'User can delete a license pool in other companies',
    SCOPE_LICENSE_POOL_MY_LIST: 'User can list all the license pools in its company',
    # endregion

    # region CANDIDATE
    SCOPE_CANDIDATE_LIST: 'User can list all the candidates in other companies',
    SCOPE_CANDIDATE_CREATE: 'User can create a new candidate in other companies',
    SCOPE_CANDIDATE_UPDATE: 'User can update a candidate in other companies',
    SCOPE_CANDIDATE_DELETE: 'User can delete a candidate in other companies',
    SCOPE_CANDIDATE_MY_LIST: 'User can list all the candidates in its company',
    SCOPE_CANDIDATE_MY_CREATE: 'User can create a new candidate in its company',
    SCOPE_CANDIDATE_MY_UPDATE: 'User can update a candidate in its company',
    SCOPE_CANDIDATE_MY_DELETE: 'User can delete a candidate in its company',
    SCOPE_CANDIDATE_MYSELF_GET: 'Candidate can get itself',
    SCOPE_CANDIDATE_MYSELF_UPDATE: 'Candidate can update itself',
    # endregion

    # region CANDIDATE ADD. FIELDS
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_LIST: 'User can list all the candidates additional fields in other companies',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_LIST: 'User can list all the protected candidates additional fields '
                                                      'in other companies',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_CREATE: 'User can create a candidates additional field in other companies',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_UPDATE: 'User can update all the candidates additional fields in other companies',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_DELETE: 'User can delete a candidates additional field in other companies',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_CREATE: 'User can create a protected candidates additional field in '
                                                        'other companies',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_UPDATE: 'User can update all the protected candidates additional '
                                                        'fields in other companies',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_DELETE: 'User can delete a protected candidates additional field in '
                                                        'other companies',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_UPDATE: 'User can update all the candidates additional '
                                                    'fields values in other companies',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_VALUE_UPDATE: 'User can update all the protected candidates additional '
                                                              'fields values in other companies',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_LIST: 'User can list all the candidates additional fields in its company',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_CREATE: 'User can create a candidates additional field in its company',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_UPDATE: 'User can update all the candidates additional fields in its '
                                                 'companies',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_DELETE: 'User can delete a candidates additional field in its company',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_LIST: 'User can list all the protected candidates additional '
                                                         'fields in its company',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_CREATE: 'User can create a protected candidates additional '
                                                           'field in its company',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_UPDATE: 'User can update all the protected candidates additional '
                                                           'fields in its company',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_DELETE: 'User can delete a protected candidates additional '
                                                           'field in its company',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_MY_UPDATE: 'User can update all the candidates additional '
                                                       'fields values in its company',
    SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_VALUE_MY_UPDATE: 'User can update all the protected candidates '
                                                                 'additional fields values in its company',
    # endregion

    # region PIPELINE
    SCOPE_PIPELINE_LIST: 'User can list all the pipelines in other companies',
    SCOPE_PIPELINE_CREATE: 'User can create a new pipeline in other companies',
    SCOPE_PIPELINE_UPDATE: 'User can update a pipeline in other companies',
    SCOPE_PIPELINE_DELETE: 'User can delete a pipeline in other companies',
    SCOPE_PIPELINE_MY_LIST: 'User can list all the pipelines in its company',
    SCOPE_PIPELINE_MY_CREATE: 'User can create a new pipeline in its company',
    SCOPE_PIPELINE_MY_UPDATE: 'User can update a pipeline in its company',
    SCOPE_PIPELINE_MY_DELETE: 'User can delete a pipeline in its company',
    # endregion

    # region PIPELINE ADD. FIELDS
    SCOPE_PIPELINE_ADDITIONAL_FIELDS_LIST: 'User can list all the pipelines additional fields in other companies',
    SCOPE_PIPELINE_ADDITIONAL_FIELDS_UPDATE: 'User can update all the pipelines additional fields in other companies',
    SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_LIST: 'User can list all the pipelines additional fields in its company',
    SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_UPDATE: 'User can update all the pipelines additional fields in its '
                                                'companies',
    # endregion

    # region PIPELINE - CANDIDATE
    SCOPE_PIPELINE_CANDIDATE_LIST: 'User can list all the candidates assigned to a pipeline in other companies',
    SCOPE_PIPELINE_CANDIDATE_CREATE: 'User can assign a candidate to a pipeline in other companies',
    SCOPE_PIPELINE_CANDIDATE_DELETE: 'User can unassign a candidate from a pipeline in other companies',
    SCOPE_PIPELINE_CANDIDATE_MY_LIST: 'User can list all the candidates assigned to a pipeline in its company',
    SCOPE_PIPELINE_CANDIDATE_MY_CREATE: 'User can assign a candidate to a pipeline in its company',
    SCOPE_PIPELINE_CANDIDATE_MY_DELETE: 'User can unassign a candidate from a pipeline in its company',
    # endregion

    # region PIPELINE - MANAGER
    SCOPE_PIPELINE_MANAGER_LIST: 'User can list all the managers assigned to a pipeline in other companies',
    SCOPE_PIPELINE_MANAGER_CREATE: 'User can assign a manager to a pipeline in other companies',
    SCOPE_PIPELINE_MANAGER_DELETE: 'User can unassign a manager from a pipeline in other companies',
    SCOPE_PIPELINE_MANAGER_MY_LIST: 'User can list all the managers assigned to a pipeline in its company',
    SCOPE_PIPELINE_MANAGER_MY_CREATE: 'User can assign a manager to a pipeline in its company',
    SCOPE_PIPELINE_MANAGER_MY_DELETE: 'User can unassign a manager from a pipeline in its company',
    # endregion

    # region MANAGER - PIPELINE
    SCOPE_MANAGER_PIPELINE_MY_LIST: 'Manager can list all the pipelines assigned to him/her',
    SCOPE_MANAGER_PIPELINE_MY_UPDATE: 'Manager can update a pipeline assigned to him/her',
    SCOPE_MANAGER_PIPELINE_MY_DELETE: 'Manager can delete a pipeline assigned to him/her',
    # endregion

    # region PAYMENT
    SCOPE_PAYMENT_LIST: 'User can list payments of other companies',
    SCOPE_PAYMENT_MY_LIST: 'User can list payments of its company',
    SCOPE_PAYMENT_MY_CREATE: 'User can buy new licenses for its company',
    # endregion
}
