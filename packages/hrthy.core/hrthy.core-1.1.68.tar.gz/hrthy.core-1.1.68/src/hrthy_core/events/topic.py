from enum import Enum


class Topic(Enum):
    COMPANY_V1 = 'hrthy.company.v1'
    USER_V1 = 'hrthy.user.v1'
    USER_AUTH_V1 = 'hrthy.user.auth.v1'
    ROLE_V1 = 'hrthy.role.v1'
    CANDIDATE_V1 = 'hrthy.candidate.v1'
    CANDIDATE_AUTH_V1 = 'hrthy.candidate.auth.v1'
    PIPELINE_V1 = 'hrthy.pipeline.v1'
    LICENSE_V1 = 'hrthy.license.v1'
    NOTIFICATION_V1 = 'hrthy.notification.v1'
    PAYMENT_V1 = 'hrthy.payment.v1'

    # Retry
    USER_RETRY_V1 = 'hrthy.user.retry.v1'
    CANDIDATE_RETRY_V1 = 'hrthy.candidate.retry.v1'
    PIPELINE_RETRY_V1 = 'hrthy.pipeline.retry.v1'
    LICENSE_RETRY_V1 = 'hrthy.license.retry.v1'
    NOTIFICATION_RETRY_V1 = 'hrthy.notification.retry.v1'
    PAYMENT_RETRY_V1 = 'hrthy.payment.retry.v1'


class TopicGroup(Enum):
    COMPANY = 'company'
    CANDIDATE = 'candidate'
    USER = 'user'
    PIPELINE = 'pipeline'
    LICENSE = 'license'
    NOTIFICATION = 'notification'
    PAYMENT = 'payment'
