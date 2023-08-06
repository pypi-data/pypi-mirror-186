from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'Does atoms helping and other utilities Im tired of copying'

# Setting up
setup(
    name="AtomsHelpersUtils",
    version=VERSION,
    author="Eric Chen",
    author_email="<ericchen@udel.edu>",
    description=DESCRIPTION,
    long_description="geom2graph takes atoms in an ASE atoms object and makes a graph from it using networkx",
    packages=find_packages(),
)
