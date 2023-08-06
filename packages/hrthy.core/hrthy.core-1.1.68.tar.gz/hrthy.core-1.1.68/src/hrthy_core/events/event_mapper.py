from hrthy_core.events.events.candidate_event import (
    CandidateCreatedEvent, CandidateInvitedEvent, CandidateLoggedInEvent, CandidateLoggedOutEvent,
    CandidateLoginRefreshedEvent, CandidateUpdatedEvent,
)
from hrthy_core.events.events.company_event import (
    CompanyCreatedEvent, CompanyDeletedEvent, CompanyRestoredEvent, CompanyUpdatedEvent,
)
from hrthy_core.events.events.license_event import (
    LicenseConsumedEvent, LicensePoolCreatedEvent, LicensePoolDeletedEvent, LicensePoolUpdatedEvent,
)
from hrthy_core.events.events.notification_event import (
    EmailNotificationToCandidateFailedEvent, EmailNotificationToCandidateSentEvent,
    EmailNotificationToUserFailedEvent, EmailNotificationToUserSentEvent,
)
from hrthy_core.events.events.payment_event import PaymentConfirmedEvent
from hrthy_core.events.events.pipeline_event import (
    PipelineCandidateAssignedEvent, PipelineCandidateStartedEvent, PipelineCandidateUnassignedEvent,
    PipelineCreatedEvent, PipelineDeletedEvent, PipelineUpdatedEvent,
)
from hrthy_core.events.events.role_event import RoleCreatedEvent, RoleDeletedEvent, RoleUpdatedEvent
from hrthy_core.events.events.user_event import (
    UserAcceptedInvitationEvent, UserCreatedEvent, UserDeletedEvent, UserForgotPasswordEvent, UserInvitedEvent,
    UserInvitedResendEvent, UserLoggedInEvent,
    UserLoggedOutEvent, UserLoginRefreshedEvent, UserRestoredEvent, UserUpdatedEvent,
)

event_mapping = {
    # Company
    'CompanyCreatedEvent': CompanyCreatedEvent,
    'CompanyUpdatedEvent': CompanyUpdatedEvent,
    'CompanyDeletedEvent': CompanyDeletedEvent,
    'CompanyRestoredEvent': CompanyRestoredEvent,
    # User
    'UserCreatedEvent': UserCreatedEvent,
    'UserUpdatedEvent': UserUpdatedEvent,
    'UserDeletedEvent': UserDeletedEvent,
    'UserInvitedEvent': UserInvitedEvent,
    'UserInvitedResendEvent': UserInvitedResendEvent,
    'UserRestoredEvent': UserRestoredEvent,
    'UserAcceptedInvitationEvent': UserAcceptedInvitationEvent,
    # Role
    'RoleCreatedEvent': RoleCreatedEvent,
    'RoleUpdatedEvent': RoleUpdatedEvent,
    'RoleDeletedEvent': RoleDeletedEvent,
    # User Auth
    'UserLoggedInEvent': UserLoggedInEvent,
    'UserLoggedOutEvent': UserLoggedOutEvent,
    'UserLoginRefreshedEvent': UserLoginRefreshedEvent,
    'UserForgotPasswordEvent': UserForgotPasswordEvent,
    # Candidate
    'CandidateCreatedEvent': CandidateCreatedEvent,
    'CandidateUpdatedEvent': CandidateUpdatedEvent,
    'CandidateInvitedEvent': CandidateInvitedEvent,
    # Candidate Auth
    'CandidateLoggedInEvent': CandidateLoggedInEvent,
    'CandidateLoggedOutEvent': CandidateLoggedOutEvent,
    'CandidateLoginRefreshedEvent': CandidateLoginRefreshedEvent,
    # Pipeline
    'PipelineCreatedEvent': PipelineCreatedEvent,
    'PipelineUpdatedEvent': PipelineUpdatedEvent,
    'PipelineDeletedEvent': PipelineDeletedEvent,
    'PipelineCandidateAssignedEvent': PipelineCandidateAssignedEvent,
    'PipelineCandidateUnassignedEvent': PipelineCandidateUnassignedEvent,
    'PipelineCandidateStartedEvent': PipelineCandidateStartedEvent,
    # License
    'LicensePoolCreatedEvent': LicensePoolCreatedEvent,
    'LicensePoolUpdatedEvent': LicensePoolUpdatedEvent,
    'LicensePoolDeletedEvent': LicensePoolDeletedEvent,
    'LicenseConsumedEvent': LicenseConsumedEvent,
    # Notification
    'EmailNotificationToUserSentEvent': EmailNotificationToUserSentEvent,
    'EmailNotificationToCandidateSentEvent': EmailNotificationToCandidateSentEvent,
    'EmailNotificationToUserFailedEvent': EmailNotificationToUserFailedEvent,
    'EmailNotificationToCandidateFailedEvent': EmailNotificationToCandidateFailedEvent,
    # Payment
    'PaymentConfirmedEvent': PaymentConfirmedEvent,
}
