from setuptools import find_packages, setup
from pathlib import Path

setup(
    name='polarity-pde',
    version='0.1.0',
    license="CC BY 4.0",
    author='Tom Bland',
    author_email='tom_bland@hotmail.co.uk',
    packages=find_packages(),
    install_requires=['numpy',
                      'matplotlib',
                      'scipy',
                      'ipywidgets',
                      'jupyter'],
    description='Tools for simulating one-dimensional cell polarity PDE models and performing parameter space analysis'
)
