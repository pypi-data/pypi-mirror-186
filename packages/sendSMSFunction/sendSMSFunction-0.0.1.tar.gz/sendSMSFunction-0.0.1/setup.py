from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A test for hello'
LONG_DESCRIPTION = 'A basic thing.'

# Setting up
setup(
    name="sendSMSFunction",
    version=VERSION,
    author="Mito (Mito Khoza)",
    author_email="<emito@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description='long_description',
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)