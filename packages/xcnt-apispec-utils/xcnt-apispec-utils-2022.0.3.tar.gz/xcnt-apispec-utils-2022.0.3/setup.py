import os
import sys
from typing import Dict, List

from setuptools import find_namespace_packages, setup

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 8)
EGG_NAME = "xcnt-apispec-utils"


def list_packages(source_directory: str = "src") -> List[str]:
    packages = list(find_namespace_packages(source_directory, exclude="venv"))
    return packages


def list_namespace_packages(source_directory: str = "src") -> List[str]:
    if len(list_packages(source_directory=source_directory)) > 0:
        return ["xcnt", "xcnt.apispec"]
    else:
        return []


def get_package_dir() -> Dict[str, str]:
    if not os.path.isdir("src"):
        return {}
    return {"": "src"}


__version__ = "2022.0.3"
requirements = [
    "apispec>=3,<7",
]
webframeworks_requirements = ["apispec-webframeworks>=0.5.2,<2"]
flasgger_requirements = ["flasgger>=0.9.5,<1"]
sqlalchemy_search_requirements = ["xcnt-sqlalchemy-search>=2021"]
marshmallow_enum_requirements = ["marshmallow-enum"]
all_requirements = [
    *webframeworks_requirements,
    *flasgger_requirements,
    *sqlalchemy_search_requirements,
    *marshmallow_enum_requirements,
]
test_requirements = [
    "apispec-webframeworks>=0.5.2,<2",
    "apispec>=3,<7",
    "black>=19.3b0",
    "coverage>=7.0.5,<8",
    "factory-boy>=2.12.0,<4",
    "flake8>=6,<7",
    "flasgger>=0.9.5,<1",
    "marshmallow-enum",
    "mypy>=0.961",
    "pre-commit>=2.2.0,<3",
    "pytest-cases>=3.6.13,<4",
    "pytest-mock>=3.1.0,<4",
    "pytest==7.2.1,<8",
    "python-dateutil>=2.8,<3",
    "python-dotenv>=0.10",
    "python-semantic-release>=7.19.2,<8",
    "types-setuptools",
    "xcnt-sqlalchemy-search>=2023.2.0",
]


setup(
    name=EGG_NAME,
    version=__version__,
    python_requires=">={}.{}".format(*REQUIRED_PYTHON),
    url="https://github.com/xcnt/apispec-utils",
    author="XCNT Dev Team",
    author_email="dev-infra@xcnt.io",
    description="Helper functionality for providing OpenAPI documentation",
    long_description="",
    license="Internal",
    packages=list_packages(),
    package_dir=get_package_dir(),
    include_package_data=True,
    install_requires=requirements,
    tests_require=test_requirements,
    extras_require={
        "test": test_requirements,
        "webframeworks": webframeworks_requirements,
        "flasgger": flasgger_requirements,
        "sqlalchemy-search": sqlalchemy_search_requirements,
        "marshmallow-enum": marshmallow_enum_requirements,
        "all": all_requirements,
    },
    zip_safe=False,
    entry_points={},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={"GitHub": "https://github.com/xcnt/apispec-utils"},
    namespace_packages=list_namespace_packages(),
)
