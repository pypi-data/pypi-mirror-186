from warnings import warn

from demessaging.messaging.producer import MessageProducer  # noqa: F403, F401

warn(
    "The demessaging.PulsarMessageProducer module has been renamed to "
    "demessaging.messaging.producer and will be removed soon!",
    DeprecationWarning,
)


class PulsarMessageProducer(MessageProducer):
    # deprecated

    def __init__(self, *args, **kwargs):
        warn(
            "The `demessaging.PulsarMessageProducer.PulsarMessageProducer` "
            "class has been replaced by the "
            "`demessaging.messaging.producer.MessageProducer` class "
            "and will be removed soon!",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)
