from warnings import warn

from demessaging.messaging.constants import *  # noqa: F403, F401

warn(
    "The demessaging.PulsarMessageConstants module has been renamed to "
    "demessaging.messaging.constants and will be removed soon!",
    DeprecationWarning,
)
