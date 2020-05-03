#!/usr/bin/env python
import sys
import os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))
about = {}
MODULE_NAME="its"
with open(os.path.join(here, MODULE_NAME, "__version__.py"), "r", encoding="utf8") as f:
    exec(f.read(), about)

with open("README.md", "r", encoding="utf8") as f:
    long_description = f.read()

class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name=MODULE_NAME,
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    packages=find_packages(),
    install_requires=[
        "Click==7.0",
        "tinydb==3.15.2",
        "pylint==2.4.4",
    ],
    tests_require=["pytest", "pytest_mock"],
    extras_require={
        'dev': [
            'pyinstaller'
        ]
    },
    cmdclass={"test": PyTest},
    scripts=["./bin/itscli"],
)
