import os
import re
from pathlib import Path
from setuptools import setup

# Set version as environment variable
semver_regex = re.compile(r'\d{1}.\d{1}.\d{1}')
if 'RELEASE_VERSION' not in os.environ:
    raise Exception('Set version as environment variable (e.g. export RELEASE_VERSION=1.0.0)')
version = os.getenv('RELEASE_VERSION')
match = semver_regex.search(version)
if match is None:
    raise Exception(f'Module version must follow semantic versioning format (e.g. v1.0.0). Provided: {version}')

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='wallaby_data_access',
    version=match.group(),
    description='Module for accessing WALLABY internal release data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AusSRC/WALLABY_data_access',
    author='Austin Shen',
    author_email='austin.shen@csiro.au',
    packages=['wallaby_data_access'],
    install_requires=[
        'numpy',
        'astropy',
        'astroquery',
        'matplotlib',
        'django',
        'django_extensions',
        'psycopg2-binary',
        'python-dotenv'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
    ]
)
