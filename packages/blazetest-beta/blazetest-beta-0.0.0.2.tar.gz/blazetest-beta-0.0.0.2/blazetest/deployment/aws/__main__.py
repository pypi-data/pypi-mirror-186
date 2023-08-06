import base64
import json
import logging
import os
import random
import string
from typing import Dict

import pulumi
import pulumi_aws as aws
from pulumi_docker import DockerBuild, Image, ImageRegistry

logger = logging.getLogger(__name__)

ENVIGNORE = ".envignore"
CWD: str = os.environ.get("PROJECT_CWD")
BUILD_FOLDER_PATH = os.path.join(CWD, ".blazetest")
DOCKER_FILE_PATH = os.path.join(BUILD_FOLDER_PATH, "Dockerfile")

ECR_REPOSITORY_NAME = os.environ.get("ECR_REPOSITORY_NAME")
S3_BUCKET = os.environ.get("S3_BUCKET")


class Workflow:
    """
    The Workflow class is used to deploy an image to Amazon Elastic Container Registry (ECR)
    and an AWS Lambda function to an AWS CloudFormation stack.

    Attributes:
        ecr_repository_name (str): The name of the ECR repository to deploy the image to.
        s3_bucket_name (str): The name of the S3 bucket to use.
        stack_name (str): The name of the CloudFormation stack to deploy the Lambda function to.
        env_vars (Dict): A dictionary of environment variables to set for the Lambda function.

    Properties:
        ecr_repository (aws.ecr.Repository): The ECR repository object.
        lambda_function (aws.lambda_.Function): The Lambda function object.
        image (Image): The image object.
        s3_bucket (aws.s3.Bucket): The S3 bucket object.

    Methods:
        deploy(): Initializes the ECR repository, S3 bucket, image, and Lambda function, and deploys them.

        init_ecr_repository(): Initializes the ECR repository.
        init_s3(): Initializes the S3 bucket.
        init_image(): Initializes the image and builds it using Docker.
        init_lambda_function(): Initializes the Lambda function.

        get_lambda_iam_policy(): Retrieves IAM Policy for attaching to IAM Role
        get_lambda_iam_role(): Retrieves IAM Role for attaching to Lambda
        get_policy_attachment(): Attaches IAM Policy to IAM Role
    """

    ecr_repository: aws.ecr.Repository
    lambda_function: aws.lambda_.Function
    image: Image
    s3_bucket: aws.s3.Bucket

    def __init__(
        self,
        ecr_repository_name: str,
        s3_bucket_name: str,
        stack_name: str,
        env_vars: Dict,
    ):
        self.ecr_repository_name = ecr_repository_name
        self.s3_bucket_name = s3_bucket_name
        self.stack_name = stack_name
        self.env_vars = env_vars

    def deploy(self):
        self.init_ecr_repository()
        self.init_s3()
        self.init_image()
        self.init_lambda_function()

    def init_ecr_repository(self):
        self.ecr_repository = aws.ecr.Repository(
            self.ecr_repository_name,
            tags={"Name": self.ecr_repository_name},
        )

    def init_s3(self):
        self.s3_bucket = self.get_s3_bucket(bucket_name=self.s3_bucket_name)

    def init_image(self):
        image_name = self.ecr_repository.repository_url
        registry_info = self.ecr_repository.registry_id.apply(self.__get_registry_info)
        docker_build = DockerBuild(context=CWD, dockerfile=DOCKER_FILE_PATH)

        self.image = Image(
            name=f"{self.stack_name}-image",
            build=docker_build,
            image_name=image_name,
            registry=registry_info,
        )

    def init_lambda_function(self):
        iam_role = self.get_lambda_iam_role()
        iam_policy = self.get_lambda_iam_policy()

        role_policy_attachment = aws.iam.RolePolicyAttachment(
            f"{self.stack_name}-policy-attachment",
            role=iam_role.name,
            policy_arn=iam_policy.arn,
        )

        function_name = f"{self.stack_name}-ServiceTests"

        # env_vars = self.env_vars
        # env_vars.pop("S3_BUCKET")
        #
        # def get_env_vars_(bucket_id):
        #     return f"{bucket_id}"
        #
        # s3_bucket_id = self.s3_bucket.id.apply(get_env_vars_)

        self.lambda_function = aws.lambda_.Function(
            function_name,
            description="Lambda function for execution of PyTest tests in parallel",
            package_type="Image",
            image_uri=self.image.image_name,
            role=iam_role.arn,
            memory_size=4096,
            timeout=300,
            environment=aws.lambda_.FunctionEnvironmentArgs(
                variables={
                    "S3_BUCKET": self.s3_bucket.id,
                },
            ),
            opts=pulumi.ResourceOptions(
                depends_on=[
                    self.ecr_repository,
                    self.image,
                    self.s3_bucket,
                    role_policy_attachment,
                ],
            ),
        )

    def get_lambda_iam_policy(self) -> aws.iam.Policy:
        policy = self.s3_bucket.arn.apply(
            lambda arn: {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": [
                            "s3:PutObject",
                        ],
                        "Resource": f"{arn}/*",
                    }
                ],
            }
        )
        return aws.iam.Policy(
            resource_name=f"{self.stack_name}-policy",
            policy=policy,
        )

    def get_lambda_iam_role(self) -> aws.iam.Role:
        return aws.iam.Role(
            resource_name=f"{self.stack_name}-role",
            assume_role_policy=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {"Service": "lambda.amazonaws.com"},
                            "Action": "sts:AssumeRole",
                        }
                    ],
                }
            ),
        )

    @staticmethod
    def __get_registry_info(registry_id) -> ImageRegistry:
        """
        Generates authentication information to access the repository to build and publish the image.
        :param registry_id: Registry ID
        :return: pulumi_docker.ImageRegistry
        """
        credentials = aws.ecr.get_credentials(registry_id=registry_id)
        decoded = base64.b64decode(credentials.authorization_token).decode()

        parts = decoded.split(":")
        if len(parts) != 2:
            raise Exception("Invalid credentials")

        return ImageRegistry(credentials.proxy_endpoint, parts[0], parts[1])

    @staticmethod
    def get_s3_bucket(bucket_name: str) -> aws.s3.Bucket:
        return aws.s3.Bucket(bucket_name)

    @staticmethod
    def generate_random_string(length):
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


def get_env_vars():
    with open(ENVIGNORE, "r") as f:
        env_ignore = [line.strip() for line in f.readlines()]

    return {k: v for k, v in os.environ.items() if k not in env_ignore}


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(message)s",
    )
    environment_variables = get_env_vars()
    logger.debug(f"Environment variables: {environment_variables}")
    workflow = Workflow(
        ecr_repository_name=ECR_REPOSITORY_NAME,
        s3_bucket_name=S3_BUCKET,
        stack_name=pulumi.get_stack(),
        env_vars=environment_variables,
    )
    workflow.deploy()
