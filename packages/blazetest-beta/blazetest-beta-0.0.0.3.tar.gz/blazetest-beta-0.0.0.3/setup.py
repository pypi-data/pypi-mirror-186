from setuptools import setup, find_packages

setup(
    name="blazetest-beta",
    version="0.0.0.3",
    author="Abrorjon Ruziboev",
    author_email="abror.ruzibayev@gmail.com",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={
        "blazetest": [
            ".dockerignore",
            "Dockerfile",
            "template.yaml",
            "scripts/install_chromedriver.sh",
            "deployment/aws/__main__.py",
            "deployment/aws/.envignore",
            "deployment/aws/requirements.txt",
        ],
    },
    install_requires=[
        "click",
        "pytest",
        "PyYAML",
        "dacite",
        "boto3",
        "licensing",
        "pulumi",
        "pulumi-aws",
        "pulumi-docker==3.1.0",
        "pyopenssl>=23.0.0; python_version >= '3.7'",
    ],
    entry_points={
        "console_scripts": [
            "blazetest=blazetest.runner:run_tests",
        ],
    },
)
