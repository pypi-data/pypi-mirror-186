from enum import Enum


class ScopeType(Enum):
    GLOBAL = 'global'
    COMPANY = 'company'
    PERSONAL = 'personal'


class ConditionType(str, Enum):
    AND = 'and'
    OR = 'or'
