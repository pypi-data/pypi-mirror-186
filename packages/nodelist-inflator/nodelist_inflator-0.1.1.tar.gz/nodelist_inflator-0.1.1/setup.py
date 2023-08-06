#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_namespace_packages

setup(
    author="Zach Nussbaum",
    author_email="zanussbaum@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        "console_scripts": [
            "nodelist_inflate=nodelist_inflator.nodelist_infate:cli",
        ]
    },
    description="Expands hostnames/nodelists",
    license="MIT license",
    include_package_data=True,
    keywords="nodelist_inflator, slurm, hostnames",
    name="nodelist_inflator",
    packages=find_namespace_packages(include=["nodelist_inflator", "nodelist_inflator.*"]),
    url="https://github.com/zanussbaum/nodelist-inflator",
    version="0.1.1",
    zip_safe=False,
)
