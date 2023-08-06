from datetime import datetime, timedelta
from operator import or_
from time import time
from typing import Optional

from sqlalchemy import false, null, true
from sqlalchemy.orm import Query, Session

from hrthy_core.events.events.base_event import BaseEvent
from hrthy_core.models.base_model import BaseEventModel
from hrthy_core.repository.event.repository_abstract import BaseEventRepositoryAbstract


class BaseEventRepository(BaseEventRepositoryAbstract):
    MODEL = BaseEventModel

    def __init__(self, db: Session):
        super().__init__()
        self.db = db

    def get_first_event_to_send(self) -> Optional[BaseEventModel]:
        query: Query = self.db.query(self.MODEL) \
            .filter(self.MODEL.sent == false()) \
            .filter(or_(self.MODEL.retry_at == null(), self.MODEL.retry_at <= datetime.utcnow())) \
            .order_by(self.MODEL.retry_at, self.MODEL.created_at) \
            .with_for_update()
        return query.first()

    def set_event_as_sent(self, event: BaseEventModel) -> BaseEventModel:
        event.sent = True
        event.sent_at = datetime.utcnow()
        self.db.add(event)
        return event

    def cleanup_old_sent_events(self) -> None:
        self.db.query(self.MODEL) \
            .filter(self.MODEL.sent == true()) \
            .filter(self.MODEL.sent_at < (datetime.utcnow() - timedelta(days=1))) \
            .delete()

    def negative_ack(self, topic: str, event_to_send: BaseEvent) -> BaseEventModel:
        event_to_send.retry = event_to_send.retry + 1
        event_to_send.retry_at = int(time()) + (event_to_send.retry ** 2)
        return self._send_event(topic=topic, event_to_send=event_to_send)

    def _send_event(self, topic: str, event_to_send: BaseEvent) -> BaseEventModel:
        event = self.MODEL()
        event.topic = topic
        event.event_type = event_to_send.type
        event.event = event_to_send.json()
        event.created_at = datetime.utcnow()
        event.sent = False
        event.retry = event_to_send.retry
        event.retry_at = None if event_to_send.retry_at is None else datetime.utcfromtimestamp(event_to_send.retry_at)
        event.sent_at = None
        self.db.add(event)
        return event
