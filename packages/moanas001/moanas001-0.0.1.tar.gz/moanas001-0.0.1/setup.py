from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'PythonTutorial'
LONG_DESCRIPTION = 'A package to find area of different figures'

# Setting up
setup(
    name="moanas001",
    version=VERSION,
    author="Muhammad Anas",
    author_email="msdsf21m533@pucit.edu.pk",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'logic gates','binary as string','speedometer'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)