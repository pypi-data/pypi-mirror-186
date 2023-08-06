"""Configuration classes for the de-messaging backend module."""
from __future__ import annotations

import importlib
import inspect
import textwrap
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)
from warnings import warn

from deprogressapi import BaseReport
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from pydantic import (
    BaseSettings,
    Field,
    Json,
    PositiveInt,
    root_validator,
    validator,
)

from demessaging.template import Template

if TYPE_CHECKING:
    from demessaging.backend.class_ import BackendClass
    from demessaging.backend.function import BackendFunction


T = TypeVar("T", bound=Callable[..., Any])


def type_to_string(type_: Any):
    if inspect.isclass(type_):
        if type_.__module__ == "builtins":
            return type_.__name__
        return f"{type_.__module__}.{type_.__name__}"
    else:
        return str(type_)


def build_parameter_docs(model: Type[BaseModel]) -> str:
    """Build the docstring for the parameters of a model."""
    docstring = "\n\nParameters\n----------"
    for fieldname, field in model.__fields__.items():
        param_doc = textwrap.dedent(
            f"""
            {fieldname} : {type_to_string(field.type_)}
                {field.field_info.description}
            """
        )
        docstring = docstring + param_doc.rstrip()
    return docstring


def append_parameter_docs(model: Type[BaseModel]) -> Type[BaseModel]:
    """Append the parameters section to the docstring of a model."""
    docstring = build_parameter_docs(model)
    model.__doc__ += docstring
    return model


@append_parameter_docs
class ApiRegistry(BaseModel):
    """A registry for imports and encoders"""

    @validator("imports")
    @classmethod
    def can_import_import(cls, imports: Dict[str, str]) -> Dict[str, str]:
        errors: List[ImportError] = []
        for key in imports:
            try:
                importlib.import_module(key)
            except ImportError as e:
                errors.append(e)
            except Exception:
                raise
        if errors:
            raise ValueError(
                "Could not import all modules!\n    "
                + "\n    ".join(map(str, errors))
            )
        return imports

    json_encoders: Dict[Any, Callable[[Any], Any]] = Field(
        default_factory=dict,
        description=(
            "Custom encoders for datatypes. See "
            "https://pydantic-docs.helpmanual.io/usage/exporting_models/#json_encoders"  # noqa: E501
        ),
    )

    imports: Dict[str, str] = Field(
        default_factory=dict,
        description=(
            "Modules to import at the top of every file. The first "
            "item is the module, the second is the alias"
        ),
    )

    objects: List[str] = Field(
        default_factory=list,
        description=(
            "Source code for objects that should be inlined in the generated "
            "Python API."
        ),
    )

    def register_import(
        self, module: str, alias: Optional[str] = None
    ) -> None:
        """Register a module that needs to be imported in generated API files.

        Parameters
        ----------
        module: str
            The name of the module, e.g. matplotlib.pyplot
        """
        self.imports[module] = alias or ""

    def register_encoder(
        self, Class: Any, encoder: Callable[[Any], Any]
    ) -> None:
        """Register an encoder for the backend config.

        This function can be used to register a custom encoder for a type.
        You should use this for any object that cannot be decoded by default
        using the standard json.dumps.

        Under the hood, this is then transformed as the ``json_encoders``
        configuration value for pydantic (see
        https://pydantic-docs.helpmanual.io/usage/exporting_models/#modeljson)

        Parameters
        ----------
        Class: object
            The type that can be encoded by the given encoder
        encoder: function
            A function that takes one argument, an instance of `Class` and
            converts it to a JSON-conform representation
        """
        self.json_encoders[Class] = encoder

    def register_type(self, obj: T) -> T:
        """Register a class or function to be available in the generated API.

        Use this function if you want to have certain functions of classes
        available in the generated API module, but they should not be
        transformed to a call to the backend module.
        """
        self.objects.append(inspect.getsource(obj))
        return obj

    def hard_code(self, python_code: str) -> None:
        """Register some code to be implemented in the generated module.

        Parameters
        ----------
        python_code: str
            The code that is supposed to be executed on a module level.
        """
        self.objects.append(python_code)
        return


#: registry for the stuff that should be available in the generated client stub
registry = ApiRegistry()


def _get_registry() -> ApiRegistry:
    """Convenience function to get :attr:`registry`.

    Without this, the default value for the config classes `registry` attribute
    would always be empty.
    """
    return registry


@append_parameter_docs
class BaseConfig(BaseModel):
    """Configuration base class for functions, modules and classes."""

    doc: str = Field(
        "",
        description=(
            "The documentation of the object. If empty, this will be taken "
            "from the corresponding ``__doc__`` attribute."
        ),
    )

    registry: ApiRegistry = Field(
        default_factory=_get_registry,
        description="Utilities for imports and encoders.",
    )

    template: Template = Field(
        Template(name="empty"),
        description=(
            "The :class:`demessaging.template.Template` that is used "
            "to render this object for the generated API."
        ),
    )

    def render(self, **context) -> str:
        """Generate the code to call this function in the frontend."""
        context["config"] = self
        code = self.template.render(**context)
        return code


