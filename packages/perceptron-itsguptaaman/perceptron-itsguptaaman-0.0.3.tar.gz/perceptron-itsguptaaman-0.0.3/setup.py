import setuptools
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements() -> List[str]:

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace(
        "\n", "") for requirement_name in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PKG_NAME = "perceptron"
USER_NAME = "itsguptaaman"
PROJECT_NAME = "Perceptron_package"

setuptools.setup(
    name=f"{PKG_NAME}-{USER_NAME}",
    version="0.0.3",
    author=USER_NAME,
    author_email="itsamangupta420@gmail.com",
    description="A small package for perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "numpy==1.21.4",
        "pandas==1.3.4",
        "joblib==1.1.0"
    ]
)
