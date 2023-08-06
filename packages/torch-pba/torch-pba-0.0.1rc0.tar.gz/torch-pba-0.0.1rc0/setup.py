
import setuptools
import re
import os
import sys


setuptools.setup(
    name="torch-pba",
    version="0.0.1rc0",
    python_requires=">3.7.0",
    author="Michael E. Vinyard - Harvard University - Broad Institute - MGH",
    author_email="mvinyard@broadinstitute.org",
    url=None,
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="PyTorch implementation of PBA.",
    packages=setuptools.find_packages(),
    install_requires=[
        "torch>=1.12",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    license="MIT",
)
