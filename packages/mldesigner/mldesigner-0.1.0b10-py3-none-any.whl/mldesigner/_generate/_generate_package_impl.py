# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=protected-access

import glob
import logging
import re
import sys
from fnmatch import fnmatch
from logging import Logger
from pathlib import Path
from typing import List, Tuple, Union

from tqdm import tqdm

from azure.ai.ml import MLClient, load_component
from azure.ai.ml.dsl._utils import _sanitize_python_variable_name
from azure.ai.ml.entities import Component
from mldesigner._constants import REGISTRY_URI_FORMAT
from mldesigner._exceptions import UserErrorException
from mldesigner._generate._assets_entity import PackageAssets
from mldesigner._generate._generate_package import generate_pkg_logger
from mldesigner._generate._generators._constants import COMPONENT_TO_NODE
from mldesigner._generate._generators._package_generator import PackageGenerator
from mldesigner._operations import ComponentOperations
from mldesigner._utils import TimerContext, get_auth, update_logger_level


class AssetsUtil:
    WORKSPACE_PREFIX = "azureml://subscriptions/"
    REGISTRY_PREFIX = REGISTRY_URI_FORMAT
    WORKSPACE_REGEX = r"^azureml://subscriptions/([^/]+)/resourcegroups/([^/]+)/workspaces/([^/]+)/components/?(.*)$"
    REGISTRY_REGEX = r"^azureml://registries/([^/]+)/components/?(.*)$"
    WORKSPACE_FORMATTER = "azureml://subscriptions/{}/resourcegroups/{}/workspaces/{}"
    REGISTRY_FORMATTER = "azureml://registries/{}"
    COMPONENT_FORMATTER = "{prefix}/components/{name}"

    @classmethod
    def match_workspace(cls, asset: str) -> Tuple:
        result = re.match(cls.WORKSPACE_REGEX, asset.lower())
        if result is None:
            raise UserErrorException(
                f"Invalid workspace pattern {asset} specified, valid pattern: {cls.WORKSPACE_REGEX}"
            )
        return tuple(result.groups()[:3])

    @classmethod
    def match_registry(cls, asset: str) -> Tuple:
        result = re.match(cls.REGISTRY_REGEX, asset.lower())
        if result is None:
            raise UserErrorException(f"Invalid registry pattern {asset} specified, valid pattern: {cls.REGISTRY_REGEX}")
        return tuple(result.groups()[:1])

    @classmethod
    def match_remote(cls, asset) -> Tuple:
        try:
            return cls.match_workspace(asset)
        except UserErrorException:
            return cls.match_registry(asset)

    @classmethod
    def refine_pattern(cls, pattern, regex, formatter):
        result = re.match(regex, pattern)
        parts = tuple(part if part else "*" for part in result.groups())
        return formatter.format(*parts)

    @classmethod
    def match_remote_pattern(cls, match_method, asset, result):
        workspace_tuple = match_method(asset)
        workspace_name = workspace_tuple[-1]
        workspace_name = _sanitize_python_variable_name(workspace_name)
        if workspace_name in result:
            existing_pattern = result[workspace_name][0]
            if workspace_tuple != cls.match_remote(existing_pattern):
                raise UserErrorException(
                    f"Pattern {asset} and {existing_pattern} has conflict module name {workspace_name}."
                )
            result[workspace_name].append(asset)
        else:
            result[workspace_name] = [asset]

    @classmethod
    def load_from_list(cls, asset_list: list) -> PackageAssets:
        result = {}
        # raise exception when conflict
        for asset in asset_list:
            if asset.startswith(cls.WORKSPACE_PREFIX):
                cls.match_remote_pattern(cls.match_workspace, asset, result)
            elif asset.startswith(cls.REGISTRY_PREFIX):
                cls.match_remote_pattern(cls.match_registry, asset, result)
            else:
                default_local_module = "components"
                if default_local_module in result:
                    result[default_local_module].append(asset)
                else:
                    result[default_local_module] = [asset]
        return PackageAssets._load(data={"components": result})

    @classmethod
    def load_from_dict(cls, assets):
        return PackageAssets._load(data={"components": assets})

    @classmethod
    def load_from_file(cls, asset_file: str) -> PackageAssets:
        return PackageAssets.load(path=asset_file)

    @classmethod
    def load_components_from_remote(
        cls, pattern: str, component_dict: dict, matcher_func, regex, formatter, max_results=None
    ):
        match_parts = matcher_func(pattern)
        formatted_key = formatter.format(*match_parts)

        if formatted_key in component_dict:
            components = component_dict[formatted_key]
            warnings = []
        else:
            if len(match_parts) == 1:
                registry_name = match_parts[0]
                # use this instead of from_config to avoid loading config from file
                client = MLClient(
                    credential=get_auth(),
                    registry_name=registry_name,
                )
            else:
                client = MLClient(
                    credential=get_auth(),
                    subscription_id=match_parts[0],
                    resource_group_name=match_parts[1],
                    workspace_name=match_parts[2],
                )
            component_operations = ComponentOperations(operations=client.components)
            components, warnings = component_operations.list_component_versions(max_result=max_results)
            component_dict[formatted_key] = components

        # filter components
        filtered_components = []
        pattern = cls.refine_pattern(pattern, regex, formatter + "/components/{}")
        for component in components:
            component_pattern = cls.COMPONENT_FORMATTER.format(prefix=formatted_key, name=component.name)
            if fnmatch(component_pattern, pattern):
                filtered_components.append(component)
        return filtered_components, warnings

    @classmethod
    def load_components_from_workspace(cls, asset: str, component_dict: dict):
        return cls.load_components_from_remote(
            pattern=asset,
            component_dict=component_dict,
            matcher_func=cls.match_workspace,
            regex=cls.WORKSPACE_REGEX,
            formatter=cls.WORKSPACE_FORMATTER,
        )

    @classmethod
    def load_components_from_registry(cls, asset: str, component_dict: dict):
        return cls.load_components_from_remote(
            pattern=asset,
            component_dict=component_dict,
            matcher_func=cls.match_registry,
            regex=cls.REGISTRY_REGEX,
            formatter=cls.REGISTRY_FORMATTER,
        )

    @classmethod
    def load_components_from_local(cls, asset: str) -> Tuple[List[Component], List[str]]:
        component_files = list(glob.glob(asset, recursive=True))
        components = []
        warnings = []
        desc = "Listing components with '{}'".format(asset)

        # set root logger level to CRITICAL to avoid logs during update of progress bar
        with tqdm(
            total=len(component_files), desc=desc, unit="component", position=0
        ) as progress_bar, update_logger_level(logging.CRITICAL):
            for file in component_files:
                progress_bar.update(1)
                try:
                    component = load_component(source=file)
                    components.append(component)
                # pylint: disable=broad-except
                except Exception as e:
                    warnings.append(f"Failed to load {Path(file).as_posix()} due to {e}")
        return components, warnings

    @classmethod
    def parse_validate_asset_dict(cls, asset_dict: PackageAssets) -> Tuple[dict, dict, list]:
        """Parse and validate assets.

        Remove patterns which failed to match components and raise exception when illegal asset specified in assets.
        """
        result = {}
        components_dict = {}
        pattern_to_components = {}
        warning_summary = []
        # TODO: load in parallel
        for module_path, assets in asset_dict.components.items():
            # TODO: raise error when multiple workspaces/registries specified in assets
            formatted_assets = []
            for asset in assets:
                if asset.startswith(cls.WORKSPACE_PREFIX):
                    components, warnings = cls.load_components_from_workspace(asset, components_dict)
                elif asset.startswith(cls.REGISTRY_PREFIX):
                    components, warnings = cls.load_components_from_registry(asset, components_dict)
                else:
                    # otherwise treat as local assets
                    components, warnings = cls.load_components_from_local(asset)
                warning_summary += warnings

                components, warnings = cls.filter_components(components)
                warning_summary += warnings

                if not components:
                    generate_pkg_logger.warning("No matched components found for specified pattern %s", asset)
                    continue
                formatted_assets.append(asset)
                pattern_to_components[asset] = components
            result[module_path] = formatted_assets

        return result, pattern_to_components, warning_summary

    @classmethod
    def summary_generate_package_info(cls, logger: Logger, warnings: list, errors: list):
        if not warnings and not errors:
            return
        logger.info("========== Short generate package summary info ==========")
        for warning in warnings:
            logger.warning(warning)
        for error in errors:
            logger.error(error)
        logger.info("========== %s error, %s warning ==========", len(errors), len(warnings))

    @classmethod
    def filter_components(cls, components):
        supported_components = COMPONENT_TO_NODE.keys()
        results = []
        warnings = []
        for c in components:
            if c.type not in supported_components:
                warnings.append(f"Skipped unsupported component {c.name}, type: {c.type}")
            else:
                results.append(c)
        return results, warnings


