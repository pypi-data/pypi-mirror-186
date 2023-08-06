import json
import uuid
from dataclasses import dataclass
from functools import reduce
from typing import Iterator, Optional

from azure.servicebus import ServiceBusClient, ServiceBusMessage


@dataclass
class EventMessage:
    event: dict
    subject: str
    message_id: Optional[str] = None

    def __post_init__(self):
        self.message_id = self.message_id if self.message_id else str(uuid.uuid4())

    @classmethod
    def from_func_msg(cls, msg):
        """
        Parse Azure Function Service Bus trigger binding message to an
        event message"""
        return cls(
            event=json.loads(msg.get_body()),
            message_id=msg.message_id,
            subject=msg.label,
        )


class WarpzoneEventClient:
    """Class to interact with Azure Service Bus for events"""

    def __init__(self, service_bus_client: ServiceBusClient):
        self._service_bus_client = service_bus_client

    @classmethod
    def from_connection_string(cls, conn_str: str) -> "WarpzoneEventClient":
        service_bus_client = ServiceBusClient.from_connection_string(conn_str)
        return cls(service_bus_client)

    def _get_subscription_receiver(
        self,
        topic_name: str,
        subscription_name: str,
        max_wait_time: int = None,
    ):
        return self._service_bus_client.get_subscription_receiver(
            topic_name=topic_name,
            subscription_name=subscription_name,
            max_wait_time=max_wait_time,
        )

    def _get_topic_sender(self, topic_name: str):
        return self._service_bus_client.get_topic_sender(topic_name=topic_name)

    def receive(
        self,
        topic_name: str,
        subscription_name: str,
        max_wait_time: int = None,
    ) -> Iterator[EventMessage]:
        with self._get_subscription_receiver(
            topic_name, subscription_name, max_wait_time
        ) as receiver:
            for az_sdk_msg in receiver:
                content_parts = az_sdk_msg.message.get_data()
                # message data can either be a generator
                # of string or bytes. We want to concatenate
                # them in either case
                content = reduce(lambda x, y: x + y, content_parts)
                yield EventMessage(
                    event=json.loads(content),
                    message_id=az_sdk_msg.message_id,
                    subject=az_sdk_msg.subject,
                )
                receiver.complete_message(az_sdk_msg)

    def send(
        self,
        topic_name: str,
        event_msg: EventMessage,
    ):
        az_sdk_msg = ServiceBusMessage(
            body=json.dumps(event_msg.event),
            subject=event_msg.subject,
            message_id=event_msg.message_id,
        )
        with self._get_topic_sender(topic_name) as sender:
            sender.send_messages(message=az_sdk_msg)
