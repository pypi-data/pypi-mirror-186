from time import time
from uuid import UUID

from pydantic import Field, typing
from pydantic.main import BaseModel

from hrthy_core.security.security import Requester


class BaseEvent(BaseModel):
    type: str = 'BaseEvent'
    timestamp: int = Field(default_factory=lambda: int(time()))
    requester: Requester
    payload: typing.Any
    retry: int = 0
    retry_at: int = None


class BasePayload(BaseModel):
    id: UUID


class CompanyBasePayload(BasePayload):
    company_id: UUID