def _generate(
    *,
    source: Union[list, dict, str],
    package_name: str = None,
    force_regenerate: bool = False,
    **kwargs,
) -> None:
    # hide mode in kwargs, when export graph to code, can set this to deep mode.
    mode = kwargs.get("mode", "reference")
    if mode != "reference":
        raise UserErrorException(f"Not supported mode: {mode} provided.")

    if isinstance(source, list):
        source = AssetsUtil.load_from_list(source)
    elif isinstance(source, dict):
        source = AssetsUtil.load_from_dict(source)
    elif isinstance(source, str):
        source = AssetsUtil.load_from_file(source)
    else:
        raise UserErrorException(f"Only list, dict and str are supported for assets, got {type(source)}.")

    warning_summary, error_summary = [], []
    working_dir = Path(".")
    generate_pkg_logger.info("========== Generating package in %s ==========", working_dir.absolute().as_posix())
    with TimerContext() as timer:
        source, pattern_to_components, warnings = AssetsUtil.parse_validate_asset_dict(source)
        warning_summary += warnings

        generator = PackageGenerator(
            assets=source,
            working_dir=working_dir,
            package_name=package_name,
            force_regenerate=force_regenerate,
            pattern_to_components=pattern_to_components,
        )
        generator.generate()
        error_summary += generator.errors
    generate_pkg_logger.info(
        "========== Finished generating packages in %s seconds ========== ", timer.get_duration_seconds()
    )

    AssetsUtil.summary_generate_package_info(logger=generate_pkg_logger, warnings=warning_summary, errors=error_summary)

    if error_summary:
        sys.exit(1)
