# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=unused-argument

from os import PathLike
from pathlib import Path
from typing import Dict, Union

from azure.ai.ml._utils.utils import load_yaml
from azure.ai.ml.entities._validation import SchemaValidatableMixin
from azure.ai.ml.exceptions import ErrorTarget
from mldesigner._constants import BASE_PATH_CONTEXT_KEY
from mldesigner._exceptions import UserErrorException
from mldesigner._generate._assets_schema import PackageAssetsSchema


class PackageAssets(dict, SchemaValidatableMixin):
    @classmethod
    def _get_schema(cls, context) -> PackageAssetsSchema:
        return PackageAssetsSchema(context=context)

    def _get_validation_error_target(self) -> ErrorTarget:
        """Return the error target of this resource. Should be overridden by subclass.
        Value should be in ErrorTarget enum.
        """
        return ErrorTarget.PIPELINE

    def _create_schema_for_validation(self, context):
        pass

    @property
    def components(self) -> dict:
        return self["components"]

    @classmethod
    def load(
        cls,
        path: Union[PathLike, str] = None,
        **kwargs,
    ) -> "PackageAssets":
        yaml_dict = load_yaml(path)
        if yaml_dict is None:
            msg = "Target yaml file is empty: {}"
            raise UserErrorException(msg.format(path))
        if not isinstance(yaml_dict, dict):
            msg = "Expect dict but get {} after parsing yaml file: {}"
            raise UserErrorException(msg.format(type(yaml_dict), path))
        return cls._load(data=yaml_dict, yaml_path=path)

    @classmethod
    def _load(cls, data: Dict = None, yaml_path: Union[PathLike, str] = None, **kwargs):
        data = data or {}
        context = {
            BASE_PATH_CONTEXT_KEY: Path(yaml_path).parent if yaml_path else Path("./"),
        }
        # pylint: disable=no-member
        return PackageAssets(**cls._get_schema(context=context).load(data))
