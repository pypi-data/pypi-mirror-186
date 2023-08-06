# region GLOBAL
SCOPE_REFRESH_TOKEN = 'refresh.token'  # System
SCOPE_ROLE_MY_ASSIGN_GLOBAL = 'rol.my.a.global'  # SuperAdmin
# endregion

# region COMPANY
# Permissions to manage companies
SCOPE_COMPANY_LIST = 'com.l'  # SuperAdmin
SCOPE_COMPANY_CREATE = 'com.c'  # SuperAdmin
SCOPE_COMPANY_UPDATE = 'com.u'  # SuperAdmin
SCOPE_COMPANY_DELETE = 'com.d'  # SuperAdmin
SCOPE_COMPANY_RESTORE = 'com.r'  # SuperAdmin
SCOPE_COMPANY_MY_UPDATE = 'com.my.u'  # Admin
SCOPE_COMPANY_MY_DELETE = 'com.my.d'  # Admin
SCOPE_COMPANY_MYSELF_GET = 'com.myself.g'  # Myself
# endregion

# region USER
# Permissions to manage users
SCOPE_USER_LIST = 'use.l'  # SuperAdmin
SCOPE_USER_CREATE = 'use.c'  # SuperAdmin
SCOPE_USER_UPDATE = 'use.u'  # SuperAdmin
SCOPE_USER_DELETE = 'use.d'  # SuperAdmin
SCOPE_USER_MY_LIST = 'use.my.l'  # Admin
SCOPE_USER_MY_CREATE = 'use.my.c'  # Admin
SCOPE_USER_MY_UPDATE = 'use.my.u'  # Admin
SCOPE_USER_MY_DELETE = 'use.my.d'  # Admin
SCOPE_USER_MYSELF_GET = 'use.myself.g'  # Myself
SCOPE_USER_MYSELF_UPDATE = 'use.myself.u'  # Myself
SCOPE_USER_MYSELF_DELETE = 'use.myself.d'  # Myself
# endregion

# region ROLE
# Permissions to manage roles
SCOPE_ROLE_LIST = 'rol.l'  # SuperAdmin
SCOPE_ROLE_CREATE = 'rol.c'  # SuperAdmin
SCOPE_ROLE_UPDATE = 'rol.u'  # SuperAdmin
SCOPE_ROLE_DELETE = 'rol.d'  # SuperAdmin
SCOPE_ROLE_MY_LIST = 'rol.my.l'  # Admin
SCOPE_ROLE_MY_CREATE = 'rol.my.c'  # Admin
SCOPE_ROLE_MY_UPDATE = 'rol.my.u'  # Admin
SCOPE_ROLE_MY_DELETE = 'rol.my.d'  # Admin
SCOPE_ROLE_MYSELF_GET = 'rol.myself.g'  # Myself
# endregion

# region LICENSE
# Permissions to manage license pools
SCOPE_LICENSE_POOL_LIST = 'lic_pool.l'  # SuperAdmin
SCOPE_LICENSE_POOL_CREATE = 'lic_pool.c'  # SuperAdmin
SCOPE_LICENSE_POOL_UPDATE = 'lic_pool.u'  # SuperAdmin
SCOPE_LICENSE_POOL_DELETE = 'lic_pool.d'  # SuperAdmin
SCOPE_LICENSE_POOL_MY_LIST = 'lic_pool.my.l'  # Admin, User
# endregion

# region CANDIDATE
# Permissions to manage candidates
SCOPE_CANDIDATE_LIST = 'can.l'  # SuperAdmin
SCOPE_CANDIDATE_CREATE = 'can.c'  # SuperAdmin
SCOPE_CANDIDATE_UPDATE = 'can.u'  # SuperAdmin
SCOPE_CANDIDATE_DELETE = 'can.d'  # SuperAdmin
SCOPE_CANDIDATE_MY_LIST = 'can.my.l'  # Admin, User
SCOPE_CANDIDATE_MY_CREATE = 'can.my.c'  # Admin, User
SCOPE_CANDIDATE_MY_UPDATE = 'can.my.u'  # Admin, User
SCOPE_CANDIDATE_MY_DELETE = 'can.my.d'  # Admin, User
SCOPE_CANDIDATE_MYSELF_GET = 'can.myself.g'  # Myself
SCOPE_CANDIDATE_MYSELF_UPDATE = 'can.myself.u'  # Myself
# endregion

