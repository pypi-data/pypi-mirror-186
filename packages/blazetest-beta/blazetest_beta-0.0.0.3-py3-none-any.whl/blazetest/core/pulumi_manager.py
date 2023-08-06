import logging
import os
import subprocess
from typing import Dict, List

import yaml

from blazetest.core.config import BUILD_FOLDER_PATH, DEFAULT_ENCODING

logger = logging.getLogger(__name__)


class CommandResult:
    def __init__(
        self, completed_process: subprocess.CompletedProcess, allowed_return_codes: List
    ):
        if completed_process.returncode not in allowed_return_codes:
            raise Exception(
                f"Pulumi error with return code {completed_process.returncode}, "
                f"stdout: {completed_process.stdout.decode(DEFAULT_ENCODING)}"
            )

        self.stdout = completed_process.stdout.decode(DEFAULT_ENCODING)
        logger.debug(self.stdout)


class CommandExecutor:
    def __init__(self, executable: str, command: str, arguments: Dict):
        """
        :param executable:
            Executable service or module, for example: sam
        :param command:
            Command for the executable, for example: sam build
        :param arguments:
            Arguments needed to be added to the command
        """
        self.executable = executable
        self.command = command
        self.arguments: List = self.__join_arguments(arguments=arguments)

    def execute_command(self, allowed_return_codes=None) -> CommandResult:
        if allowed_return_codes is None:
            allowed_return_codes = [0]

        logger.debug(
            f"Command: {self.executable} {self.command} {' '.join(self.arguments)}"
        )
        return CommandResult(
            subprocess.run(
                [
                    self.executable,
                    self.command,
                ]
                + self.arguments,
                stdout=subprocess.PIPE,
            ),
            allowed_return_codes=allowed_return_codes,
        )

    @staticmethod
    def __join_arguments(arguments: Dict) -> List:
        arguments_list = []
        for arg_key in arguments:
            arg_value = arguments[arg_key]

            arguments_list.append(arg_key)
            if arg_value is not None:
                arguments_list.append(arg_value)

        return arguments_list


class PulumiManager:
    EXECUTABLE = "pulumi"
    LOGIN_COMMAND = "login"
    STACK_INIT_COMMAND = "stack"
    UP_COMMAND = "up"

    def __init__(self, aws_region: str, stack_name: str):
        self.aws_region = aws_region
        self.stack_name = stack_name

    def deploy(self):
        self.login()
        self.create_config_files()
        self.create_stack()

        logger.info("Deploying..")
        self.up()
        logger.info("Deploying has finished.")

    def up(self):
        return self.__execute(
            command=self.UP_COMMAND,
            arguments={
                "--cwd": ".blazetest/",
                "--stack": self.stack_name,
                "--non-interactive": None,
                "--yes": None,
            },
        )

    def create_stack(self):
        return self.__execute(
            command=self.STACK_INIT_COMMAND,
            arguments={
                "init": self.stack_name,
                "--non-interactive": None,
            },
            allowed_return_codes=[0, 255],
        )

    def login(self):
        return self.__execute(
            command=self.LOGIN_COMMAND,
            arguments={
                "--local": None,
            },
        )

    def __execute(
        self, command: str, arguments: Dict, allowed_return_codes=None
    ) -> str:
        if allowed_return_codes is None:
            allowed_return_codes = [0]

        command_executor = CommandExecutor(
            executable=self.EXECUTABLE,
            command=command,
            arguments=arguments,
        )
        command_result: CommandResult = command_executor.execute_command(
            allowed_return_codes=allowed_return_codes
        )
        return command_result.stdout

    def create_config_files(self):
        pulumi_yaml = {
            "name": "blazetest-aws",
            "runtime": {
                "name": "python",
                "options": {
                    "virtualenv": "venv",
                },
            },
        }
        pulumi_dev_yaml = {
            "config": {
                "aws:region": self.aws_region,
            }
        }
        with open(os.path.join(BUILD_FOLDER_PATH, "Pulumi.yaml"), "w") as f:
            yaml.dump(pulumi_yaml, f, default_flow_style=False)

        with open(
            os.path.join(BUILD_FOLDER_PATH, f"Pulumi.{self.stack_name}.yaml"), "w"
        ) as f:
            yaml.dump(pulumi_dev_yaml, f, default_flow_style=False)
