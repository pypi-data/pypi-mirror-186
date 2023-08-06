"""Test module for :mod:`demessaging.config`."""
from typing import Type

from demessaging import backend, config


def test_configure_function(func_sig) -> None:
    """Test configurating a function."""
    config.configure(field_params={"a": {"gt": 0}})(func_sig)
    Model = backend.BackendFunction.create_model(func_sig)

    schema = Model.schema()

    assert "exclusiveMinimum" in schema["properties"]["a"]
    assert schema["properties"]["a"]["exclusiveMinimum"] == 0


def test_configure_class(default_class) -> None:
    """Test configurating a function."""
    config.configure(field_params={"a": {"gt": 0}})(default_class)
    Model = backend.BackendClass.create_model(default_class)

    schema = Model.schema()

    assert "exclusiveMinimum" in schema["properties"]["a"]
    assert schema["properties"]["a"]["exclusiveMinimum"] == 0


def test_configure_method(default_class: Type[object]) -> None:
    """Test configuring a specific method."""

    class TestClass(default_class):  # type: ignore
        @config.configure(field_params={"a": {"gt": 0}})
        def test_method(self, a: int) -> int:
            return a

    Model = backend.BackendClass.create_model(TestClass)

    schema = Model.schema()

    assert (
        "exclusiveMinimum"
        in schema["definitions"]["MethClassTestClassTestMethod"]["properties"][
            "a"
        ]
    )
    aconf = schema["definitions"]["MethClassTestClassTestMethod"][
        "properties"
    ]["a"]
    assert aconf["exclusiveMinimum"] == 0
