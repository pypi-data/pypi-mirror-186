from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'azka'
LONG_DESCRIPTION = 'A package to find area of different figures'

# Setting up
setup(
    name="azka",
    version=VERSION,
    author="azka rathor",
    author_email="azka.rathor1@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'Area_module', 'Volume_module', 'area', 'basic_mathOperation'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)