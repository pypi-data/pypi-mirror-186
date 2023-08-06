from distutils.core import setup
from setuptools import find_packages
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    # Project name:
    name='onipkg_api',
    # Packages to include in the distribution:
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    # Project version number:
    version='1.0.16',
    # List a license for the project, eg. MIT License
    license='',
    # Short description of your library:
    description='Helper para consumo de APIs',
    # Long description of your library:
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Your name:
    author='Lucas Heilbuth Nazareth de Sousa',
    # Your email address:
    author_email='lucasheilbuth@yahoo.com.br',
    # Link to your github repository or website:
    url='https://github.com/LucasHeilbuth',
    # Download Link from where the project can be downloaded from:
    download_url='https://github.com/Onimusic/oni_api_helper.git',
    # List of keywords:
    keywords=['onimusic'],
    # List project dependencies:
    install_requires=[
        'cachetools',
        'certifi',
        'charset-normalizer',
        'google-api-core',
        'google-api-python-client',
        'google-auth',
        'google-auth-httplib2',
        'googleapis-common-protos',
        'httplib2',
        'idna',
        'numpy',
        'pandas',
        'protobuf',
        'pyasn1',
        'pyasn1-modules',
        'pyparsing',
        'python-dateutil',
        'pytz',
        'requests',
        'rsa',
        'six',
        'uritemplate',
        'urllib3',
    ],
    # https://pypi.org/classifiers/
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
)
