<div align="center">
  <img src="docs/images/blue_logo.svg"><br>
</div>

-----------------

# uintel: unified Python data analysis toolkit
[![PyPI Latest Release](https://img.shields.io/pypi/v/uintel.svg)](https://pypi.org/project/uintel/)
[![License](https://img.shields.io/pypi/l/uintel.svg)](https://github.com/uintel/pyui/blob/main/LICENSE)

## What is it?

**uintel** is a Python package that provides all the common-day functions and tools for analysts at Urban Intelligence Ltd. It aims to reduce re-using of generic code between similar projects, which leads to bug duplication and further security vulnerabilities. Building upon this, another mission of this package is to install Urban Intelligence's style guides by modifying the matplotlib installation and installing fonts. 


## Main Features

  - Easy uploading of files to Amazon Web Services S3 buckets, and appropriate versioning control for data cache handling
  - Creating colour palettes relating to Urban Intelligence's main products
  - Connecting (and creating) databases on postgreSQL servers, as well as uploading DataFrames to a database
  - Bulk querying (public and private) ESRI servers to download geometric data with attributes
  - Connecting to Linux servers (e.g. Piwakawaka) to execute terminal commands, as well as uploading files and/or whole directories to the server
  - Quickly send messages or files to a Slack channel or person
  - Calculate statistics of raster files over a polygon geometry ("zonal statistics")
  - Quickly convert a GeoDataFrame to a simplified topojson file

## Where to get it
The source code is currently hosted on GitHub at: [https://github.com/uintel/pyui](https://github.com/uintel/pyui)

Binary installers for the latest released version are available at the [Python Package Index (PyPI)](https://pypi.org/project/uintel) by running:

```sh
pip install uintel
```

## Configuration
Each time ```uintel``` is imported,

```py
import uintel as ui
```

all necessary installations shall begin that have not been completed before. This will include creating a configuration file, installing fonts and modifying matplotlib - if it has not been done so before.

If you have adjusted your computer and the UI defaults have altered, you can revert them by running:

```py
ui.reset_fonts()
ui.reset_styles()
ui.reset_config()
```

## Documentation
Documentation is available at [https://uintel.github.io/pyui/](https://uintel.github.io/pyui/)
