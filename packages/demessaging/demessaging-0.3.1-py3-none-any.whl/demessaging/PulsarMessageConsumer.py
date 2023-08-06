from warnings import warn

from demessaging.messaging.consumer import MessageConsumer  # noqa: F403, F401

warn(
    "The demessaging.PulsarMessageConsumer module has been renamed to "
    "demessaging.messaging.consumer and will be removed soon!",
    DeprecationWarning,
)


class PulsarMessageConsumer(MessageConsumer):
    # deprecated

    def __init__(self, *args, **kwargs):
        warn(
            "The `demessaging.PulsarMessageConsumer.PulsarMessageConsumer` "
            "class has been replaced by the "
            "`demessaging.messaging.consumer.MessageConsumer` class "
            "and will be removed soon!",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)
