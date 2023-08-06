from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='svers',
    version='2.0',
    packages="s",
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)