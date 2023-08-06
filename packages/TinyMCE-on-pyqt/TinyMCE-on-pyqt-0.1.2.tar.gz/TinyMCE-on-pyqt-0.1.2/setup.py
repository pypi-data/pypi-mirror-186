#!/usr/bin/python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TinyMCE-on-pyqt",
    version="0.1.2",
    author="TimTu",
    author_email="ovo-tim@qq.com",
    description="在pyqt中方便的使用TinyMCE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ovo-Tim/TinyMCE-on-pyqt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)