# region CANDIDATE ADD. FIELDS
# Permissions to manage candidate additional fields
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_LIST = 'can.fields.l'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_LIST = 'can.fields.protected.l'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_CREATE = 'can.fields.c'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_CREATE = 'can.fields.protected.c'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_UPDATE = 'can.fields.u'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_UPDATE = 'can.fields.protected.u'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_DELETE = 'can.fields.d'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_DELETE = 'can.fields.protected.d'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_LIST = 'can.fields.my.l'  # Admin, User
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_LIST = 'can.fields.protected.my.l'  # Admin, User
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_CREATE = 'can.fields.my.c'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_CREATE = 'can.fields.protected.my.c'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_UPDATE = 'can.fields.my.u'  # Admin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_UPDATE = 'can.fields.protected.my.u'  # Admin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_MY_DELETE = 'can.fields.my.d'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_MY_DELETE = 'can.fields.protected.my.d'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_UPDATE = 'can.fields.value.u'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_VALUE_UPDATE = 'can.fields.protected.value.u'  # SuperAdmin
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_VALUE_MY_UPDATE = 'can.fields.value.my.u'  # Admin, User
SCOPE_CANDIDATE_ADDITIONAL_FIELDS_PROTECTED_VALUE_MY_UPDATE = 'can.fields.protected.value.my.u'  # Admin, User
# endregion

# region PIPELINE
# Permissions to manage pipelines
SCOPE_PIPELINE_LIST = 'pip.l'  # SuperAdmin
SCOPE_PIPELINE_CREATE = 'pip.c'  # SuperAdmin
SCOPE_PIPELINE_UPDATE = 'pip.u'  # SuperAdmin
SCOPE_PIPELINE_DELETE = 'pip.d'  # SuperAdmin
SCOPE_PIPELINE_MY_LIST = 'pip.my.l'  # Admin, User
SCOPE_PIPELINE_MY_CREATE = 'pip.my.c'  # Admin, User
SCOPE_PIPELINE_MY_UPDATE = 'pip.my.u'  # Admin, User
SCOPE_PIPELINE_MY_DELETE = 'pip.my.d'  # Admin, User
SCOPE_PIPELINE_MYSELF_GET = 'pip.myself.g'  # Myself
# endregion

# region PIPELINE - CANDIDATE
# Permissions to assign, unassign candidates to a pipeline
SCOPE_PIPELINE_CANDIDATE_LIST = 'pip.can.l'  # SuperAdmin
SCOPE_PIPELINE_CANDIDATE_CREATE = 'pip.can.c'  # SuperAdmin
SCOPE_PIPELINE_CANDIDATE_DELETE = 'pip.can.d'  # SuperAdmin
SCOPE_PIPELINE_CANDIDATE_MY_LIST = 'pip.can.my.l'  # Admin, User
SCOPE_PIPELINE_CANDIDATE_MY_CREATE = 'pip.can.my.c'  # Admin, User
SCOPE_PIPELINE_CANDIDATE_MY_DELETE = 'pip.can.my.d'  # Admin, User
# endregion

# region PIPELINE - MANAGER
# Permissions to assign, unassign managers to a pipeline
SCOPE_PIPELINE_MANAGER_LIST = 'pip.man.l'  # SuperAdmin
SCOPE_PIPELINE_MANAGER_CREATE = 'pip.man.c'  # SuperAdmin
SCOPE_PIPELINE_MANAGER_DELETE = 'pip.man.d'  # SuperAdmin
SCOPE_PIPELINE_MANAGER_MY_LIST = 'pip.man.my.l'  # Admin, User
SCOPE_PIPELINE_MANAGER_MY_CREATE = 'pip.man.my.c'  # Admin, User
SCOPE_PIPELINE_MANAGER_MY_DELETE = 'pip.man.my.d'  # Admin, User
# endregion

# region MANAGER - PIPELINE
# Permissions to manage pipelines by a manager
SCOPE_MANAGER_PIPELINE_MY_LIST = 'man.pip.my.l'  # Manager
SCOPE_MANAGER_PIPELINE_MY_UPDATE = 'man.pip.my.u'  # Manager
SCOPE_MANAGER_PIPELINE_MY_DELETE = 'man.pip.my.d'  # Manager
# endregion

# region PIPELINE ADD. FIELDS
# Permissions to manage pipeline additional fields
SCOPE_PIPELINE_ADDITIONAL_FIELDS_LIST = 'pip.fields.l'  # SuperAdmin
SCOPE_PIPELINE_ADDITIONAL_FIELDS_UPDATE = 'pip.fields.u'  # SuperAdmin
SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_LIST = 'pip.fields.my.l'  # Admin, User
SCOPE_PIPELINE_ADDITIONAL_FIELDS_MY_UPDATE = 'pip.fields.my.u'  # Admin, User
# endregion

# region PAYMENT
# Permissions to manage payments
SCOPE_PAYMENT_LIST = 'pay.l'  # SuperAdmin
SCOPE_PAYMENT_MY_LIST = 'pay.my.l'  # Admin
SCOPE_PAYMENT_MY_CREATE = 'pay.my.c'  # Admin
# endregion
