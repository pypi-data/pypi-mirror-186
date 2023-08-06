# Always prefer setuptools over distutils
import re
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'justrpa', '__init__.py')) as f:
    VERSION = re.search('\n__version__ = "(.*)"', f.read()).group(1)

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(HERE, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

# This call to setup() does all the work
setup(
    name="justrpa",
    version=VERSION,
    description="Just RPA Common library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://justrpa.com/",
    author="JUSTRPA",
    author_email="jing.yan.cn@gmail.com",
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
    packages=find_packages('justrpa'),
    include_package_data=True,
    install_requires=REQUIREMENTS
)
