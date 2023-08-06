import os
import pathlib
import random
import subprocess as spr
import sys
import time
import uuid
from typing import TYPE_CHECKING, Any, Callable, Dict, Iterator, List, Type

import pytest
from pydantic import BaseModel  # pylint: disable=no-name-in-module

from demessaging import config
from demessaging.types import TypeMixin

try:
    import xarray
except ImportError:
    xarray = None  # type: ignore
else:
    try:
        import netCDF4
    except ImportError:
        netCDF4 = None  # type: ignore


os.environ["DASF_REPORT_SHOW_METHOD"] = "PRINT"


if TYPE_CHECKING:
    from _pytest.monkeypatch import MonkeyPatch


test_dir = pathlib.Path(__file__).parent


@pytest.fixture(scope="session")
def test_module_path() -> str:
    return str(test_dir / "_test_module.py")


@pytest.fixture(scope="session")
def test_module_path_xr() -> str:
    return str(test_dir / "_test_module_with_xarray.py")


@pytest.fixture(scope="session")
def test_module_path_report() -> str:
    return str(test_dir / "_test_module_with_report.py")


@pytest.fixture(scope="session")
def test_module_path_basemodel() -> str:
    return str(test_dir / "_test_module_with_basemodel_type.py")


@pytest.fixture(scope="session")
def requests_path() -> pathlib.Path:
    return test_dir / "requests"


@pytest.fixture(scope="session")
def test_request_path(requests_path: pathlib.Path) -> str:
    return str(requests_path / "test_request.json")


@pytest.fixture(scope="session")
def test_request_arbitrary_path(requests_path: pathlib.Path) -> str:
    return str(requests_path / "test_request_arbitrary.json")


@pytest.fixture(scope="session")
def test_request_xr_path(requests_path: pathlib.Path) -> str:
    return str(requests_path / "test_request_xarray.json")


@pytest.fixture(scope="session")
def test_request_report_path(requests_path: pathlib.Path) -> str:
    return str(requests_path / "test_report_request.json")


@pytest.fixture
def tmp_sys_path(
    tmp_path: pathlib.Path, monkeypatch: "MonkeyPatch"
) -> pathlib.Path:
    """Get a temporary path and add it to the sys.path."""
    monkeypatch.syspath_prepend(str(tmp_path))
    return tmp_path


@pytest.fixture
def random_mod_name() -> str:
    """Generate a random module name."""
    return "test_" + str(random.randint(1, 10000))


@pytest.fixture
def tmp_module(tmp_sys_path: pathlib.Path, random_mod_name: str):
    """Generate a path to a module file for tests."""
    return tmp_sys_path / (random_mod_name + ".py")


@pytest.fixture
def func_sig() -> Callable[[int], List[int]]:
    """Create a test function with signature and docstring."""

    def func(a: int) -> List[int]:
        """A test function.

        With some docu.

        Parameters
        ----------
        a: integer
            An integer

        Returns
        -------
        list of int
            A list of integers
        """
        return [a]

    return func


@pytest.fixture
def func_invalid_sig() -> Callable[[int], List[int]]:
    """Create a test function with signature and docstring."""

    def func(a: int) -> List[int]:
        """A test function.

        With some docu.

        Parameters
        ----------
        a: integer
            An integer

        Returns
        -------
        list of int
            A list of integers
        """
        return a  # type: ignore

    return func


@pytest.fixture
def func_missing_doc() -> Callable[[int], int]:
    """Get a function with missing documentation."""

    def func(a: int) -> int:
        return a

    return func


@pytest.fixture
def func_missing_sig() -> Callable:
    """Get a function with missing signatures"""

    def func(a):
        """Do something.

        Parameters
        ----------
        a: int
            A parameter

        Returns
        -------
        int
            An integer
        """
        return a

    return func


class ArbitraryType(TypeMixin):
    def __init__(self, a: int):
        self.a = a

    @classmethod
    def validate(cls, v):
        if isinstance(v, cls):
            return v
        else:
            return cls(int(v))


class ArbitraryTestModel(BaseModel):
    """A model for test purposes."""

    int_test_required: int

    int_test_optional: int = 1

    custom_type_required: ArbitraryType

    # the following does not work!!!
    # because Object of type 'ArbitraryType' is not JSON serializable
    # custom_type_optional: ArbitraryType = ArbitraryType(2)


def encode_arbitrary_type(a: ArbitraryType) -> int:
    return a.a


config.registry.register_encoder(ArbitraryType, encode_arbitrary_type)
config.registry.register_import("conftest")


default_registry = config.registry.copy()


@pytest.fixture(autouse=True)
def clean_registry() -> Iterator[config.ApiRegistry]:
    """Generate a clean registry for the test."""
    from demessaging import config

    saved_registry = config.registry

    config.registry = default_registry.copy(deep=True)

    yield config.registry

    config.registry = saved_registry


@pytest.fixture
def func_arbitrary_types() -> Callable[[ArbitraryType], ArbitraryType]:
    """Define a function with an arbitraty class as annotation."""

    def func(a: ArbitraryType) -> ArbitraryType:
        return a

    return func


@pytest.fixture
def func_arbitrary_model() -> Callable[
    [ArbitraryTestModel], ArbitraryTestModel
]:
    """Define a function with an arbitrary model."""

    def func(a: ArbitraryTestModel) -> ArbitraryTestModel:
        return a

    return func


@pytest.fixture
def valid_obj() -> Dict[str, Any]:
    return {"a": 1}


@pytest.fixture
def invalid_obj() -> Dict[str, Any]:
    return {"a": "x"}


