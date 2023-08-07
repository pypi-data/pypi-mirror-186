# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import contextlib
import functools
import importlib
import inspect
import logging
import os
import re
import sys
import types
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

import pkg_resources

from mldesigner._constants import MLDESIGNER_COMPONENT_EXECUTION, VALID_NAME_CHARS, IoConstants
from mldesigner._exceptions import ComponentException, UserErrorException
from mldesigner._logger_factory import _LoggerFactory


def is_valid_name(name: str):
    """Indicate whether the name is a valid component name."""
    return all(c in VALID_NAME_CHARS for c in name)


def _resolve_source_directory():
    """Resolve source directory as last customer frame's module file dir position."""
    source_file = _resolve_source_file()
    # Fall back to current working directory if not found
    return Path(os.getcwd()) if not source_file else Path(os.path.dirname(source_file)).absolute()


def _resolve_source_file():
    """Resolve source file as last customer frame's module file position."""
    try:
        frame_list = inspect.stack()
        # We find the last frame which is in SDK code instead of customer code or dependencies code
        # by checking whether the package name of the frame belongs to azure.ai.ml.component.
        pattern = r"(^mldesigner(?=\..*|$).*)"
        for frame, last_frame in zip(frame_list, frame_list[1:]):
            if _assert_frame_package_name(pattern, frame.frame) and not _assert_frame_package_name(
                pattern, last_frame.frame
            ):
                module = inspect.getmodule(last_frame.frame)
                return Path(module.__file__).absolute() if module else None
    # pylint: disable=broad-except
    except Exception:
        return None


def _assert_frame_package_name(pattern, frame):
    """Check the package name of frame is match pattern."""
    # f_globals records the function's module globals of the frame. And __package__ of module must be set.
    # https://docs.python.org/3/reference/import.html#__package__
    # Although __package__ is set when importing, it may happen __package__ does not exist in globals
    # when using exec to execute.
    package_name = frame.f_globals.get("__package__", "")
    return bool(package_name and re.match(pattern, package_name))


def _mldesigner_component_execution() -> bool:
    """Return True if mldesigner component is executing."""
    if os.getenv(MLDESIGNER_COMPONENT_EXECUTION, "false").lower() == "true":
        return True
    return False


def _relative_to(path, basedir, raises_if_impossible=False):
    """Compute the relative path under basedir.

    This is a wrapper function of Path.relative_to, by default Path.relative_to raises if path is not under basedir,
    In this function, it returns None if raises_if_impossible=False, otherwise raises.

    """
    # The second resolve is to resolve possible win short path.
    path = Path(path).resolve().absolute().resolve()
    basedir = Path(basedir).resolve().absolute().resolve()
    try:
        return path.relative_to(basedir)
    except ValueError:
        if raises_if_impossible:
            raise
        return None


def _is_mldesigner_component(function):
    return hasattr(function, "_is_mldesigner_component")


@contextlib.contextmanager
def _change_working_dir(path, mkdir=True):
    """Context manager for changing the current working directory"""

    saved_path = os.getcwd()
    if mkdir:
        os.makedirs(path, exist_ok=True)
    os.chdir(str(path))
    try:
        yield
    finally:
        os.chdir(saved_path)


def _import_component_with_working_dir(module_name, working_dir=None, force_reload=False):
    if working_dir is None:
        working_dir = os.getcwd()
    working_dir = str(Path(working_dir).resolve().absolute())

    with _change_working_dir(working_dir, mkdir=False), inject_sys_path(working_dir):
        try:
            py_module = importlib.import_module(module_name)
        except Exception as e:
            raise e
        except BaseException as e:
            # raise base exception like system.exit as normal exception
            raise ComponentException(message=str(e)) from e
        loaded_module_file = Path(py_module.__file__).resolve().absolute().as_posix()
        posix_working_dir = Path(working_dir).absolute().as_posix()
        if _relative_to(loaded_module_file, posix_working_dir) is None:
            if force_reload:
                # If force_reload is True, reload the module instead of raising exception.
                # This is used when we don't care the original module with the same name.
                return importlib.reload(py_module)
            raise RuntimeError(
                "Could not import module: '{}' because module with the same name has been loaded.\n"
                "Path of the module: {}\n"
                "Working dir: {}".format(module_name, loaded_module_file, posix_working_dir)
            )
        return py_module


