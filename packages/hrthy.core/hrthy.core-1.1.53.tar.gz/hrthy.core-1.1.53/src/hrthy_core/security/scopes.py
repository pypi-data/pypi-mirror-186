# region GLOBAL
SCOPE_REFRESH_TOKEN = 'refresh.token'  # System
SCOPE_ROLE_MY_ASSIGN_GLOBAL = 'rol.my.a.global'  # Superuser
# endregion

# region COMPANY
SCOPE_COMPANY_LIST = 'com.l'  # Superuser
SCOPE_COMPANY_CREATE = 'com.c'  # Superuser
SCOPE_COMPANY_UPDATE = 'com.u'  # Superuser
SCOPE_COMPANY_DELETE = 'com.d'  # Superuser
SCOPE_COMPANY_RESTORE = 'com.r'  # Superuser
SCOPE_COMPANY_MY_UPDATE = 'com.my.u'  # Admin
SCOPE_COMPANY_MY_DELETE = 'com.my.d'  # Admin
SCOPE_COMPANY_MYSELF_GET = 'com.myself.g'  # Myself
# endregion

# region USER
SCOPE_USER_LIST = 'use.l'  # Superuser
SCOPE_USER_CREATE = 'use.c'  # Superuser
SCOPE_USER_UPDATE = 'use.u'  # Superuser
SCOPE_USER_DELETE = 'use.d'  # Superuser
SCOPE_USER_MY_LIST = 'use.my.l'  # Admin
SCOPE_USER_MY_CREATE = 'use.my.c'  # Admin
SCOPE_USER_MY_UPDATE = 'use.my.u'  # Admin
SCOPE_USER_MY_DELETE = 'use.my.d'  # Admin
SCOPE_USER_MYSELF_GET = 'use.myself.g'  # Myself
SCOPE_USER_MYSELF_UPDATE = 'use.myself.u'  # Myself
SCOPE_USER_MYSELF_DELETE = 'use.myself.d'  # Myself
# endregion

# region ROLE
SCOPE_ROLE_LIST = 'rol.l'  # Superuser
SCOPE_ROLE_CREATE = 'rol.c'  # Superuser
SCOPE_ROLE_UPDATE = 'rol.u'  # Superuser
SCOPE_ROLE_DELETE = 'rol.d'  # Superuser
SCOPE_ROLE_MY_LIST = 'rol.my.l'  # Admin
SCOPE_ROLE_MY_CREATE = 'rol.my.c'  # Admin
SCOPE_ROLE_MY_UPDATE = 'rol.my.u'  # Admin
SCOPE_ROLE_MY_DELETE = 'rol.my.d'  # Admin
SCOPE_ROLE_MYSELF_GET = 'rol.myself.g'  # Myself
# endregion

# region LICENSE
SCOPE_LICENSE_POOL_LIST = 'lic_pool.l'  # Superuser
SCOPE_LICENSE_POOL_CREATE = 'lic_pool.c'  # Superuser
SCOPE_LICENSE_POOL_UPDATE = 'lic_pool.u'  # Superuser
SCOPE_LICENSE_POOL_DELETE = 'lic_pool.d'  # Superuser
SCOPE_LICENSE_POOL_MY_LIST = 'lic_pool.my.l'  # Admin, User
# endregion

# region CANDIDATE
SCOPE_CANDIDATE_LIST = 'can.l'  # Superuser
SCOPE_CANDIDATE_CREATE = 'can.c'  # Superuser
SCOPE_CANDIDATE_UPDATE = 'can.u'  # Superuser
SCOPE_CANDIDATE_DELETE = 'can.d'  # Superuser
SCOPE_CANDIDATE_MY_LIST = 'can.my.l'  # Admin, User
SCOPE_CANDIDATE_MY_CREATE = 'can.my.c'  # Admin, User
SCOPE_CANDIDATE_MY_UPDATE = 'can.my.u'  # Admin, User
SCOPE_CANDIDATE_MY_DELETE = 'can.my.d'  # Admin, User
SCOPE_CANDIDATE_MYSELF_GET = 'can.myself.g'  # Myself
SCOPE_CANDIDATE_MYSELF_UPDATE = 'can.myself.u'  # Myself
# endregion

