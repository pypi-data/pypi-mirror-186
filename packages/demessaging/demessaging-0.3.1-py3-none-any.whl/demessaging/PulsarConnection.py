from warnings import warn

from demessaging.messaging.connection import (  # noqa: F403, F401
    WebsocketConnection,
)

warn(
    "The demessaging.PulsarConnection module has been renamed to "
    "demessaging.messaging.connection and will be removed soon!",
    DeprecationWarning,
)


class PulsarConnection(WebsocketConnection):
    # deprecated

    def __init__(self, *args, **kwargs):
        warn(
            "The `demessaging.PulsarConnection.PulsarConnection` class has "
            "been replaced by the "
            "`demessaging.messaging.connection.WebsocketConnection` class "
            "and will be removed soon!",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)
