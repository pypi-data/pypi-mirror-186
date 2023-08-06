# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="pascal-voc-analyser",
    version="1.0.0",
    description="Pascal VOC XML annotation format analysis library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Aman Khatri",
    author_email="amankhatri.ai@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["pascal_voc_analyser"],
    include_package_data=True,
    install_requires=["dict2xml==1.7.2", "pytest==7.2.1", "xmltodict==0.13.0"]
)