@contextlib.contextmanager
def inject_sys_path(path):
    path_str = str(path)
    sys.path.insert(0, path_str)
    try:
        yield
    finally:
        if path_str in sys.path:
            sys.path.remove(path_str)


def _force_reload_module(module):
    # Reload the module except the case that module.__spec__ is None.
    # In the case module.__spec__ is None (E.g. module is __main__), reload will raise exception.
    if module.__spec__ is None:
        return module
    path = Path(module.__spec__.loader.path).parent
    with inject_sys_path(path):
        return importlib.reload(module)


@contextlib.contextmanager
def environment_variable_overwrite(key, val):
    if key in os.environ.keys():
        backup_value = os.environ[key]
    else:
        backup_value = None
    os.environ[key] = val

    try:
        yield
    finally:
        if backup_value:
            os.environ[key] = backup_value
        else:
            os.environ.pop(key)


def _is_primitive_type(val):
    return val in (int, float, bool, str)


def _sanitize_python_class_name(snake_name: str):
    """Change variable name from snake to camel case."""
    components = snake_name.split("_")
    return "".join(component.title() for component in components)


class TimerContext(object):
    """A context manager calculates duration when executing inner block."""

    def __init__(self):
        self.start_time = None

    def get_duration_seconds(self):
        """Get the duration from context manger start to this function call.
        Result will be format to two decimal places.

        """
        duration = datetime.utcnow() - self.start_time
        return round(duration.total_seconds(), 2)

    def __enter__(self):
        self.start_time = datetime.utcnow()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


@contextlib.contextmanager
def update_logger_level(level):
    logger = logging.getLogger()
    backup_level = logger.level

    logger.setLevel(level)

    try:
        yield
    finally:
        logger.setLevel(backup_level)


def get_package_version(package_name):
    """Get the version of the package."""
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        return None


def check_main_package(logger=None):
    if logger is None:
        logger = _LoggerFactory.get_logger("mldesigner")
    version = get_package_version("azure-ai-ml")
    target_version = "1.2.0"
    version_to_check = pkg_resources.parse_version(target_version)
    msg = (
        f"Mldesigner requires azure-ai-ml >= {target_version} package to be fully functional."
        f"It's highly recommended to install the latest azure-ai-ml package."
    )
    if version:
        if not version.startswith("0.0."):
            # public version
            if pkg_resources.parse_version(version) <= version_to_check:
                logger.warning(msg)
    else:
        logger.warning(msg)


def _is_mldesigner_component_function(func):
    return getattr(func, "_is_mldesigner_component", None) is True


def _is_dsl_pipeline_function(func):
    return getattr(func, "_is_dsl_func", None) is True


def _is_variable_args_function(func):
    is_variable_func = any(
        param.kind in [param.VAR_KEYWORD, param.VAR_POSITIONAL] for param in inspect.signature(func).parameters.values()
    )
    return is_variable_func


def _remove_empty_key_in_dict(data):
    if not isinstance(data, dict):
        return data
    res = {}
    for k, v in data.items():
        if v == {}:
            continue
        res[k] = _remove_empty_key_in_dict(v)
    return res


def get_credential_auth():
    """Get the available credential."""
    from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

    try:
        credential = DefaultAzureCredential()
        # Check if given credential can get token successfully.
        credential.get_token("https://management.azure.com/.default")
    except Exception:  # pylint: disable=broad-except
        # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
        credential = InteractiveBrowserCredential()
    return credential


