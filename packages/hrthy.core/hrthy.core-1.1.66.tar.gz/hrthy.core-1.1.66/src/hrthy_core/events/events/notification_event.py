from uuid import UUID

from hrthy_core.events.events.base_event import BaseEvent, CompanyBasePayload


class EmailNotificationToUserSentPayload(CompanyBasePayload):
    user_id: UUID


class EmailNotificationToCandidateSentPayload(CompanyBasePayload):
    candidate_id: UUID


class EmailNotificationToUserFailedPayload(CompanyBasePayload):
    user_id: UUID


class EmailNotificationToCandidateFailedPayload(CompanyBasePayload):
    candidate_id: UUID


class EmailNotificationToUserSentEvent(BaseEvent):
    type = 'EmailNotificationToUserSentEvent'
    payload: EmailNotificationToUserSentPayload


class EmailNotificationToCandidateSentEvent(BaseEvent):
    type = 'EmailNotificationToCandidateSentEvent'
    payload: EmailNotificationToCandidateSentPayload


class EmailNotificationToUserFailedEvent(BaseEvent):
    type = 'EmailNotificationToUserFailedEvent'
    payload: EmailNotificationToUserFailedPayload


class EmailNotificationToCandidateFailedEvent(BaseEvent):
    type = 'EmailNotificationToCandidateFailedEvent'
    payload: EmailNotificationToCandidateFailedPayload
