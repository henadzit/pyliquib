"""
Pyliquib
========

See https://github.com/gtsarik/pyliquib for documentation.
"""
from setuptools import setup

setup(
    name='pyliquib',
    version='0.1.2',
    packages=['pyliquib', ],
    license='BSD',
    url='https://github.com/gtsarik/pyliquib',
    author='Henadzi Tsaryk',
    author_email='vare6gin@gmail.com',
    description='A MongoDB migration tool with pymongo inspired by Liquibase',
    long_description=__doc__,
    platforms='Any',
    install_requires=[
        'pymongo>=2'
    ]
)