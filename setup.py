# setup.py

from setuptools import setup

setup(
        name='pixelwizard',
        version='0.1.0',
        author='andrithstef',
        description='A simple image editor',
        packages=['pixelwizard'],
        entry_points={
            'console_scripts': [
                'pixelwizard = pixelwizard.main:main'
                ]
            }
        )