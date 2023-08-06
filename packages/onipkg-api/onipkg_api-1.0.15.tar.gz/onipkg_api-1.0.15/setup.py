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
    version='1.0.15',
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
        'cachetools==5.2.0',
        'certifi==2022.9.24',
        'charset-normalizer==2.1.1',
        'google-api-core==2.10.1',
        'google-api-python-client==2.63.0',
        'google-auth==2.12.0',
        'google-auth-httplib2==0.1.0',
        'googleapis-common-protos==1.56.4',
        'httplib2==0.20.4',
        'idna==3.4',
        'numpy==1.23.3',
        'pandas==1.5.0',
        'protobuf==4.21.7',
        'pyasn1==0.4.8',
        'pyasn1-modules==0.2.8',
        'pyparsing==3.0.9',
        'python-dateutil==2.8.2',
        'pytz==2022.2.1',
        'requests==2.28.1',
        'rsa==4.9',
        'six==1.16.0',
        'uritemplate==4.1.1',
        'urllib3==1.26.12',
    ],
    # https://pypi.org/classifiers/
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
)
