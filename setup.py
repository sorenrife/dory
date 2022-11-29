"""
Setup project and PyPi package
"""
from setuptools import setup, find_packages
from pathlib import Path
import os

# read the contents of your README file
directory = Path(__file__).parent

setup(
    name="dory-cache",
    version=os.getenv("VERSION"),
    license="MIT",
    author="Sören Rifé",
    author_email="sorenrife@gmail.com",
    long_description=(directory / "README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages("dory"),
    package_dir={"": "dory"},
    python_requires=">=3.8",
    url="https://github.com/sorenrife/dory",
    keywords="dory smart cache",
    install_requires=["redis==4.3.3"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
