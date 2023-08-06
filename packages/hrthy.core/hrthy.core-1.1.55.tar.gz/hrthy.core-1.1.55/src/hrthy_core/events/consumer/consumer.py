import json
import signal
from time import sleep
from typing import List

from kafka import KafkaConsumer
from kafka.errors import KafkaError

from hrthy_core.events.events.base_event import BaseEvent
from hrthy_core.events.topic import Topic, TopicGroup
from hrthy_core.repository.event.repository_abstract import BaseEventRepositoryAbstract
from hrthy_core.utils.utils import logger


class BaseConsumer:
    CONNECTION_RETRY: int = 0
    TOPICS: list = []
    RETRY_TOPIC: Topic = None
    TOPIC_GROUP: TopicGroup = None
    REPOSITORY: BaseEventRepositoryAbstract = None

    EXIT: bool = False

    def __init__(self):
        super().__init__()
        signal.signal(signal.SIGTERM, self._signal_handler)

    def _signal_handler(self):
        self.EXIT = True

    def _get_topics(self) -> list:
        if not self.RETRY_TOPIC:
            raise Exception('Invalid Retry TOPIC. Please make sure you have it set')
        if type(self.TOPICS) is not list:
            raise Exception('Invalid TOPICS. Please make sure you have it set')
        for topic in self.TOPICS:
            if type(topic) is not Topic:
                raise Exception('Invalid TOPIC in the list. Please make sure to use one of the available topics')
        return [t.value for t in self.TOPICS]

    def _get_topics_group(self) -> str:
        if type(self.TOPIC_GROUP) is not TopicGroup:
            raise Exception('Invalid TOPIC_GROUP. Please make sure you have it set')
        return self.TOPIC_GROUP.value

    def _get_brokers(self) -> list:
        return []

    def _callback(self, message) -> None:
        pass

    def _negative_ack(self, event: BaseEvent):
        self.REPOSITORY.negative_ack(topic=self.RETRY_TOPIC.value, event_to_send=event)

    def start(self, topics_to_restart: List[Topic] = None) -> None:
        try:
            self._start(topics_to_restart=topics_to_restart)
        except KafkaError as ex:
            self.CONNECTION_RETRY += 1
            if self.CONNECTION_RETRY <= 20 and not self.EXIT:
                logger.info('Kafka not Ready. Retry again. Tentative: %s' % self.CONNECTION_RETRY)
                sleep(self.CONNECTION_RETRY ** 2)
                self.start(topics_to_restart=topics_to_restart)
            else:
                logger.exception(ex)

    def _get_topics_to_subscribe(self, topics_to_restart: List[Topic] = None):
        if self._has_topic_to_restart(topics_to_restart):
            return [t.value for t in topics_to_restart]
        return self._get_topics()

    def _has_topic_to_restart(self, topics_to_restart: List[Topic] = None):
        return topics_to_restart and len(topics_to_restart) > 0

    def _start(self, topics_to_restart: List[Topic] = None) -> None:
        topics_to_subscribe = self._get_topics_to_subscribe(topics_to_restart=topics_to_restart)
        consumer = KafkaConsumer(
            *topics_to_subscribe,
            group_id=self._get_topics_group(),
            value_deserializer=lambda v: json.loads(v),
            bootstrap_servers=self._get_brokers(),
            enable_auto_commit=True
        )
        if self._has_topic_to_restart(topics_to_restart=topics_to_restart):
            consumer.poll()
            for x in consumer.assignment():
                consumer.seek(x, 0)
        logger.info('Kafka connected')
        for message in consumer:
            if self.EXIT:
                break
            self._callback(message)
