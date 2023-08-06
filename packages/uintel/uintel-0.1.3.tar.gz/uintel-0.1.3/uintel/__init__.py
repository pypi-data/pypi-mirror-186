"""Urban Intelligence's collection of Python code for everyday use.

uintel is a Python package that provides all the common-day functions and tools for analysts at Urban Intelligence Ltd. It aims to reduce re-using of generic code between similar projects, which leads to bug duplication and further security vulnerabilities. Building upon this, another mission of this package is to install Urban Intelligence's style guides by modifying the matplotlib installation and installing fonts.

Main Features
    - Easy uploading of files to Amazon Web Services S3 buckets, and appropriate versioning control for data cache handling
    - Creating colour palettes relating to Urban Intelligence's main products
    - Connecting (and creating) databases on postgreSQL servers, as well as uploading DataFrames to a database
    - Bulk querying (public and private) ESRI servers to download geometric data with attributes
    - Connecting to Linux servers (e.g. Piwakawaka) to execute terminal commands, as well as uploading files and/or whole directories to the server
    - Quickly send messages or files to a Slack channel or person
    - Calculate statistics of raster files over a polygon geometry ("zonal statistics")
    - Quickly convert a GeoDataFrame to a simplified topojson file
"""

import uintel.install as _install

def reset_fonts() -> None:
    """Force re-install all fonts.

    Reinstalls all Urban Intelligence fonts back to defaults.

    Args: 
        None
    
    Returns:
        None
    
    Raises:
        None
    """
    _install._install_fonts(force=True, verbose=True)


def reset_styles() -> None:
    """Force re-install all matplotlib styles.
    
    Reinstalls all Urban Intelligence matplotlib styles (*.mplstyle files in /fonts) back to defaults.

    Args: 
        None
    
    Returns:
        None
    
    Raises:
        None

    """
    _install._install_styles(force=True, verbose=True)


def reset_config() -> None:
    """Force re-make the configuration file, in case at least one saved bit of information needs updating.
    
    Remakes the configuration file, regardless if it exists or is is up to date.

    Args: 
        None
    
    Returns:
        None
    
    Raises:
        None
    """
    _install._create_config_file()


def save_config(config: dict) -> None:
    """Save the configuration file.
    
    Saves the configuration to disk, regardless if it exists or is up to date.

    Args: 
        config: A dictionary of the Urban Intelligence configurations
    
    Returns:
        None
    
    Raises:
        None
    """
    _install._save_config(config)


_install._update_config_file()
_install._install_styles(force=False, verbose=True)
_install._install_fonts(force=False, verbose=True)
config = _install._get_config()

import uintel.aws as aws
import uintel.esri as esri
import uintel.figures as figures
import uintel.geometry as geometry
import uintel.server as server
import uintel.slack as slack
import uintel.sql as sql
__all__ = ["aws", "esri", "figures", "geometry", "server", "slack", "sql"]