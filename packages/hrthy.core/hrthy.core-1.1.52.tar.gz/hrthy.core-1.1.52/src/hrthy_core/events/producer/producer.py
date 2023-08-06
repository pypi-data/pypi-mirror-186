import signal
from time import sleep
from typing import List

from kafka import KafkaProducer
from kafka.errors import KafkaError
from sqlalchemy.orm import Session

from hrthy_core.models.base_model import BaseEventModel
from hrthy_core.models.transaction import transaction
from hrthy_core.repository.event.repository_abstract import BaseEventRepositoryAbstract
from hrthy_core.utils.utils import logger


class BaseProducer:
    CONNECTION_RETRY: int = 0
    DB: Session = None
    BROKERS: List[str] = None
    REPOSITORY: BaseEventRepositoryAbstract = None

    EXIT: bool = False

    _event_found = False

    def __init__(self):
        if any(
                [
                    self.DB is None,
                    self.BROKERS is None,
                    self.REPOSITORY is None
                ]
        ):
            raise RuntimeError("Producer Wrong Configuration.")
        signal.signal(signal.SIGTERM, self._signal_handler)
        self._connect_producer()

    def _signal_handler(self):
        self.EXIT = True

    def _connect_producer(self) -> None:
        try:
            self._create_producer()
        except KafkaError as ex:
            self.CONNECTION_RETRY += 1
            if self.CONNECTION_RETRY < 20 and not self.EXIT:
                logger.info('Kafka not Ready. Retry again. Tentative: %s' % self.CONNECTION_RETRY)
                sleep(self.CONNECTION_RETRY ** 2)
                self._connect_producer()
            else:
                logger.exception(ex)

    def _create_producer(self) -> None:
        self.producer = KafkaProducer(
            bootstrap_servers=self.BROKERS,
        )
        logger.info('Kafka connected')

    def _send(self, event: BaseEventModel):
        self.producer.send(event.topic, event.event.encode('utf-8'))
        self._flush()

    def _flush(self):
        self.producer.flush()

    def start(self):
        while True:
            if self.EXIT:
                break
            try:
                sleep(0.3 if not self._event_found else 0)
                with transaction(self.DB):
                    event: BaseEventModel = self.REPOSITORY.get_first_event_to_send()
                    if event:
                        self._event_found = True
                        self._send(event)
                        self.REPOSITORY.set_event_as_sent(event)
                    else:
                        self._event_found = False
                # Cleanup inside a new transaction
                with transaction(self.DB):
                    self.REPOSITORY.cleanup_old_sent_events()
            except Exception as ex:
                logger.exception(ex)
