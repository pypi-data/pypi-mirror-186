# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=protected-access

from typing import Union

from azure.ai.ml import Input, Output
from azure.ai.ml.dsl._utils import _sanitize_python_variable_name
from mldesigner._constants import SupportedParameterTypes
from mldesigner._utils import _sanitize_python_class_name


class ParamGenerator:
    def __init__(self, name: str, param: Union[Input, Output]):
        self._name = name
        self._param = param

        if isinstance(param, Input):
            self._is_input = True
        elif isinstance(param, Output):
            self._is_input = False

        self._arg_type = self._get_arg_type()
        self._comment = self._get_comment()

    def _get_arg_type(self):
        param = self._param
        if isinstance(param, Input):
            if self.is_port():
                # For other type, use Input
                return "Input"
            return param._get_python_builtin_type_str()
        if isinstance(param, Output):
            return "Output"

    def _get_comment(self):
        """Returns comment for current param."""
        comment_str = self.description.replace('"', '\\"')
        hint_item = ["optional"] if self.optional is True else []
        hint_item.extend(
            [f"{key}: {val}" for key, val in zip(["min", "max", "enum"], [self.min, self.max, self.enum]) if val]
        )
        hint_str = ", ".join(hint_item)
        if hint_str:
            return f"{comment_str} ({hint_str})"
        return f"{comment_str}"

    def is_enum(self):
        return self._param._is_enum

    def has_default(self):
        return self.default is not None

    @property
    def default(self):
        result = self._param.get("default")
        if result is not None and self._param.type.lower() == SupportedParameterTypes.STRING:
            result = repr(result)
        return result

    @property
    def optional(self) -> bool:
        return self._is_input and self._param.optional

    @property
    def min(self):
        return self._param.get("min")

    @property
    def max(self):
        return self._param.get("max")

    @property
    def enum(self):
        return self._param.get("enum")

    @property
    def description(self):
        # self._param.type can be a list of types, e.g. ["AnyFile", "AnyDirectory"]
        default_description = self._param.description or str(self._param.type)
        if self.is_port():
            default_description += f" (type: {self._param.type})"
        return default_description

    @property
    def var_name(self):
        return _sanitize_python_variable_name(self._name)

    @property
    def arg_type(self):
        return self._arg_type

    @property
    def comment(self):
        return self._comment

    def is_port(self):
        """If input/output is not literal, fallback to Input/Output"""
        return not self._param._is_literal()


class EnumGenerator(ParamGenerator):
    def __init__(self, name: str, param: Input, component_cls_name):
        self._component_cls_name = component_cls_name
        super(EnumGenerator, self).__init__(name=name, param=param)

    def _get_arg_type(self):
        return self.enum_cls_name

    @property
    def component_cls_name(self):
        return self._component_cls_name

    @property
    def enum_cls_name(self):
        return f"{self.component_cls_name}{_sanitize_python_class_name(self.var_name)}"

    @property
    def default(self):
        result = self._param.get("default")
        if result:
            return f"{self.enum_cls_name}.{_sanitize_python_variable_name(result).upper()}"
        return None

    @property
    def var_2_options(self) -> dict:
        if self.enum:
            return {_sanitize_python_variable_name(option).upper(): option for option in self.enum}
        return {}
