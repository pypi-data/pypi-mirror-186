from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'mrpythonlib'
LONG_DESCRIPTION = 'my first python library ever😉'

# Setting up
setup(
    name="mrpythonhello",
    version=VERSION,
    author="Bilal Ahmad",
    author_email="bilalahmad176176@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'mr python', 'area of figs', 'area', 'developergautam'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)