def _copy_func(f):
    """Copy func without deep copy as some method may contains fields can not be copied."""
    g = types.FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__)
    g = functools.update_wrapper(g, f)
    g.__kwdefaults__ = f.__kwdefaults__
    return g


def extract_input_output_name_from_binding(expression):
    """Use this func to process two format of output string and get valid output name:
    1: parent.jobs.a_job.output.a_port
    2: parent.inputs.a_input
    3: parent.outputs.b_output"""
    _jobs_regex = r"parent.jobs.([^.]+).([^.]+).([^.]+)\Z"
    _inputs_regex = r"parent.inputs.([^.]+)\Z"
    _outputs_regex = r"parent.outputs.([^.]+)\Z"

    if re.match(_jobs_regex, expression):
        expression_l = re.match(_jobs_regex, expression)
        return f"{expression_l.group(1)}.{expression_l.group(2)}.{expression_l.group(3)}"
    if re.match(_inputs_regex, expression):
        return re.match(_inputs_regex, expression).group(1)
    if re.match(_outputs_regex, expression):
        return re.match(_outputs_regex, expression).group(1)
    raise UserErrorException(f"Invalid input expression: {expression}")


class AMLVersionedArmId(object):
    """Parser for versioned arm id: e.g. /subscription/.../code/my-
    code/versions/1.

    :param arm_id: The versioned ARM id.
    :type arm_id: str
    :raises UserErrorException: Raised if the ARM id is incorrectly formatted.
    """

    REGEX_PATTERN = (
        "^/?subscriptions/([^/]+)/resourceGroups/(["
        "^/]+)/providers/Microsoft.MachineLearningServices/workspaces/([^/]+)/([^/]+)/([^/]+)/versions/(["
        "^/]+)"
    )
    PREFIX_REGEX_PATTERN = (
        "azureml:/subscriptions/([^/]+)/resource[gG]roups/([^/]+)/"
        "providers/Microsoft.MachineLearningServices/workspaces/([^/]+)/([^/]+)/([^/]+)/versions/(.+)"
    )

    def __init__(self, arm_id=None):
        self.is_registry_id = None
        if arm_id:
            match = re.match(AMLVersionedArmId.REGEX_PATTERN, arm_id) or re.match(
                AMLVersionedArmId.PREFIX_REGEX_PATTERN, arm_id
            )
            if match:
                self.subscription_id = match.group(1)
                self.resource_group_name = match.group(2)
                self.workspace_name = match.group(3)
                self.asset_type = match.group(4)
                self.asset_name = match.group(5)
                self.asset_version = match.group(6)
            else:
                REGISTRY_VERSION_PATTERN = "^azureml://registries/([^/]+)/([^/]+)/([^/]+)/versions/([^/]+)"
                match = re.match(REGISTRY_VERSION_PATTERN, arm_id)
                if match:
                    self.asset_name = match.group(3)
                    self.asset_version = match.group(4)
                    self.is_registry_id = True
                else:
                    raise UserErrorException(f"Invalid AzureML ARM versioned Id {arm_id}")


class AMLLabelledArmId(object):
    """Parser for versioned arm id: e.g. /subscription/.../code/my-
    code/labels/default.

    :param arm_id: The labelled ARM id.
    :type arm_id: str
    :raises UserErrorException: Raised if the ARM id is incorrectly formatted.
    """

    REGEX_PATTERN = (
        "^/?subscriptions/([^/]+)/resourceGroups/(["
        "^/]+)/providers/Microsoft.MachineLearningServices/workspaces/([^/]+)/([^/]+)/([^/]+)/labels/(["
        "^/]+)"
    )

    def __init__(self, arm_id=None):
        self.is_registry_id = None
        if arm_id:
            match = re.match(AMLLabelledArmId.REGEX_PATTERN, arm_id)
            if match:
                self.subscription_id = match.group(1)
                self.resource_group_name = match.group(2)
                self.workspace_name = match.group(3)
                self.asset_type = match.group(4)
                self.asset_name = match.group(5)
                self.asset_label = match.group(6)
            else:
                REGISTRY_VERSION_PATTERN = "^azureml://registries/([^/]+)/([^/]+)/([^/]+)/versions/([^/]+)"
                match = re.match(REGISTRY_VERSION_PATTERN, arm_id)
                if match:
                    self.asset_name = match.group(3)
                    self.asset_label = match.group(4)
                    self.is_registry_id = True
                else:
                    raise UserErrorException(f"Invalid AzureML ARM versioned Id {arm_id}")


