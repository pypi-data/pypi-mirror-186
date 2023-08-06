from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import logging
import time
from typing import List

import pytest

from blazetest.core.config import CWD, MAX_LAMBDA_WORKERS
from blazetest.core.lambda_config import LambdaConfig
from blazetest.core.lambda_function import Lambda

logger = logging.getLogger(__name__)


class NodeIDCollector:
    node_ids: List[str] = []

    def pytest_collection_modifyitems(self, items):
        self.node_ids = [item.nodeid for item in items]


class TestsRunnerFacade:
    """
    Facade class for running tests using Lambda functions.
    This class is responsible for collecting the test items,
    creating the report paths, and invoking the Lambda functions.

    Attributes:
        pytest_args (List[str]): List of arguments to pass to pytest.
        config (LambdaConfig): Configuration for running the tests on AWS Lambda.
        lambda_function (Lambda):  Object responsible for interacting with AWS Lambda.

    Methods:
        run_tests(): Collects the test items, creates the report paths,
            and invokes the Lambda functions.
    """

    FOLDER_NAME_TIMESTAMP = "%Y-%m-%d_%H-%M-%S"
    TMP_REPORT_FOLDER = "/tmp/junitxml/{}.xml"
    REPLACE_SYMBOLS = ["::", ".", "/"]
    REPLACE_TO = "-"

    def __init__(self, pytest_args: List[str], config: LambdaConfig):
        """
        Initializes the class with the given pytest arguments,
        config and creates a new Lambda object.

        :param pytest_args: List of arguments to pass to pytest.
        :param config: Configuration for running the tests on AWS Lambda.
        """
        self.pytest_args = pytest_args
        logger.info(f"Pytest args initiated: {pytest_args}")

        self.config = config
        logger.info(f"Config initialized: {self.config}")

        self.lambda_function = Lambda(
            region=self.config.aws_region,
            stack_name=config.deploy.stack_name,
        )

    def run_tests(self):
        """
        Collects the test items, creates the report paths,
        and invokes the Lambda functions in parallel.
        """
        node_ids = self.__collect_tests()
        logger.info(f"Collected tests: {node_ids}")

        timestamp = self.__get_timestamp_now()

        function_details = self.lambda_function.get_created_lambda_function_details()
        function_name = function_details["function_name"]
        s3_bucket = function_details["s3_bucket"]

        logger.info(f"Function name: {function_name}, S3 Bucket: {s3_bucket}")

        def invoke_lambda(node_id: str):
            logger.info(f"Invoking Lambda with node_id: {node_id}")
            report_path = self.__get_pytest_xml_report_path(node_id=node_id)
            pytest_args = self.pytest_args + [f"--junitxml={report_path}"]
            return self.lambda_function.invoke(
                function_name=function_name,
                node_id=node_id,
                pytest_args=pytest_args,
                report_path=report_path,
                timestamp=timestamp,
            )

        s = time.time()
        with ThreadPoolExecutor(max_workers=MAX_LAMBDA_WORKERS) as executor:
            results = list(executor.map(invoke_lambda, node_ids))
            tests_passed = results.count(True)

        logger.info(
            f"Reports have been saved to s3://{s3_bucket}/{timestamp}/target/junitxml/"
        )
        logger.info(f"Time taken to execute {len(node_ids)} tests: {time.time() - s}")
        logger.info(f"Tests passed: {tests_passed} out of {len(node_ids)}")

        return tests_passed

    @staticmethod
    def __collect_tests() -> List[str]:
        collector = NodeIDCollector()
        pytest.main([CWD, "--collect-only"], plugins=[collector])
        return collector.node_ids

    def __get_timestamp_now(self):
        return datetime.now().strftime(self.FOLDER_NAME_TIMESTAMP)

    def __get_pytest_xml_report_path(self, node_id: str) -> str:
        for symbol in self.REPLACE_SYMBOLS:
            node_id = node_id.replace(symbol, self.REPLACE_TO)

        return self.TMP_REPORT_FOLDER.format(node_id)
