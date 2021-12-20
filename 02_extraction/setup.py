import setuptools
from setuptools import setup

setuptools.setup(
    name="extract",
    version="0.1",
    packages=setuptools.find_packages(),
    install_requires=['Click',],
    entry_points='''
        [console_scripts]
        extract=extract.cli:cli
    ''',

)