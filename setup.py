import os
import commands
from setuptools import find_packages
from distutils.core import setup

setup(
    name = 'Python-AA',
    version = commands.__version__,
    description = 'Python Ascii Art',
    author = 'ci11y',
    url = 'https://github.com/huyfififi/PyAA',
    packages = find_packages(),
    python_requires='>=3.7',
    install_requires=[],
    entry_points = {
        'console_scripts': [
            'pyaa = commands.pyaa:main',
        ]
    }
)
