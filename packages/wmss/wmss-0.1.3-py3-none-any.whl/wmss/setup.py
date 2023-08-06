from setuptools import setup

exec(open("wmss/_version.py").read())

setup(
    version=__version__)