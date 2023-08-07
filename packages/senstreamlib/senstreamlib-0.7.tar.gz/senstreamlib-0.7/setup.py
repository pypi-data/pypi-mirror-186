from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.9'
DESCRIPTION = 'Python package for managing and interacting with Resensys SenSpots.'
LONG_DESCRIPTION = """
<img src="https://resensys.net:8443/static/images/resensys-logo-hollow.bmp" alt="resensys" width="300"/>

# SenStream (v 0.1.8)

[![GitHub releases](https://img.shields.io/github/release/greenbone/PROJECT.svg)](2.1)
[![PyPI release](https://img.shields.io/pypi/v/PROJECT.svg)](2.1)

**SenStream** is a python package for managing and interacting with Resensys SenSpot devices. Streamline data flows from SenSpot technologies and high-level data pipelines with this high-level software development kit.

At a high level, the SenStream project is designed to bridge the gap between the structural/civil engineer and the software developer for **structural health monitoring** and other scientific applications. This package comes equipped with the following features for SenSpot management, custom time streams, and state-of-the art time series machine learning tools:

#### API Functionality

*   Extract and configure SenSpot parameters.
*   Pull time streams from SenSpots from the cloud
*   Push custom time streams to the cloud with `stream_builder` module
*   Assign and configure custom email/SMS alerts
*   Setup custom and automated report generation
*   Stream real-time data in laboratory environment with `lab_streamer` module
*   Time-series analysis/model training (regression, classification, clustering, anomaly detection, etc.)

<br>
<img src="https://www.resensys.com/images/load-rating-app-note.png" alt="resensys_arch" width="700"/>

## Installation

#### Requirements

We recommend that you have a version of python >= 3.7 installed on your machine before proceeding. If the below `pip` command does not automatically install `pandas` and `numpy`, you should make sure that these libraries have been installed before proceeding.

#### Install using pip

To start using SenStream install using pip:

    pip install senstream

`pip` is the de facto and recommended package-management system written in Python and is used to install and manage software packages. It connects to an online repository of public packages, called the [Python Package Index](https://pypi.org/).

Note the `pip` refers to the Python 3 package manager. In environment where Python 2 is also available the correct command may be `pip3`.

## Getting Started

The following demonstrates what you need to get started with a connection to the Resensys cloud and check that you can extract data.



```
# import the necessary libraries and modules
import numpy as np
import pandas as pd

from senstream.resensys import Resensys,Sensors
from senstream.senspot import SenSpot

# for users with SenScope license, specify username and password
username,password = "test_user","user_password" 

# create a client connection to resensys.net
client = Resensys(username,password)

# create Sensors object to check all sensors in present account
sensors = Sensors(client)

# get list of all devices in the client account as pandas dataframe
sensor_df = sensors.getSensors(format="dataframe")

# print list of all the sensors in the account
print(sensor_df['DID'].tolist())
```

## Support

For any question on the usage of PROJECT please use the [Resensys Community Portal](). If you found a problem with the software, please [create an issue](https://github.com/resensys/PROJECT/issues) on GitHub. If you are a Greenbone customer, you may alternatively or additionally forward your issue to the Resensys Support Portal.

## Maintainer

This project is maintained by [Tom Wade](https://www.linkedin.com/in/thomas-shane-wade/) at Resensys, LLC.

## Contributing

Your contributions are highly appreciated. Please [create a pull request](https://github.com/greenbone/PROJECT/pulls) on GitHub. Bigger changes need to be discussed with the development team via the [issues section at GitHub](https://github.com/greenbone/PROJECT/issues) first.

State here if contributions are welcome. State the requirements a contribution should meet to get merged.

Details about development, like creating a dev environment or running tests, also belong here, for example:

For development, you should use [pipenv](https://pipenv.readthedocs.io/en/latest/) to keep your Python packages separated in different environments. First install pipenv via pip

    pip install --user pipenv

Afterwards run

    pipenv install --dev

in the checkout directory of PROJECT (the directory containing the Pipfile) to install all dependencies including the packages only required for development.

If there are more specific suggestions for development or guidelines for contributions, consider sending an email to thomas.wade@resensys.com.


## License

Copyright (C) 2022 [Resensys, LLC.](https://www.resensys.com/index.html)

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
"""

# Setting up
setup(
    name="senstream",
    version=VERSION,
    author="Resensys (Tom Wade)",
    author_email="<thomas.wade@resensys.com>",
    description='Python package for managing and interacting with Resensys SenSpots.',
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['mysql-connector-python', 'numpy', 'pandas', 'datetime','requests'],
    keywords=['python', 'stream', 'senspot', 'resensys', 'time series'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

from setuptools import setup

setup(
    name="senstreamlib",
    version="0.7",
    author="Tom Wade",
    author_email="thomas.wade@resensys.com",
    description="Resensys Python SDK for building SenSpot Data Pipelines and Time Series Analysis Tools.",
    packages=['senstream'],
    python_reqires=">=3.7",
)