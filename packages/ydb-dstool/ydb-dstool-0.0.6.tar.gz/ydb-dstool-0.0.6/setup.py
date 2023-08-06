# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="ydb-dstool",
    version="0.0.6",
    description="YDB Distributed Storage Administration Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yandex LLC",
    author_email="ydb@yandex-team.ru",
    url="https://github.com/ydb-platform/ydb/tree/main/ydb/apps/dstool",
    license="Apache 2.0",
    package_dir={"": "."},
    packages=setuptools.find_packages("."),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=(
        "protobuf>=3.13.0",
        "grpcio>=1.5.0",
        "packaging"
    ),
    entry_points={
        "console_scripts": [
            "ydb-dstool = ydb.apps.dstool.cli:main",
        ]
    }
)
