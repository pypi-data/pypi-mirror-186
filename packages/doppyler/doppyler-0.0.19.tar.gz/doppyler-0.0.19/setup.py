#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = ["aiohttp"]

test_requirements = []

setup(
    author="Sandman Doppler",
    author_email="hi@paloaltoinnovation.com",
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="A library to interact with the Sandman Doppler Clock API",
    install_requires=requirements,
    include_package_data=True,
    keywords="doppyler",
    name="doppyler",
    packages=find_packages(include=["doppyler", "doppyler.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/pa-innovation/doppyler",
    version="0.0.19",
    zip_safe=False,
)
