"""Test module for the :mod:`demessaging.backend` module."""
import importlib
import inspect
import pathlib
import subprocess as spr
import sys
from textwrap import dedent
from typing import Dict, List, Type

import pytest

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


class TestModuleModel:
    """Test class for the :class:`demessaging.backend.BackendModule`."""

    def test_load_all(self) -> None:
        """Test loading everything with __all__."""
        Model = backend.BackendModule.create_model(
            "_test_module", messaging_config=dict(topic="test")
        )
        schema = Model.schema()

        assert "FuncFuncBasic" in schema["definitions"]
        assert "FuncFuncArbitraryType" in schema["definitions"]
        assert "FuncFuncArbitraryModel" in schema["definitions"]

        assert "ClassClass" in schema["definitions"]
        assert "MethClassClassAdd2a" in schema["definitions"]

        assert "_private_func" not in schema["definitions"]
        assert "_PrivateFunc" not in schema["definitions"]
        assert "PrivateFunc" not in schema["definitions"]

    def test_load_function_name(self) -> None:
        """Test loading everything with __all__."""
        Model = backend.BackendModule.create_model(
            "_test_module",
            messaging_config=dict(topic="test"),
            members=["func_basic"],
        )
        schema = Model.schema()

        assert "FuncFuncBasic" in schema["definitions"]
        assert "FuncFuncArbitraryType" not in schema["definitions"]
        assert "ClassClass" not in schema["definitions"]

    def test_load_function(self) -> None:
        """Test loading everything with __all__."""
        from _test_module import func_basic

        Model = backend.BackendModule.create_model(
            "_test_module",
            messaging_config=dict(topic="test"),
            members=[func_basic],
        )
        schema = Model.schema()

        assert "FuncFuncBasic" in schema["definitions"]
        assert "FuncFuncArbitraryType" not in schema["definitions"]
        assert "ClassClass" not in schema["definitions"]

    def test_load_function_model(self) -> None:
        """Test loading everything with __all__."""
        from _test_module import func_basic

        FuncModel = backend.BackendFunction.create_model(func_basic)
        Model = backend.BackendModule.create_model(
            "_test_module",
            messaging_config=dict(topic="test"),
            members=[FuncModel],
        )
        schema = Model.schema()

        assert "FuncFuncBasic" in schema["definitions"]
        assert "FuncFuncArbitraryType" not in schema["definitions"]
        assert "ClassClass" not in schema["definitions"]

    def test_parse_basic(self) -> None:
        """Test parsing a request to the :func:`func_basic` function."""
        Model = backend.BackendModule.create_model(
            "_test_module", messaging_config=dict(topic="test")
        )

        obj = {"func_name": "func_basic", "a": 1}

        model = Model.parse_obj(obj)
        val = model()
        assert val.__root__ == [1]  # type: ignore

    def test_parse_class(self) -> None:
        """Test parsing a request for a class method."""
        Model = backend.BackendModule.create_model(
            "_test_module", messaging_config=dict(topic="test")
        )

        obj = {
            "class_name": "Class",
            "a": 2,
            "function": {"func_name": "add2a", "c": 2},
        }

        model = Model.parse_obj(obj)
        val = model()
        assert val.__root__ == 4  # type: ignore

    def test_connect(
        self, test_module_path: str, test_module_args: List[str]
    ) -> None:
        """Test connecting to the messaging server."""
        spr.check_call(
            [sys.executable, test_module_path]
            + test_module_args
            + ["test-connect"]
        )

    @pytest.mark.usefixtures("connected_module")
    def test_request(
        self,
        test_module_command: List[str],
        test_request_path: str,
    ) -> None:
        """Test parsing a request via the pulsar messaging system."""
        spr.check_call(
            test_module_command + ["send-request", test_request_path]
        )

    @pytest.mark.usefixtures("connected_module")
    def test_request_arbitrary(
        self,
        test_module_command: List[str],
        test_request_arbitrary_path: str,
    ) -> None:
        """Test parsing a request via the pulsar messaging system."""
        spr.check_call(
            test_module_command + ["send-request", test_request_arbitrary_path]
        )

    @pytest.mark.skipif(
        xarray is None or netCDF4 is None,
        reason="xarray and netCDF4 are required",
    )
    @pytest.mark.usefixtures("connected_module_xr")
    def test_request_xarray(
        self,
        test_module_command_xr: List[str],
        test_request_xr_path: str,
    ) -> None:
        """Test parsing a request via the pulsar messaging system."""
        spr.check_call(
            test_module_command_xr + ["send-request", test_request_xr_path]
        )

    @pytest.mark.usefixtures("connected_module_report")
    def test_request_report(
        self,
        test_module_command_report: List[str],
        test_request_report_path: str,
        spr_report_env: Dict,
    ) -> None:
        """Test parsing a request via the pulsar messaging system."""
        spr.check_call(
            test_module_command_report
            + ["send-request", test_request_report_path],
            env=spr_report_env,
        )

    def test_render(
        self, default_class, tmp_module: pathlib.Path, random_mod_name: str
    ) -> None:
        """Test the rendering of a module."""
        import _test_module as ref

        Model = backend.BackendModule.create_model(
            "_test_module", messaging_config=dict(topic="test")
        )

        code = Model.backend_config.render()

        tmp_module.write_text(code)

        mod = importlib.import_module(random_mod_name)

        # test the Class member
        assert hasattr(mod, "Class")

        Class: Type[ref.Class] = mod.Class  # type: ignore

        ref_doc = dedent(inspect.getdoc(ref.Class)).strip()  # type: ignore
        func_doc = dedent(inspect.getdoc(Class)).strip()  # type: ignore

        assert func_doc == ref_doc

        init_ref_doc = dedent(inspect.getdoc(ref.Class.__init__)).strip()  # type: ignore  # noqa: E501
        init_doc = dedent(inspect.getdoc(Class.__init__)).strip()  # type: ignore  # noqa: E501

        assert init_ref_doc == init_doc

        assert hasattr(Class, "sum") and callable(Class.sum)

        params_ref = list(inspect.signature(ref.Class.sum).parameters)
        params = list(inspect.signature(Class.sum).parameters)

        assert params == params_ref

        # test the function member
        assert hasattr(mod, "func_basic")

        ref_doc = dedent(inspect.getdoc(ref.func_basic)).strip()  # type: ignore  # noqa: E501
        func_doc = dedent(inspect.getdoc(mod.func_basic)).strip()  # type: ignore  # noqa: E501

        assert func_doc == ref_doc

    def test_render_with_type(
        self,
        tmp_module: pathlib.Path,
        random_mod_name: str,
    ) -> None:
        """Test the rendering of a module with a custom type defined in it."""

        Model = backend.BackendModule.create_model(
            "_test_module_with_type", messaging_config=dict(topic="test")
        )

        code = Model.generate()

        tmp_module.write_text(code)

        mod = importlib.import_module(random_mod_name)

        # test the Class member
        assert hasattr(mod, "MyType")

        ini = mod.MyType(a=1)  # type: ignore
        assert ini.add2a(1) == 2

    @pytest.mark.usefixtures("connected_module_basemodel")
    def test_generate_and_call_basemodel(
        self,
        test_module_command_basemodel: List[str],
        tmp_module: pathlib.Path,
        random_mod_name: str,
        spr_report_env: Dict,
    ) -> None:
        """Test the generation of a frontend API."""

        with tmp_module.open("w") as f:
            spr.check_call(
                test_module_command_basemodel + ["generate"],
                stdout=f,
                env=spr_report_env,
            )

        mod = importlib.import_module(random_mod_name)

        # test the Class member
        assert hasattr(mod, "TestBaseModelType")

        result = mod.func_basic([dict(data=2)])  # type: ignore
        assert result == 2

        result = mod.TestClass([dict(data=2)]).test_func(dict(data=2))  # type: ignore
        assert result == 4

    @pytest.mark.usefixtures("connected_module")
    def test_generate_and_call(
        self,
        test_module_command: List[str],
        tmp_module: pathlib.Path,
        random_mod_name: str,
    ) -> None:
        """Test the generation of a frontend API."""
        import _test_module as ref

        with tmp_module.open("w") as f:
            spr.check_call(test_module_command + ["generate"], stdout=f)

        mod = importlib.import_module(random_mod_name)

        # test the function member
        assert hasattr(mod, "func_basic")

        result = mod.func_basic(1)  # type: ignore
        assert result == ref.func_basic(1)

        # test the Class member
        assert hasattr(mod, "Class")

        Class: Type[ref.Class] = mod.Class  # type: ignore

        ini = Class(1)
        ref_ini = ref.Class(1)
        result = ini.add2a(2)
        assert result == ref_ini.add2a(2)

    @pytest.mark.usefixtures("connected_module_report")
    def test_generate_and_call_report(
        self,
        test_module_command_report: List[str],
        tmp_module: pathlib.Path,
        random_mod_name: str,
        spr_report_env: Dict,
    ) -> None:
        """Test the generation of a frontend API."""
        import _test_module_with_report as ref

        with tmp_module.open("w") as f:
            spr.check_call(
                test_module_command_report + ["generate"],
                stdout=f,
                env=spr_report_env,
            )

        mod = importlib.import_module(random_mod_name)

        # test the function member
        assert hasattr(mod, "report_test")

        TestReport: Type[ref.TestReport] = mod.TestReport  # type: ignore

        result: TestReport = mod.report_test()  # type: ignore
        assert isinstance(result, TestReport)  # type: ignore

        assert len(TestReport._reports) == 2
