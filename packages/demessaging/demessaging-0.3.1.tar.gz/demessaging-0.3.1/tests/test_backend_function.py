"""Test module for the :mod:`demessaging.backend` module."""
import importlib
import inspect
import pathlib
from textwrap import dedent
from typing import Any, Callable, Dict

import pytest
from conftest import ArbitraryType
from pydantic import ValidationError  # pylint: disable=no-name-in-module
from pytest_lazyfixture import lazy_fixture as lf

from demessaging import backend

try:
    import xarray
except ImportError:
    xarray = None  # type: ignore
else:
    try:
        import netCDF4
    except ImportError:
        netCDF4 = None  # type: ignore


class TestFunctionModel:
    """Test functions for creating a function model."""

    def test_missing_doc(self, func_missing_doc: Callable) -> None:
        """Test parsing a function with missing docstrings."""
        Model = backend.BackendFunction.create_model(func_missing_doc)
        schema = Model.schema()
        assert "description" not in schema
        assert "description" not in schema["properties"]["a"]

    def test_missing_sig(self, func_missing_sig: Callable) -> None:
        """Test parsing a function with missing signatures."""
        with pytest.warns(RuntimeWarning, match="Missing signature for a"):
            Model = backend.BackendFunction.create_model(func_missing_sig)
        schema = Model.schema()
        assert "type" not in schema["properties"]["a"]

    @pytest.mark.skip("Not yet adapted")
    def test_missing_return_sig(self, func_missing_sig: Callable) -> None:
        """Test parsing a function with missing signatures."""
        with pytest.warns(RuntimeWarning, match="Missing return signature"):
            Model = backend.BackendFunction.create_model(func_missing_sig)
        schema = Model.schema()
        assert "func_returns" in schema["properties"]
        assert "description" in schema["properties"]["func_returns"]
        desc = schema["properties"]["func_returns"]["description"]
        assert desc == "An integer"

    def test_arbitraty_types(self, func_arbitrary_types: Callable) -> None:
        Model = backend.BackendFunction.create_model(func_arbitrary_types)
        schema = Model.schema()

        # test the properties
        assert "type" not in schema["properties"]["a"]
        assert "custom_type" in schema["properties"]["a"]
        assert schema["properties"]["a"]["custom_type"] == (
            "conftest.ArbitraryType"
        )

        # test the return statement
        # assert "func_returns" in schema["properties"]
        # assert "type" not in schema["properties"]["func_returns"]
        # assert "custom_type" in schema["properties"]["func_returns"]
        # assert schema["properties"]["func_returns"]["custom_type"] == (
        #     "conftest.ArbitraryType"
        # )

    def test_arbitraty_model(self, func_arbitrary_model: Callable) -> None:
        """Test input and output of arbitraty pydantic models."""
        Model = backend.BackendFunction.create_model(func_arbitrary_model)
        schema = Model.schema()

        assert "ArbitraryTestModel" in schema["definitions"]
        assert "$ref" in schema["properties"]["a"]
        assert schema["properties"]["a"]["$ref"].endswith("ArbitraryTestModel")

        assert "ArbitraryTestModel" in schema["definitions"]
        # assert "$ref" in schema["properties"]["func_returns"]
        # assert schema["properties"]["func_returns"]["$ref"].endswith(
        #     "ArbitraryTestModel"
        # )

    @pytest.mark.parametrize(
        "func,obj,xfail",
        [
            (lf("func_sig"), lf("valid_obj"), False),
            (lf("func_sig"), lf("invalid_obj"), True),
            (lf("func_missing_doc"), lf("valid_obj"), False),
            (lf("func_missing_doc"), lf("invalid_obj"), True),
            (lf("func_missing_sig"), lf("valid_obj"), False),
            (lf("func_missing_sig"), lf("invalid_obj"), False),
            (lf("func_arbitrary_types"), lf("valid_obj"), False),
            (lf("func_arbitrary_types"), lf("invalid_obj"), True),
            (lf("func_arbitrary_model"), lf("valid_arbitrary_model"), False),
            (lf("func_arbitrary_model"), lf("invalid_obj"), True),
        ],
    )
    @pytest.mark.filterwarnings("ignore: Missing signature")
    @pytest.mark.filterwarnings("ignore: Missing return signature")
    def test_function_request(
        self, func: Callable, obj: Dict[str, Any], xfail: bool
    ) -> None:
        """Test parsing a function to the model."""
        Model = backend.BackendFunction.create_model(func)
        obj["func_name"] = func.__name__

        if xfail:
            with pytest.raises(ValidationError):
                Model.parse_obj(obj)
        else:
            Model.parse_obj(obj)

    def test_invalid_func_name(
        self, func_sig: Callable, valid_obj: Dict[str, Any]
    ) -> None:
        """Test if the function cannot be parsed if a wrong name is given."""
        Model = backend.BackendFunction.create_model(func_sig)
        valid_obj["func_name"] = func_sig.__name__ + "123"

        with pytest.raises(ValidationError):
            Model.parse_obj(valid_obj)

    def test_missing_func_name(
        self, func_sig: Callable, valid_obj: Dict[str, Any]
    ) -> None:
        """Test if the function cannot be parsed if a wrong name is given."""
        Model = backend.BackendFunction.create_model(func_sig)

        with pytest.raises(ValidationError):
            Model.parse_obj(valid_obj)

    def test_call_function(
        self, func_arbitrary_types: Callable, valid_obj: Dict[str, Any]
    ) -> None:
        """Test calling a function with conversion to arbitrary type."""
        Model = backend.BackendFunction.create_model(func_arbitrary_types)
        valid_obj["func_name"] = func_arbitrary_types.__name__
        model = Model.parse_obj(valid_obj)
        ret = model()
        assert isinstance(ret.__root__, ArbitraryType)  # type: ignore
        assert ret.__root__.a == 1  # type: ignore

    def test_call_function_2(
        self, func_sig: Callable, valid_obj: Dict[str, Any]
    ) -> None:
        """Test calling a function with conversion to list."""
        Model = backend.BackendFunction.create_model(func_sig)
        valid_obj["func_name"] = func_sig.__name__
        model = Model.parse_obj(valid_obj)
        ret = model()
        assert ret.__root__ == [1]  # type: ignore

    def test_call_invalid_function(
        self, func_invalid_sig: Callable, valid_obj: Dict[str, Any]
    ) -> None:
        """Test calling a function with invalid signature."""
        Model = backend.BackendFunction.create_model(func_invalid_sig)
        valid_obj["func_name"] = func_invalid_sig.__name__
        model = Model.parse_obj(valid_obj)
        with pytest.raises(ValidationError):
            model()

    def test_render(
        self,
        func_sig: Callable,
        tmp_module: pathlib.Path,
        random_mod_name: str,
    ) -> None:
        """Test the rendering of a function."""
        Model = backend.BackendFunction.create_model(func_sig)
        code = Model.backend_config.render()

        tmp_module.write_text("from __future__ import annotations\n" + code)

        mod = importlib.import_module(random_mod_name)

        assert hasattr(mod, func_sig.__name__)
        func = getattr(mod, func_sig.__name__)

        ref_doc = dedent(inspect.getdoc(func_sig)).strip()  # type: ignore
        func_doc = dedent(inspect.getdoc(func)).strip()  # type: ignore

        assert func_doc == ref_doc
