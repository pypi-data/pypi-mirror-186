# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="avenieca-python",
    version="0.1.0",
    description="Python SDK for AveniECA",
    url="https://github.com/aveni-hub/avenieca-python",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Ogban Ugot",
    author_email="ogbanugot@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["avenieca", "avenieca/producers"],
    include_package_data=True,
    install_requires=["kafka-python", "numpy"],
)
