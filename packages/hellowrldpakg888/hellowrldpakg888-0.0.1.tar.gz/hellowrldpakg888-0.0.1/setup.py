from setuptools import setup, find_packages
#import codecs
#import os

VERSION = '0.0.1'
DESCRIPTION = 'Basic Hello World Package'

# Setting up
setup(
    name="hellowrldpakg888",
    version=VERSION,
    author="SMS",
    #author_email="<abcdef@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'helloworld'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)