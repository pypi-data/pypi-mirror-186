"""Connect to and download ESRI services.

Bulk querying and downloading of geometric data hosted on an ESRI FeatureService, MapService or ImageServer. When the Service is private, authentication is attempted using saved credentials in the project file.
"""

__all__ = ["get_data", "generate_token"]

import geopandas as gpd, requests, esridump, esridump.errors, yaml
import typing, subprocess, logging, os

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


def get_data(url: str, projection: int = 2193, verbose: bool = False, assume_data_type: str = "Feature Layer") -> gpd.GeoDataFrame:
    """Query an ESRI service and return data.
    
    The main function to call to return an ESRI REST MapServer, FeatureService or ImageServer. The url is verified to ensure a layer number is within the url, and gathers any query parameters that were added in the url. An automatic attempt is made to see if the Service contains vector or raster geometry, and thhe appropiate downloading methodology is chosen.
    
    Args:
        url: String of the ESRI Service. E.g. https://services7.arcgis.com/NNoivt2IKUC8czGf/arcgis/rest/services/NZTA_One_Road/FeatureServer/1.
        projection: Integer of the CRS that the data should be returned in.
        verbose: Display progress of the downloading procedure and assumptions made if verbose=True. Otherwise, logging is kept to errors or above.
        assume_data_type: If the automatic attempt of determining the type of the Service fails, the assume_data_type is used instead. Hence, assume_data_type should either be: "Feature Service" or "Raster Layer".

    Returns:
        For vector Services, a geopandas.GeoDataFrame (for vector data) is returned.
    
    Raises:
        NotImplementedError: Raised if the Service is a MapServer or ImageServer.
    """
    
    # Verify the given endpoint is okay
    url, query_parameters = _check_url(url)
    # Check the type of data of the endpoint so we know which method to download as
    response = requests.get(url + '?f=json')
    if response.ok:
        results = response.json()
        data_type = results.get("type", None)
        if not data_type and 'pixelType' in results:
            data_type = "Raster Layer"
        elif not data_type:
            data_type = assume_data_type
    else:
        data_type = assume_data_type

    if data_type == "Feature Layer":
        # Grab the features using the esridumps package and return as a GeoDataFrame
        return _download_vector_endpoint(url, query_parameters, projection, verbose)

    elif data_type == "Raster Layer":
        # Return the server as an numpy array?
        return _download_raster_endpoint(url, query_parameters, projection)


def _check_url(url: str) -> typing.Tuple[str, dict]:
    """Ensure the url is valid.

    Check to see if the given url was valid by ensuring it is correctly formatted with the layer number if it is a MapServer or FeatureSever.

    Args: 
        url: String of the ESRI Service. E.g. https://services7.arcgis.com/NNoivt2IKUC8czGf/arcgis/rest/services/NZTA_One_Road/FeatureServer/1.
    
    Returns:
        The verified url and a dictionary of query parameters. If not query parameters are were in the original url, then the defaul query parameters are returned.
    """

    # Check to see if there are query parmeters already in the given end_point_url
    if 'query?' in url:
        # Drop the url part
        query_parameters_str = url[url.index('query?'):].replace("query?", "")
        # Build a dictionary of key:values for each parameter
        query_parameters = {}
        for query_combo in query_parameters_str.split("&"):
            query_parameters[query_combo.split("=")[0]] = query_combo.split("=")[1]
        if "%3D" in query_parameters.get("where", ""):
            query_parameters["where"] = query_parameters["where"].replace("%3D", "=")
        if "f" in query_parameters:
            del query_parameters["f"]
        # Set the url as everything before the query parameters
        url = url[:url.index('query?')]
    else:
        # Set as default query parameters
        query_parameters = {'where': '1=1', 'outFields': '*'}
    
    if not url.endswith('/'):
        # Map Server URL needs a slash at the end
        url += '/' 
    
    if url.endswith("FeatureServer/") or url.endswith("MapServer/"):
        logger.error(f"A Layer number for {url} was not given. Please choose from the following:")
        response = requests.get(url+"?f=json")
        if response.ok:
            results = response.json()
            layers = results.get("layers", [])
            if len(layers) > 0:
                # There are layers so ask the user which one to download
                for layer in layers:
                    print(f"Layer {layer['id']}:\t{layer['name']} ({layer['geometryType'].replace('esriGeometry', '')})")
                layer_number_is_acceptable = False
                while not layer_number_is_acceptable:
                    layer_number = input("What is the Layer Number you wish to download? ")
                    try:
                        layer_number = int(layer_number)
                        url += f"{layer_number}/"
                        layer_number_is_acceptable = True
                    except:
                        print(f"{layer_number} is not an acceptable input. Please input an integer (e.g. 1, 6, 9).")
                        pass
            else:
                logger.error(f"No Layers could be found at the given endpoint server ({url}).\n ERROR {response.status_code}: {response.reason}")
                return
        else:
            logger.error(f"The endpoint server could not be queried to find the available Layers. Please check the enpoint URL ({url}) exists.\n ERROR {response.status_code}: {response.reason}")
            return 

    return url, query_parameters


