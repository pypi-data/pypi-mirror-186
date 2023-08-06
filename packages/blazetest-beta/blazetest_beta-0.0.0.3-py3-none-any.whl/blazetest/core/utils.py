import logging
import os
import shutil
from pathlib import Path
from typing import List

from blazetest.core.config import BUILD_FOLDER_PATH, PWD, EXECUTABLE_FILES, CWD

logger = logging.getLogger(__name__)


def setup_logging(debug=False, stdout_enabled=True):
    level = logging.DEBUG if debug else logging.INFO
    if stdout_enabled:
        logging.basicConfig(
            format="%(process)d-%(levelname)s-%(message)s",
            level=level,
        )
    else:
        logging.basicConfig(
            filename=os.path.join(CWD, "blazetest.log"),
            format="%(process)d-%(levelname)s-%(message)s",
            level=level,
        )


def remove_junit_report_path(pytest_args: List[str]) -> List[str]:
    """Remove the `--junitxml` argument from a list of pytest arguments.

    Args:
        pytest_args: List of pytest arguments.

    Returns:
        List of pytest arguments with the `--junitxml` argument removed.
    """
    return [arg for arg in pytest_args if not arg.startswith("--junitxml")]


def set_aws_credentials(
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_region: str = None,
    s3_bucket: str = None,
    ecr_repository_name: str = None,
):
    """Set AWS credentials as environment variables.

    Args:
        aws_access_key_id: AWS access key ID.
        aws_secret_access_key: AWS secret access key.
        aws_region: AWS region.
        s3_bucket: S3 bucket name.
        ecr_repository_name: ECR repository name.
    """
    if aws_access_key_id:
        os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key_id

    if aws_secret_access_key:
        os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_access_key

    if aws_region:
        os.environ["AWS_DEFAULT_REGION"] = aws_region

    if s3_bucket:
        os.environ["S3_BUCKET"] = s3_bucket

    if ecr_repository_name:
        os.environ["ECR_REPOSITORY_NAME"] = ecr_repository_name

    os.environ["PROJECT_CWD"] = CWD
    os.environ["PULUMI_CONFIG_PASSPHRASE"] = "pass"


def create_build_folder() -> None:
    """Create a build folder and copy necessary files to it.

    The `__main__.py` file in the `deployment/aws` directory will also be copied
    to the build folder.
    """
    # Create build folder and necessary subdirectories
    Path(BUILD_FOLDER_PATH).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(BUILD_FOLDER_PATH, "scripts")).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(BUILD_FOLDER_PATH, "tests_runner_handler")).mkdir(
        parents=True, exist_ok=True
    )

    # Create list of source-destination file pairs for the files in EXECUTABLE_FILES
    src_dst_pairs = [
        (os.path.join(PWD, file), os.path.join(BUILD_FOLDER_PATH, file))
        for file in EXECUTABLE_FILES
    ]

    # Copy the files
    for src, dst in src_dst_pairs:
        shutil.copyfile(src=src, dst=dst)

    deployment_files = ["__main__.py", ".envignore", "requirements.txt"]
    for deployment_file in deployment_files:
        shutil.copyfile(
            src=os.path.join(PWD, f"deployment/aws/{deployment_file}"),
            dst=os.path.join(BUILD_FOLDER_PATH, deployment_file),
        )

    logger.info("Successfully created build folder")
