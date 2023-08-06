from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Econometric',
    version='8.0',
    packages=["Econometric"],
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    include_package_data=True
)