def parse_name_version(name: str) -> Tuple[str, Optional[str]]:
    """Parser for Command.component in the format of "component_name:component_version"
    :param name: The Command.component
    :type name: str
    :raises UserErrorException: Raised if the name is incorrectly formatted
    :return parsed name and version
    """
    if name.find("/") != -1 and name[0] != "/":
        raise UserErrorException(f"Could not parse {name}. If providing an ARM id, it should start with a '/'.")
    token_list = name.split(":")
    if len(token_list) == 1:
        return name, None
    name, *version = token_list  # type: ignore
    return name, ":".join(version)


def _is_arm_id(component_str):
    try:
        AMLVersionedArmId(component_str)
        return True
    except Exception:  # pylint: disable=broad-except
        return False


def _is_name_version(component_str):
    try:
        parse_name_version(component_str)
        return True
    except Exception:  # pylint: disable=broad-except
        return False


def _is_name_label(component_str):
    try:
        AMLLabelledArmId(component_str)
        return True
    except Exception:  # pylint: disable=broad-except
        return False


def private_features_enabled():
    return os.getenv("AZURE_ML_CLI_PRIVATE_FEATURES_ENABLED") in ["True", "true", True]


def is_group(obj):
    """Return True if obj is a group or an instance of a parameter group class."""
    return hasattr(obj, IoConstants.GROUP_ATTR_NAME)


def _write_properties_to_run_history(properties: dict, operation_name: str) -> None:
    """Write properties dict to run history."""
    logger = _LoggerFactory.get_logger("mldesigner")
    logger.info("Start writing properties '%s' to run history...", properties)

    try:
        import mlflow
        from mlflow.tracking import MlflowClient
        from mlflow.utils.rest_utils import http_request

    except ImportError as e:
        raise ImportError(f"mlflow is required to {operation_name}. Please install mlflow first.") from e

    # get mlflow run
    run = mlflow.active_run()
    if run is None:
        run = mlflow.start_run()
    logger.info("Got run '%s' in experiment '%s'", run.info.run_id, run.info.experiment_id)
    # get auth from client
    client = MlflowClient()
    cred = client._tracking_client.store.get_host_creds()  # pylint: disable=protected-access
    # update host to run history and request PATCH API
    cred.host = cred.host.replace("mlflow/v2.0", "mlflow/v1.0").replace("mlflow/v1.0", "history/v1.0")
    response = http_request(
        host_creds=cred,
        endpoint="/experimentids/{}/runs/{}".format(run.info.experiment_id, run.info.run_id),
        method="PATCH",
        json={"runId": run.info.run_id, "properties": properties},
    )
    if response.status_code == 200:
        logger.info("Finish writing properties '%s' to run history", properties)
    else:
        logger.error("Fail writing properties '%s' to run history: %s", properties, response.text)
        response.raise_for_status()


def get_auth():
    from azure.identity import AzureCliCredential, ClientSecretCredential

    auth = AzureCliCredential()

    tenant_id = os.getenv("tenantId", None)
    sp_id = os.getenv("servicePrincipalId", None)
    sp_secret = os.getenv("servicePrincipalKey", None)

    if tenant_id and sp_id and sp_secret:
        auth = ClientSecretCredential(tenant_id, sp_id, sp_secret)
        print(f"Using Service Principal auth with tenantId {tenant_id}")

    return auth
