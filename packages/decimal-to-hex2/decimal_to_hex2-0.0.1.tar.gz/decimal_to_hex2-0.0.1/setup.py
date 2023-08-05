from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'decial_to_hex2'
LONG_DESCRIPTION = 'this libaray use to change the decimal to 2s complement of hexadecimal'

# Setting up
setup(
    name="decimal_to_hex2",
    version=VERSION,
    author="AliZain1214",
    author_email="zali83715@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['arithmetic', 'math', 'mathematics', 'python tutorial', 'avi upadhyay'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)