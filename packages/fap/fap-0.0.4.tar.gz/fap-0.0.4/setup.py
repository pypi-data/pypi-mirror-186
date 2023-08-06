from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.4'
DESCRIPTION = 'Apis'
LONG_DESCRIPTION = 'A package used to process images in deeplearning'

# Setting up
setup(
    name="fap",
    version=VERSION,
    author="sahil",
    author_email="sahilapte1@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['fastapi', 'deeplearning', 'keras', 'yolov5', 'sahil','segmentation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)