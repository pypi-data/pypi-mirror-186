# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=redefined-builtin, unused-argument

from functools import wraps
from os import PathLike
from pathlib import Path
from typing import Any, Callable, TypeVar, Union, get_type_hints

_TFunc = TypeVar("_TFunc", bound=Callable[..., Any])

DEFAULT_COMPONENT_LOADER_CONFIG_PATH = Path(".").parent / "components.yaml"


def reference_component(path: Union[PathLike, str] = None, name=None, version=None, registry=None, **kwargs) -> _TFunc:
    """Reference an existing component with a function and return a component node built with given params.
    The referenced component can be defined with local yaml file or in remote with name and version.
    The returned component node type are hint with function return annotation and default to Command.
    If the referenced component is local component, it'll be registered as anonymous component in pipeline's workspace.
    If the referenced component is workspace component, we assume it has been registered in pipeline's workspace.
    If the referenced component is registry component, it'll still be referenced from registry in pipeline.

    Eg: Both
    .. code-block:: python

        @reference_component()
        def my_func():
            ...
    and
    .. code-block:: python

        @reference_component()
        def my_func() -> Command:
            ...
    with return a Command node.
    .. code-block:: python

        @reference_component()
        def my_func() -> Parallel:
            ...
    will return a Parallel node.

    :param path: Path to local component file.
    :type path: str
    :param name: Name of component to load.
    :type name: str
    :param version: Version of component to load.
    :type version: str
    :param registry: Registry of component's source. None means it's not a registry component.
    :type registry: str

    :return: Component node.
    :rtype: Union[Command, Parallel]
    """

    def component_decorator(func: _TFunc) -> _TFunc:
        @wraps(func)
        def wrapper(*args, **inner_kwargs):
            from azure.ai.ml.dsl._dynamic import _assert_arg_valid
            from azure.ai.ml.entities._builders import Command
            from azure.ai.ml.exceptions import UserErrorException
            from mldesigner._component_loader import ComponentLoader, ComponentsConfig
            from mldesigner._generate._generators._constants import COMPONENT_TO_NODE

            if args:
                raise UserErrorException(
                    message="`reference_component` wrapped function only accept keyword parameters."
                )
            # handle params case insensitively, raise error when unknown kwargs are passed
            _assert_arg_valid(inner_kwargs, func.__code__.co_varnames, func_name=func.__name__)

            # currently component loader only support load 1 component in reference_component
            # create a component loader only contain 1 component config with function name as key
            component_loader = ComponentLoader(
                components_config=ComponentsConfig.create_single_component_config(
                    key=func.__name__, path=path, name=name, version=version, registry=registry
                ),
                default_component_loader_config_path=DEFAULT_COMPONENT_LOADER_CONFIG_PATH,
            )

            component = component_loader.load_component(name=func.__name__)

            result_cls = get_type_hints(func).get("return", Command)

            # supported return annotations, traverse in order
            # Note: make sure no base node in supported_cls
            supported_cls = COMPONENT_TO_NODE.values()
            for cls in supported_cls:
                if issubclass(result_cls, cls):
                    result_cls = cls
            if result_cls not in supported_cls:
                msg = (
                    f"Return annotation of `reference_component` wrapped function can only be {supported_cls} "
                    f"or its subclass, got {result_cls} instead."
                )
                raise UserErrorException(message=msg)

            # This node will be init with inner_kwargs and push to pipeline stack
            node = result_cls(component=component, inputs=inner_kwargs, _from_component_func=True)

            node = component_loader.apply_post_load_func(node=node)

            return node

        return wrapper

    return component_decorator