def _download_vector_endpoint(url: str, query_parameters: dict, projection: int, verbose: bool) -> gpd.GeoDataFrame:
    """
    Return an ESRI REST FeatureService Layer (which contains vector geometries) as a GeoDataFrame. The most efficient way of downloading the Layer, given the host's configurations, is chosen based on https://github.com/openaddresses/pyesridump#methodology.
    """

    if not verbose:
        # Shut the logger from spitting out shit by force setting to ERROR level
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.ERROR, datefmt='%Y-%m-%d %H:%M:%S', force=True)
 
    try:
        # Try downloading the data and see if we get stopped
        endpoint_data = gpd.GeoDataFrame.from_features(list(esridump.EsriDumper(url=url, outSR=projection, request_geometry=True, extra_query_args=query_parameters, pause_seconds=0, timeout=120))).set_crs(projection, inplace=True)
    
    except esridump.errors.EsriDownloadError as error:
        if "Token Required" in str(error):
            # Then we have an endpoint that requires authentication. The best way to generate a token is using the Arcpy package that is only available in the arcgispro virtual environment
            arcgis_venv_path = r'C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe'
            if not os.path.exists(arcgis_venv_path):
                raise RuntimeError("Unfortunately, a token is required and you do not have ArcGIS Pro installed on this device. We are unable to generate a token, so please move onto a device that has ArcGIS installed.")

            # Get the login details from a saved file
            credentials_savepath = os.path.join(os.getcwd(), "config", "esri.yaml")
            if os.path.exists(credentials_savepath):
                credentials = yaml.load(credentials_savepath)
            else:
                print("No credentials could be found for this project.")
                credentials = {
                    "username": input("What is your Esri login username? "),
                    "password": input("What is your Esri login password? ")
                }
                os.makedirs(credentials_savepath, exist_ok=True)
                yaml.dump(credentials, open(credentials_savepath, "w"))
            
            # Generate a token in this script which outputs the token in the stdout
            res = subprocess.run([arcgis_venv_path, __file__, "token", credentials["username"], credentials["password"]], capture_output=True)
            if res.returncode == 0:
                query_parameters.update({"token": res.stdout.decode()})
                try:
                    endpoint_data =  gpd.GeoDataFrame.from_features(list(esridump.EsriDumper(url=url, outSR=projection, request_geometry=True, extra_query_args=query_parameters, pause_seconds=0, timeout=120))).set_crs(projection, inplace=True)
                except esridump.errors.EsriDownloadError as error2:
                    # Token failed to fix the error.
                    raise esridump.errors.EsriDownloadError(f"The generated token did not fix the EsriDownloadError, albeit it said a token was required. Please address the new error: \n{error2.reason}")
            
            else:
                # Token failed to be made. This should never happen but leave a catch clause in here. 
                raise esridump.errors.EsriDownloadError(f"{url} requires authentication. However, the automatically generated token led to a further issue when trying to be created: \n{res.reason}")
        else:
            raise error
    
    except Exception as error:
        # Catch all other errors
        raise error

    if not verbose:
        # Return logger to INFO level
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S', force=True)
    
    return endpoint_data


def _download_raster_endpoint(url: str, query_parameters: dict, projection: int) -> None:
    """
    Return an ESRI REST MapService Layer (which contains raster information).
    """
    # url = "https://gisimagery.ecan.govt.nz/arcgis/rest/services/Elevation/Latest_DEM/ImageServer"
    raise NotImplementedError("Sorry, rasters aren't ready yet!")


def generate_token(username: str, password: str) -> str:
    """Generate a token.
    
    Generate a token using Esri login details. This must be run in an virtual environment (typically 'arcgispro') where the arcgis package is available.
    
    Args:
        username: The username to connect to ESRI
        password: The password to connect to ESRI

    Returns:
        A valid ESRI token  
    """
    import arcgis.gis
    return arcgis.gis.GIS("https://www.arcgis.com/", username, password)._con.token


if __name__ == "__main__":
    import sys
    if sys.argv[2] == "token":
        sys.stdout.write(generate_token(sys.argv[3], sys.argv[4]))