# region CANDIDATE ADD. FIELDS
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_LIST = 'can.fields.l'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_LIST = 'can.fields.protected.l'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_CREATE = 'can.fields.c'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_CREATE = 'can.fields.protected.c'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_UPDATE = 'can.fields.u'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_UPDATE = 'can.fields.protected.u'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_DELETE = 'can.fields.d'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_DELETE = 'can.fields.protected.d'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_LIST = 'can.fields.my.l'  # Admin, User
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_LIST = 'can.fields.protected.my.l'  # Admin, User
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_CREATE = 'can.fields.my.c'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_CREATE = 'can.fields.protected.my.c'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_UPDATE = 'can.fields.my.u'  # Admin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_UPDATE = 'can.fields.protected.my.u'  # Admin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_DELETE = 'can.fields.my.d'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_DELETE = 'can.fields.protected.my.d'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_UPDATE = 'can.fields.value.u'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_VALUE_UPDATE = 'can.fields.protected.value.u'  # Superuser
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_MY_UPDATE = 'can.fields.value.my.u'  # Admin, User
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_VALUE_MY_UPDATE = 'can.fields.protected.value.my.u'  # Admin, User
# endregion

# region PIPELINE
SCOPE_PIPELINE_LIST = 'pip.l'  # Superuser
SCOPE_PIPELINE_CREATE = 'pip.c'  # Superuser
SCOPE_PIPELINE_UPDATE = 'pip.u'  # Superuser
SCOPE_PIPELINE_DELETE = 'pip.d'  # Superuser
SCOPE_PIPELINE_MY_LIST = 'pip.my.l'  # Admin, User
SCOPE_PIPELINE_MY_CREATE = 'pip.my.c'  # Admin, User
SCOPE_PIPELINE_MY_UPDATE = 'pip.my.u'  # Admin, User
SCOPE_PIPELINE_MY_DELETE = 'pip.my.d'  # Admin, User
SCOPE_PIPELINE_MYSELF_GET = 'pip.myself.g'  # Myself
# endregion

# region PIPELINE - CANDIDATE
SCOPE_PIPELINE_CANDIDATE_ASSIGN = 'pip.can.a'  # Superuser
SCOPE_PIPELINE_CANDIDATE_UNASSIGN = 'pip.can.u'  # Superuser
SCOPE_PIPELINE_CANDIDATE_MY_ASSIGN = 'pip.can.my.a'  # Admin, User
SCOPE_PIPELINE_CANDIDATE_MY_UNASSIGN = 'pip.can.my.u'  # Admin, User
# endregion

# region PIPELINE - MANAGER
SCOPE_PIPELINE_MANAGER_ASSIGN = 'pip.man.a'  # Superuser
SCOPE_PIPELINE_MANAGER_UNASSIGN = 'pip.man.u'  # Superuser
SCOPE_PIPELINE_MANAGER_MY_ASSIGN = 'pip.man.my.a'  # Admin, User
SCOPE_PIPELINE_MANAGER_MY_UNASSIGN = 'pip.man.my.u'  # Admin, User
# endregion

# region PIPELINE ADD. FIELDS
SCOPE_PIPELINE_ADDITIONAL_FIELDS_LIST = 'pip.fields.l'  # Superuser
SCOPE_PIPELINE_ADDITIONAL_FIELDS_UPDATE = 'pip.fields.u'  # Superuser
SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_LIST = 'pip.fields.my.l'  # Admin, User
SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_UPDATE = 'pip.fields.my.u'  # Admin, User
# endregion

# region PAYMENT
SCOPE_PAYMENT_LIST = 'pay.l'  # Admin
SCOPE_PAYMENT_MY_LIST = 'pay.my.l'  # Admin
SCOPE_PAYMENT_MY_CREATE = 'pay.my.c'  # Admin
# endregion
