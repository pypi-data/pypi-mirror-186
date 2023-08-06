import logging
from dataclasses import dataclass, field
from typing import Dict

import yaml
from dacite import from_dict, MissingValueError

from blazetest.core.config import LAMBDA_CONFIG_YAML
from blazetest.core.exceptions import (
    LambdaConfigurationFileNotFound,
    LambdaConfigurationMissingValue,
)

logger = logging.getLogger(__name__)


@dataclass
class BuildConfig:
    ecr_repository_name: str


@dataclass
class DeployConfig:
    stack_name: str
    s3_bucket: str
    s3_prefix: str = field(default_factory=lambda: "service")


@dataclass
class LambdaConfig:
    aws_region: str
    build: BuildConfig
    deploy: DeployConfig
    license_key: str = field(default_factory=lambda: None)
    license_file: str = field(default_factory=lambda: None)


class Config:
    @classmethod
    def from_yaml(cls, yaml_file_path: str = None) -> LambdaConfig:
        """Load configuration data from a YAML file and create a `LambdaConfig` object.

        Args:
            yaml_file_path: Path to the YAML file. If not specified, the default
                location specified by `LAMBDA_CONFIG_YAML` will be used.

        Returns:
            A `LambdaConfig` object created from the data in the YAML file.

        Raises:
            LambdaConfigurationFileNotFound: If the specified YAML file does not exist.
            LambdaConfigurationMissingValue: If required values are missing from the YAML file.
        """
        if not yaml_file_path:
            logger.info(
                f"Config file location not specified. Using default location: {LAMBDA_CONFIG_YAML}"
            )
            yaml_file_path = LAMBDA_CONFIG_YAML

        try:
            with open(yaml_file_path) as f:
                data = yaml.safe_load(f)
                return cls._get_dataclass_from_dict(data=data)
        except FileNotFoundError as err:
            raise LambdaConfigurationFileNotFound(
                f"Configuration file does not exist: {err}"
            )

    @staticmethod
    def _get_dataclass_from_dict(data: Dict):
        """Create a `LambdaConfig` object from a dictionary.

        Args:
            data: Dictionary containing configuration data.

        Returns:
            A `LambdaConfig` object created from the data in the dictionary.

        Raises:
            LambdaConfigurationMissingValue: If required values are missing from the dictionary.
        """
        try:
            return from_dict(data_class=LambdaConfig, data=data)
        except MissingValueError as err:
            raise LambdaConfigurationMissingValue(f"Lambda configuration: {err}")
