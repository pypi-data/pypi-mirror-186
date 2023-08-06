from setuptools import setup
from setuptools import find_packages


VERSION = '0.1.4'

setup(
    name='larry_utils',  # package name
    version=VERSION,  # package version
    description='larry produced utils for projects',  # package description
    packages=find_packages(),
    zip_safe=False,
)
