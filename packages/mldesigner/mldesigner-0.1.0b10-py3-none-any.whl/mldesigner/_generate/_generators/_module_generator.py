# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=protected-access
import hashlib
from pathlib import Path
from typing import Dict, List
from uuid import UUID

from azure.ai.ml.dsl._utils import _sanitize_python_variable_name
from azure.ai.ml.entities import Component
from mldesigner._generate._generate_package import generate_pkg_logger
from mldesigner._generate._generators._components_generator import ComponentReferenceGenerator
from mldesigner._generate._generators._components_impl_generator import ComponentImplGenerator
from mldesigner._generate._generators._init_generator import InitGenerator


def _get_selected_component_name(component):
    """try to use display_name when component name is not clear"""
    if component.display_name and component.name == "azureml_anonymous":
        return component.display_name
    return component.name

def get_unique_component_func_names(components: List[Component]):
    """Try to return unique component func names, raise exception when duplicate component are found."""
    name_to_component = {}
    name_version_to_component = {}
    errors = []

    for component in components:
        selected_name = _get_selected_component_name(component)
        name_version = f"{selected_name}:{component.version}"
        if name_version in name_version_to_component:
            existing_component = name_version_to_component[name_version]
            load_source = [
                existing_component._source_path or existing_component.id,
                component._source_path or existing_component.id,
            ]
            errors.append(f"Duplicate component {name_version} found. Loaded from: {load_source}")
            continue
        name_version_to_component[name_version] = component

        name_candidate = get_unique_component_func_name(name_to_component, component)
        name_to_component[name_candidate] = component
    return name_to_component, errors


def get_unique_component_func_name(existing_names, component):
    component_func_name = _get_selected_component_name(component)
    name_version = f"{component_func_name}:{component.version}"
    name_candidate = _sanitize_python_variable_name(component_func_name)
    if name_candidate not in existing_names:
        return name_candidate

    name_candidate = _sanitize_python_variable_name(name_version)
    if name_candidate not in existing_names:
        return name_candidate

    # if _sanitize_python_variable_name(component_func_name) and _sanitize_python_variable_name(name_version) both exist
    # add hash result behind name_version because current name_version must differ from other name_versions
    suffix = str(UUID(hashlib.md5(name_version.encode("utf-8")).hexdigest()))
    name_candidate = _sanitize_python_variable_name(f"{name_version}_{suffix}")
    return name_candidate


class ModuleGenerator:
    COMPONENTS_FILE_NAME = "_components.py"
    COMPONENTS_IMPL_FILE_NAME = "_components_impl.py"
    COMPONENTS_INIT_NAME = "__init__.py"

    def __init__(
        self,
        assets: list,
        working_dir: Path,
        target_dir: Path,
        module_name: str,
        pattern_to_components: Dict[str, List[Component]],
        force_regenerate=False,
    ):
        self._components = self._load_components_from_asset_matcher(assets, pattern_to_components)
        self._module_name = module_name

        # sort the components so generated file are sorted.
        self._components = sorted(self._components, key=lambda c: f"{c.name}:{c.version}")

        # handle conflicts
        name_to_components, errors = get_unique_component_func_names(self._components)
        self.errors = errors

        self._ref_generator = ComponentReferenceGenerator(
            name_to_components=name_to_components, module_dir=target_dir / self._module_name
        )
        self._impl_generator = ComponentImplGenerator(name_to_components=name_to_components)
        self._init_generator = InitGenerator(ref_generator=self._ref_generator)
        self._working_dir = Path(working_dir)
        self._force_regenerate = force_regenerate

    @classmethod
    def _load_components_from_asset_matcher(cls, assets: list, pattern_to_components: dict):
        components = []
        for asset in assets:
            components += pattern_to_components[asset]
        return components

    def generate(self, target_dir: Path):
        if not self._components:
            return
        target_module_folder = target_dir / self._module_name
        if target_module_folder.exists():
            if not self._force_regenerate:
                msg = f"Skip generating module {target_module_folder.as_posix()} since it's already exists."
                generate_pkg_logger.warning(msg)
                return
        else:
            target_module_folder.mkdir(parents=True)

        self._ref_generator.generate_to_file(target_module_folder / self.COMPONENTS_FILE_NAME)
        self._impl_generator.generate_to_file(target_module_folder / self.COMPONENTS_IMPL_FILE_NAME)
        self._init_generator.generate_to_file(target_module_folder / self.COMPONENTS_INIT_NAME)
