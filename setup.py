# setup.py

from setuptools import setup, find_packages

setup(
        name='pixelwizard',
        version='1.0.0',
        author='andrithstef',
        description='A simple image editor',
        packages=find_packages(include=['pixelwizard', 'pixelwizard.*']),
        install_requires=[
            'Pillow',
            'numpy',
            'scipy',
            "scikit-image"
            ],
        entry_points={
            'console_scripts': [
                'pixelwizard = pixelwizard.main:main'
                ]
            }
        )
