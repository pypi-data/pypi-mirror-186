from setuptools import setup

setup(
    name='heartbit',
    version='0.1',
    packages=['heartbit'],
    install_requires=['boto3'],
    scripts=['heartbit/install.py'],
)
