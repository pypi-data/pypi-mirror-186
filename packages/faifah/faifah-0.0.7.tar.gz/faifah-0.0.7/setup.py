
from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.7'
DESCRIPTION = 'DESCRIPTION'
LONG_DESCRIPTION = 'Open source for analysing electric power distribution system'

# Setting up
setup(
    name="faifah",
    version=VERSION,
    author="AKANIT KWANGKAEW",
    author_email="<akanitk84@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pypsa', 'numpy', 'pandas','colorama','termcolor'],
    # install_requires=[],
    keywords=['python', 'power system', 'voltage stability'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ]   
)
