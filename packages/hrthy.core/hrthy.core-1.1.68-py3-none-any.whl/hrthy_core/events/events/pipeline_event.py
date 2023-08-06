from uuid import UUID

from hrthy_core.events.events.base_event import BaseEvent, CompanyBasePayload


class PipelineCreatedPayload(CompanyBasePayload):
    name: str


class PipelineUpdatedPayload(PipelineCreatedPayload):
    pass


class PipelineDeletedPayload(CompanyBasePayload):
    pass


class PipelineManagerAssignedPayload(CompanyBasePayload):
    user_id: UUID


class PipelineManagerUnassignedPayload(CompanyBasePayload):
    user_id: UUID


class PipelineCandidateAssignedPayload(CompanyBasePayload):
    candidate_id: UUID


class PipelineCandidateUnassignedPayload(CompanyBasePayload):
    candidate_id: UUID


class PipelineCandidateStartedPayload(CompanyBasePayload):
    candidate_id: UUID
    license_pool_id: UUID


class PipelineCreatedEvent(BaseEvent):
    type = 'PipelineCreatedEvent'
    payload: PipelineCreatedPayload


class PipelineUpdatedEvent(BaseEvent):
    type = 'PipelineUpdatedEvent'
    payload: PipelineUpdatedPayload


class PipelineDeletedEvent(BaseEvent):
    type = 'PipelineDeletedEvent'
    payload: PipelineDeletedPayload


class PipelineManagerAssignedEvent(BaseEvent):
    type = 'PipelineManagerAssignedEvent'
    payload: PipelineManagerAssignedPayload


class PipelineManagerUnassignedEvent(BaseEvent):
    type = 'PipelineManagerUnassignedEvent'
    payload: PipelineManagerUnassignedPayload


class PipelineCandidateAssignedEvent(BaseEvent):
    type = 'PipelineCandidateAssignedEvent'
    payload: PipelineCandidateAssignedPayload


class PipelineCandidateUnassignedEvent(BaseEvent):
    type = 'PipelineCandidateUnassignedEvent'
    payload: PipelineCandidateUnassignedPayload


class PipelineCandidateStartedEvent(BaseEvent):
    type = 'PipelineCandidateStartedEvent'
    payload: PipelineCandidateStartedPayload
