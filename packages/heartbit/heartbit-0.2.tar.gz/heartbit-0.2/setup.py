from setuptools import setup

setup(
    name='heartbit',
    version='0.2',
    packages=['heartbit'],
    install_requires=['boto3'],
    scripts=['heartbit/install.py'],
    entry_points={
    'console_scripts': [
        'heartbit=heartbit.install:start_prometheus',
    ],
    }
)
