# Blazetest

## Introduction

CLI tool which allows developers to deploy their _pytest_ tests to AWS Lambda and run them in parallel.<br><br>
It automates the deployment process and makes it easier to run tests on the number of Lambda 
function instances in an **efficient and cost-effective manner**. <br><br>
CLI supports parallel execution of tests, as well as customizing the number of 
concurrent Lambda functions that can be used for your tests (up to 1000 unreserved concurrency). <br><br> 
Additionally, it provides real-time feedback on the progress of your tests, making it easy to know when the 
tests have finished running.<br><br>
Whenever the testing have been finished, you can get your ```junit-xml``` reports in the 
S3 bucket, allowing you to easily integrate it with any CI/CD workflow.

## Installation

In order to install the CLI, use pip:

`pip install blazetest`

Installation requires following packages to be installed:

```
click
pytest
PyYAML
dacite
boto3
aws-sam-cli
```

## Configuration

In order to configure the CLI, the YAML file is used. By default, `blazetest` uses _blazetest.yaml_ file located at the project root. 
However, any location can be used with specifying `--config-path` option while running CLI. Example:

`blazetest --config-path /path/to/yaml/file.yaml -v -s`

Here you can see the example `blazetest.yaml` file:

```
aws_region: "eu-west-1" # required, AWS region, which is used to deploy the application 

build:
  ecr_repository_name: "my-example-repository" # required, ECR repository name, used to create ECR repository, where the Docker image with tests is deployed

deploy:
  stack_name: "example-stack-name" # required, CloudFormation stack name, which is used for deployment, will be part of the names of the created stacks
  s3_bucket: "example-bucket" # required, S3 Bucket which will be used for deploying AWS Lambda
  s3_prefix: "example-prefix" # S3 Bucket prefix name, the folder which will be used within S3 bucket (default: service)
```

### To run the CLI tool, AWS credentials should be configured.

The CLI tool uses following AWS services:

**AWS Lambda** (creates and invokes Lambda)<br>
**AWS S3** (creates buckets and uploads files)<br>
**AWS ECR** (creates repository and uses it for Lambda invocations)<br>

## Usage

In order to use the CLI tool, following format should be used:

`blazetest [OPTIONS] [PYTEST ARGS]`

For example:

`blazetest --config-path --license-key license-key-1234 /path/to/yaml/file.yaml -vv -s`

In the example above, you can see that `--config-path` and `--license-key` 
relates to _CLI options_ whereas `--v -s` relates to _pytest args_.

**_Available options:_**

`--config-path`: configuration file path, defaults to blazetest.yaml file which is located at project root folder.<br>
`--license-key`: license key, should be set if license-file not specified<br>
`--license-file`: license file, should be set if license-key not specified<br>
`--aws-access-key-id`: AWS access key ID<br>
`--aws-secret-access-key`: AWS secret access key<br>

For pytest args, please see the usage examples in the pytest documentation: https://docs.pytest.org/en/6.2.x/usage.html. <br>
_You don't need to indicate `--junitxml` flag as it will be defined automatically._

## Workflow


Whole workflow consists of five main parts: **build, deployment, collecting tests, AWS Lambda parallel invocation, 
collecting results**.

1) The Docker image is built, local project files copied to image. [1]
2) Image is deployed to ECR repository. AWS Lambda function, S3 bucket (for test reports) are created using SAM.
3) Tests are collected locally.
4) Each test invokes separate AWS Lambda function in parallel.
5) All test XML reports are saved to S3 bucket.

[1] - Local projects are collected at the root folder of the project. Every file and folder will be copied. 
If you don't want certain files to be deployed to Lambda, please include them in `.dockerignore` in the root directory

![workflow](https://i.ibb.co/f8kqH8G/Web-App-Reference-Architecture-4.png)
![workflow](https://i.ibb.co/CwX292h/2-2.png)

_There is 1000 unreserved concurrency by default in AWS Lambda, so we can have 1000 AWS Lambda 
instances running at the same time by default. To gain more concurrent runs, you can:_<br>
1) Visit https://console.aws.amazon.com/servicequotas/home
2) Go to AWS Lambda -> Concurrent executions -> Request quota increase
3) For more information: https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html

## Selenium and WebDriver

To initialize webdriver, please use the indicated binary location and flags.

```
options = webdriver.ChromeOptions()

options.binary_location = "/usr/bin/chromium-1033/chrome-linux/chrome"

options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--single-process")

web_driver = webdriver.Chrome(options=options)
```

Above mentioned flags are required to have tests using selenium run smoothly on AWS Lambda instance.