@append_parameter_docs
class FunctionConfig(BaseConfig):
    """Configuration class for a backend module function."""

    class Config:
        arbitrary_types_allowed = True
        extra = "forbid"

    name: str = Field(
        "",
        description=(
            "The name of the function. If empty, this will be taken from the "
            "functions ``__name__`` attribute."
        ),
    )

    signature: Optional[inspect.Signature] = Field(
        None,
        description=(
            "The calling signature for the function. If empty, this will be "
            "taken from the function itself."
        ),
    )

    validators: Dict[str, classmethod] = Field(
        default_factory=dict,
        description="custom validators for the constructor parameters",
    )

    field_params: Dict[str, Dict[str, Any]] = Field(
        default_factory=dict,
        description=(
            "custom Field overrides for the constructor parameters. See "
            ":func:`pydantic.Fields.Field`"
        ),
    )

    returns: Dict[str, Any] = Field(
        default_factory=dict, description="custom returns overrides."
    )

    annotations: Dict[str, Any] = Field(
        default_factory=dict,
        description="custom annotations for function parameters",
    )

    template: Template = Field(
        Template(name="function.py"),
        description=(
            "The :class:`demessaging.template.Template` that is used "
            "to render the function for the generated API."
        ),
    )

    reporter_args: Dict[str, BaseReport] = Field(
        default_factory=dict,
        description="Arguments that use the dasf-progress-api",
    )


@append_parameter_docs
class ClassConfig(BaseConfig):
    """Configuration class for a backend module class."""

    class Config:
        arbitrary_types_allowed = True
        extra = "forbid"

    name: str = Field(
        "",
        description=(
            "The name of the function. If empty, this will be taken from the "
            "classes ``__name__`` attribute."
        ),
    )

    init_doc: str = Field(
        "",
        description=(
            "The documentation of the function. If empty, this will be taken "
            "from the classes ``__init__`` method."
        ),
    )

    signature: Optional[inspect.Signature] = Field(
        None,
        description=(
            "The calling signature for the function. If empty, this will be "
            "taken from the function itself."
        ),
    )

    methods: List[str] = Field(
        default_factory=list,
        description="methods to use within the backend modules",
    )

    validators: Dict[str, classmethod] = Field(
        default_factory=dict,
        description="custom validators for the constructor parameters",
    )

    field_params: Dict[str, Dict[str, Any]] = Field(
        default_factory=dict,
        description=(
            "custom Field overrides for the constructor parameters. "
            "See :func:`pydantic.Fields.Field`"
        ),
    )

    annotations: Dict[str, Any] = Field(
        default_factory=dict,
        description="custom annotations for constructor parameters",
    )

    template: Template = Field(
        Template(name="class_.py"),
        description=(
            "The :class:`demessaging.template.Template` that is used "
            "to render the class for the generated API."
        ),
    )

    reporter_args: Dict[str, BaseReport] = Field(
        default_factory=dict,
        description="Arguments that use the dasf-progress-api",
    )


@append_parameter_docs
class BaseMessagingConfig(BaseSettings):
    """Base class for messaging configs."""

    class Config:
        env_prefix = "de_backend_"

    topic: str = Field(
        description=(
            "The topic identifier under which to register at the pulsar."
        )
    )

    header: Union[Json[Dict[str, Any]], Dict[str, Any]] = Field(  # type: ignore
        default_factory=dict, description="Header parameters for the request"
    )

    max_workers: Optional[PositiveInt] = Field(
        default=None,
        description=(
            "(optional) number of concurrent workers for handling requests, "
            "default: number of processors on the machine, multiplied by 5."
        ),
    )

    queue_size: Optional[PositiveInt] = Field(
        default=None,
        description=(
            "(optional) size of the request queue, if MAX_WORKERS is set, "
            "this needs to be at least as big as MAX_WORKERS, "
            "otherwise an AttributeException is raised."
        ),
    )

    max_payload_size: int = Field(
        default=500 * 1024,
        description=(
            "(optional) maximum payload size, must be smaller than pulsars 'webSocketMaxTextFrameSize', "
            "which is configured e.g.via 'pulsar/conf/standalone.conf'."
            "default: 512000 (500kb)."
        ),
    )

    @root_validator
    def validate_queue_size(cls, values):
        """Check that the queue_size is smaller than the max_workers."""
        queue_size = values.get("queue_size")
        max_workers = values.get("max_workers")
        if queue_size is not None and max_workers is not None:
            if queue_size < max_workers:
                raise ValueError(
                    f"queue_size ({queue_size}) needs to be larger than or "
                    f"equal to max_workers ({max_workers})"
                )
        return values

    def get_topic_url(
        self, topic: str, subscription: Optional[str] = None
    ) -> str:
        """Build the URL to connect to a websocket."""
        raise NotImplementedError(
            "this method is supposed to be implemented by subclasses"
        )


