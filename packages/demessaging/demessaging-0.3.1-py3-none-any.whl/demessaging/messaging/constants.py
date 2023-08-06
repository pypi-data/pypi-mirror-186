"""Enums within the DASF Messaging Framework."""
from enum import Enum
from typing import Type
from warnings import warn


def generate_enum_doc(class_: Type[Enum]) -> Type[Enum]:
    """Utility function to generate the docstring for an enum."""
    docstring = "\n\nThe following values are valid:\n\n"

    params = [
        f'- **{name}** (``"{prop.value}"``)'
        for name, prop in class_.__members__.items()
    ]

    class_.__doc__ += docstring + "\n".join(params)  # type: ignore
    return class_


@generate_enum_doc
class Status(str, Enum):
    """Status flag of a request."""

    SUCCESS = "success"
    ERROR = "error"
    RUNNING = "running"


@generate_enum_doc
class PropertyKeys(str, Enum):
    """Property keys for a message to the message broker."""

    REQUEST_CONTEXT = "requestContext"
    RESPONSE_TOPIC = "response_topic"
    REQUEST_MESSAGEID = "requestMessageId"
    MESSAGE_TYPE = "messageType"
    FRAGMENT = "fragment"
    NUM_FRAGMENTS = "num_fragments"
    STATUS = "status"


@generate_enum_doc
class MessageType(str, Enum):
    """Supported message types."""

    PING = "ping"
    PONG = "pong"
    REQUEST = "request"
    RESPONSE = "response"
    LOG = "log"
    INFO = "info"
    PROGRESS = "progress"


class _DeprecatedPulsarConfigKeys:
    """DEPRECATED PulsarConfigKeys"""

    def __getattr__(self, attr):
        attrs = dict(
            HOST="host",
            PORT="port",
            PERSISTENT="persistent",
            TENANT="tenant",
            NAMESPACE="namespace",
            TOPIC="topic",
            MAX_WORKERS="max_workers",
            QUEUE_SIZE="queue_size",
            MAX_PAYLOAD_SIZE="max_payload_size",
        )
        try:
            ret = attrs[attr]
        except KeyError:
            raise AttributeError(attr)
        else:
            warn(
                "The PulsarConfigKeys class has been deprecated and will be "
                "removed soon!",
                DeprecationWarning,
                stacklevel=2,
            )
            return ret


PulsarConfigKeys = _DeprecatedPulsarConfigKeys()
