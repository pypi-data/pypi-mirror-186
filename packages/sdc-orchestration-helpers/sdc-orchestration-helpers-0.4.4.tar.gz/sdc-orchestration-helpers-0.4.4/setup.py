"""
    Set up the sdc_helpers package
"""
from setuptools import setup, find_packages


def get_required(file_name):
    """
    Get Required Filename during setup
    """
    with open(file_name):
        return file_name.read().splitlines()


setup(
    name="sdc-orchestration-helpers",
    packages=find_packages(exclude=("tests")),
    install_requires=[
        "PyYaml",
        "sdc_helpers",
        "flatten_dict",
        "boto3>=1.16.63",
        "sagemaker",
    ],
    extras_require={
        "airflow1": ["apache-airflow==1.10.12"],
        "airflow2": ["apache-airflow>=2.1.4"],
    },
    description="A package of orchestration helpers and utilities for sdc orchestration i.e AIRFLOW.",
    version="0.4.4",
    url="https://github.com/RingierIMU/sdc-global-orchestration-helpers",
    author="Ringier South Africa",
    author_email="tools@ringier.co.za",
    keywords=["pip", "helpers", "airflow", "orchestration"],
    download_url="https://github.com/RingierIMU/sdc-global-orchestration-helpers/archive/v.0.4.4.zip",
)
