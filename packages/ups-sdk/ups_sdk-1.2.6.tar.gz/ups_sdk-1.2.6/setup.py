from setuptools import setup, find_packages
from ups_sdk import __version__
# The version of this tool is based on the following steps:
# https://packaging.python.org/guides/single-sourcing-package-version/

setup(
    name="ups_sdk",
    author="Esat Yılmaz",
    author_email="esatyilmaz3500@gmail.com",
    description="UPS Sdk",
    version=__version__,
    packages=find_packages(where=".", exclude=["tests"]),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.9",
    ],
)