@append_parameter_docs
class PulsarConfig(BaseMessagingConfig):
    """A configuration class to connect to the pulsar messaging framework."""

    class Config:
        env_prefix = "de_backend_"

    host: str = Field(
        "localhost", description="The remote host of the pulsar."
    )

    port: str = Field(
        "8080", description="The port of the pulsar at the given :attr:`host`."
    )

    persistent: str = Field("non-persistent")

    tenant: str = Field("public")

    namespace: str = Field("default")

    def get_topic_url(
        self, topic: str, subscription: Optional[str] = None
    ) -> str:
        """Build the URL to connect to a websocket."""
        connection_type = "consumer" if subscription else "producer"
        sub = ("/" + subscription) if subscription else ""
        return (
            f"ws://{self.host}:{self.port}/ws/v2/{connection_type}/"
            f"{self.persistent}/{self.tenant}/{self.namespace}/{topic}{sub}"
        )


@append_parameter_docs
class WebsocketURLConfig(BaseMessagingConfig):
    """A configuration for a websocket."""

    class Config:
        env_prefix = "de_backend_"

    websocket_url: str = Field(
        "", description="The fully qualified URL to the websocket."
    )

    producer_url: Optional[str] = Field(
        None,
        description=(
            "An alternative URL to use for producers. If None, the "
            "`websocket_url` will be used."
        ),
    )

    consumer_url: Optional[str] = Field(
        None,
        description=(
            "An alternative URL to use for consumers. If None, the "
            "`websocket_url` will be used."
        ),
    )

    def get_topic_url(
        self, topic: str, subscription: Optional[str] = None
    ) -> str:
        """Build the URL to connect to a websocket."""
        sub = ("/" + subscription) if subscription else ""
        if subscription:
            uri = self.consumer_url or self.websocket_url
        else:
            uri = self.producer_url or self.websocket_url
        if not uri.endswith("/"):
            uri += "/"
        return uri + topic + sub


@append_parameter_docs
class ModuleConfig(BaseConfig):
    """Configuration class for a backend module."""

    class Config:
        arbitrary_types_allowed = True

    # it should be Type[BackendFunction], Type[BaseModel], but that's
    #  not well supported by pydantic
    if TYPE_CHECKING:
        members: List[
            Union[
                str,
                Callable,
                Type[object],
                Type[
                    BackendFunction  # pylint: disable=used-before-assignment  # noqa: E501
                ],
                Type[BackendClass],  # pylint: disable=used-before-assignment
            ]
        ]

    messaging_config: Union[PulsarConfig, WebsocketURLConfig] = Field(
        description="Configuration on how to connect to the message broker."
    )

    members: List[Union[str, Callable, Type[object], Any]] = Field(  # type: ignore  # noqa: E501
        default_factory=list, description="List of members for this module"
    )

    imports: str = Field(
        "",
        description="Imports that should be added to the generate API module.",
    )

    template: Template = Field(
        Template(name="module.py"),
        description=(
            "The :class:`demessaging.template.Template` that is used "
            "to render the module for the generated API."
        ),
    )

    @property
    def pulsar_config(self) -> Union[PulsarConfig, WebsocketURLConfig]:
        """DEPRECATED! Get the messaging configuration.

        Please use the ``messaging_config`` attribute of this class."""
        warn(
            "The `pulsar_config` property is deprecated. Please use the "
            "`messaging_config` instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.messaging_config


def configure(js: Optional[str] = None, **kwargs) -> Callable[[T], T]:
    """Configuration decorator for function or modules.

    Use this function as a decorator for classes or functions in the backend
    module like so::

        >>> @configure(field_params={"a": {"gt": 0}}, returns={"gt": 0})
        ... def sqrt(a: float) -> float:
        ...     import math
        ...
        ...     return math.sqrt(a)


    The available parameters for this function vary depending on what you
    are decorating. If you are decorating a class, your parameters must be
    valid for the :class:`ClassConfig`. If you are decorating a function, your
    parameters must be valid for a :class:`FunctionConfig`.

    Parameters
    ----------
    js: Optional[str]
        A JSON-formatted string that can be used to setup the config.
    ``**kwargs``
        Any keyword argument that can be used to setup the config.

    Notes
    -----
    If you are specifying any ``kwargs``, your first argument (`js`) should
    be ``None``.
    """

    def decorator(obj: T) -> T:
        ConfClass: Union[Type[ClassConfig], Type[FunctionConfig]]
        if inspect.isclass(obj):
            ConfClass = ClassConfig
        else:
            ConfClass = FunctionConfig
        if js and kwargs:
            raise ValueError(
                "You can either specify a JSON string or keyword arguments, "
                "not both!"
            )
        if js:
            config = ConfClass.parse_raw(js)
        else:
            config = ConfClass(**kwargs)
        obj.__pulsar_config__ = config  # type: ignore
        return obj

    return decorator
