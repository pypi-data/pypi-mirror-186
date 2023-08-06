from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.4'
DESCRIPTION = 'Tools for analysis of the extracellular matrix'

# Setting up
setup(
    name="ecmanalysis",
    version=VERSION,
    author="Mohamed Ghafoor",
    author_email="<moeghaf@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['scanpy', 'anndata', 'scanorama', 'bbknn', 'leidenalg', 'xlrd==1.2.0'],
    keywords=['extracellular matrix', 'matrisome', 'spatial transcriptomics'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)