@pytest.fixture
def valid_arbitrary_model() -> Dict[str, ArbitraryTestModel]:
    return {
        "a": ArbitraryTestModel(
            int_test_required=1,
            custom_type_required=1,  # type: ignore
        )
    }


@pytest.fixture
def default_class() -> Type[object]:
    """Create a test class with two methods."""

    class Class:
        """A test class."""

        def __init__(self, a: int, b: int = 1):
            """
            Parameters
            ----------
            a : int
                first integer
            b : int, optional
                second integer, by default 1
            """
            self.a = a
            self.b = b

        @staticmethod
        def sum(a: int, b: int) -> int:
            """
            Parameters
            ----------
            a : int
                first integer
            b : int, optional
                second integer, by default 1

            Returns
            -------
            int
                The sum of `a` and `b`
            """
            return a + b

        def _this_should_not_be_included(self, a: int) -> int:
            """This method should not be included because it stats with _

            Parameters
            ----------
            a: int
                Some dummy int
            """
            return a

        def add2a(self, c: int) -> int:
            """Add a number to `a`.

            Parameters
            ----------
            c : int
                The number to add

            Returns
            -------
            int
                a + c
            """
            return self.a + c

        def add2b(self, c: int) -> int:
            """Add a number to `b`

            Parameters
            ----------
            c : int
                The number to add

            Returns
            -------
            int
                b + c
            """
            return self.b + c

    return Class


@pytest.fixture(scope="session")
def topic() -> str:
    """Generate a random topic for testing."""
    return "test_topic_" + uuid.uuid4().urn[9:]


@pytest.fixture(scope="session", params=["", "websocket-url"])
def test_module_args(request, topic: str):
    if request.param == "websocket-url":
        return [
            "--websocket-url",
            config.PulsarConfig(topic=topic).get_topic_url("")[:-1],
            "--consumer-url",
            config.PulsarConfig(topic=topic).get_topic_url(
                "", subscription="1"
            )[:-2],
        ]
    else:
        return []


@pytest.fixture(scope="session")
def test_module_command(
    test_module_path: str, topic: str, test_module_args: List[str]
) -> List[str]:
    """Generate a command for subprocess to launch the test module."""
    return [sys.executable, test_module_path, "-t", topic] + test_module_args


@pytest.fixture(scope="session")
def connected_module(test_module_command: List[str]) -> Iterator[spr.Popen]:
    """Generate a connection to the pulsar messaging system."""
    background_process = None
    try:
        background_process = spr.Popen(test_module_command + ["listen"])
    except Exception:
        raise
    else:
        time.sleep(1)
        yield background_process
        background_process.terminate()


@pytest.fixture(scope="session")
def topic_xr() -> str:
    """Generate a random topic for testing."""
    return "test_topic_" + uuid.uuid4().urn[9:]


@pytest.fixture(scope="session")
def test_module_command_xr(
    test_module_path_xr: str, topic_xr: str
) -> List[str]:
    """Generate a command for subprocess to launch the test module."""
    return [sys.executable, test_module_path_xr, "-t", topic_xr]


@pytest.fixture(scope="session")
def topic_basemodel() -> str:
    """Generate a random topic for testing."""
    return "test_topic_" + uuid.uuid4().urn[9:]


@pytest.fixture(scope="session")
def topic_report() -> str:
    """Generate a random topic for testing."""
    return "test_topic_" + uuid.uuid4().urn[9:]


@pytest.fixture(scope="session")
def test_module_command_report(
    test_module_path_report: str, topic_report: str
) -> List[str]:
    """Generate a command for subprocess to launch the test module."""
    return [sys.executable, test_module_path_report, "-t", topic_report]


@pytest.fixture(scope="session")
def test_module_command_basemodel(
    test_module_path_basemodel: str, topic_basemodel: str
) -> List[str]:
    """Generate a command for subprocess to launch the test module."""
    return [sys.executable, test_module_path_basemodel, "-t", topic_basemodel]


@pytest.fixture(scope="session")
def connected_module_xr(
    test_module_command_xr: List[str],
) -> Iterator[spr.Popen]:
    """Generate a connection to the pulsar messaging system."""
    background_process = None

    try:
        background_process = spr.Popen(test_module_command_xr + ["listen"])
    except Exception:
        raise
    else:
        yield background_process
        background_process.terminate()


@pytest.fixture(scope="session")
def spr_basemodel_env(topic_basemodel: str) -> Dict:
    spr_env = os.environ.copy()
    spr_env["TEST_TOPIC"] = topic_basemodel
    return spr_env


@pytest.fixture(scope="session")
def connected_module_basemodel(
    test_module_command_basemodel: List[str], spr_basemodel_env: Dict
) -> Iterator[spr.Popen]:
    """Generate a connection to the pulsar messaging system."""
    background_process = None

    try:
        background_process = spr.Popen(
            test_module_command_basemodel + ["listen"], env=spr_basemodel_env
        )
    except Exception:
        raise
    else:
        yield background_process
        background_process.terminate()


@pytest.fixture(scope="session")
def spr_report_env(topic_report: str) -> Dict:
    spr_env = os.environ.copy()
    spr_env["TEST_TOPIC"] = topic_report
    return spr_env


@pytest.fixture(scope="session")
def connected_module_report(
    test_module_command_report: List[str], spr_report_env: Dict
) -> Iterator[spr.Popen]:
    """Generate a connection to the pulsar messaging system."""
    background_process = None

    try:
        background_process = spr.Popen(
            test_module_command_report + ["listen"], env=spr_report_env
        )
    except Exception:
        raise
    else:
        yield background_process
        background_process.terminate()
