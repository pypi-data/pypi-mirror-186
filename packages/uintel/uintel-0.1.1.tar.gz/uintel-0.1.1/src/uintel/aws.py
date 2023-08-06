"""
Connecting and utilising Amazon Web Services (AWS).

This module allows easy uploading to and downloading from S3 buckets. More importantly as data caching is enabled for some dashboards, versioning is taken care of by removing previous versions and updating the versions.json file on S3. 

"""

__all__ = ["upload_file_to_S3", "download_file_from_S3", "update_S3_versions", "remove_previous_versions", "get_S3_client"]

import boto3, json, os, tqdm, threading, tempfile
from typing import Optional


def create_aws_client(service: str, region: str = "ap-southeast-2") -> boto3.client:
    """Create an AWS client.

    Return an AWS client connected to one service by using the credentials file at ~/.aws/credentials.

    Args:
        service: Which AWS service to connect to. E.g. 's3'.
        region: The AWS region to connect to.
    
    Returns:
        A boto3.client connected to the requested AWS service and region.
    
    """
    try:
        return boto3.client(service, region_name=region)
    except Exception as error:
        print("""\033[91mFor first-timers, be sure to generate a credentials file as ~/.aws/credentials with the following information:
        [default]
        aws_access_key_id = ********
        aws_secret_access_key = ***********\n    
        If that does not fix this, then please investigate the following error\033[0m""")
        raise error


def upload_file_to_S3(local_filepath: str, remote_filepath: str, s3_client: boto3.client = create_aws_client('s3'), bucket: str = "urbanintelligencedevdata") -> None:
    """Upload a file to an AWS S3 bucket.

    Upload a file at local_filepath to the remote_filepath in a given AWS S3 bucket. 
    
    Args:
        local_filepath: Filepath that is to be uploaded.
        remote_filepath: Filepath to put the file in the AWS S3 bucket. The remote_filepath should be in the format: '/data/project_name/version/filename' like 'data/mrapple/1.4.5/growth_statistics.csv'.
        s3_client: A boto3.client that is connected to the S3 service.
        bucket: The AWS S3 bucket to upload the file to.
    
    Returns:
        None.
    """
    s3_client.upload_file(local_filepath, bucket, remote_filepath, Callback=_ProgressBar(local_filepath))


def download_file_from_S3(remote_filepath: str, local_filepath: str, s3_client: boto3.client = create_aws_client('s3'), bucket: str = "urbanintelligencedevdata") -> None:
    """Download a file from an AWS S3 bucket.

    Download a file at remote_filepath to the local_filepath from a given AWS S3 bucket. 

    Args:
        remote_filepath: Filepath in the AWS S3 bucket to download. The remote_filepath should be in the format: '/data/project_name/version/filename' like 'data/mrapple/1.4.5/growth_statistics.csv'.
        local_filepath: Filepath where the downloaded file should be saved.
        s3_client: A boto3.client that is connected to the S3 service.
        bucket: The AWS S3 bucket to upload the file to.
    
    Returns:
        None.
    """
    s3_client.download_file(bucket, remote_filepath, local_filepath)


def update_S3_versions(project_name: str, dev_version: Optional[str] = None, test_version: Optional[str] = None, prod_version: Optional[str] = None) -> None:
    """Update the data/version.json file with new versioning.

    Edit the data/versions.json file on the S3 bucket to the new versions provided for each domain (dev/test/prod) on a given project_name. If ther project_name is not in versions.json, it is added.

    Args:
        project_name: Project name in versions.json to update/add.
        dev_version: Version to update the development dashboard to. E.g. '1.9.2', '2023_12_18', 'v1.2.8'. If dev_version=None, the current will remain unchanged.
        test_version: Version to update the testing dashboard to. E.g. '1.9.2', '2023_12_18', 'v1.2.8'. If test_version=None, the current will remain unchanged.
        prod_version: Version to update the production dashboard to. E.g. '1.9.2', '2023_12_18', 'v1.2.8'. If prod_version=None, the current will remain unchanged.

    Returns:
        None.
    """

    # Create a temporary directory to download version.json in
    tempdir = tempfile.TemporaryDirectory()
    tempfile_name = os.path.join(tempdir.name, "versions.json")

    # Download the current versions.json file
    s3_client = create_aws_client('s3')
    download_file_from_S3("data/versions.json", tempfile_name, s3_client)

    # Read the file and make the necessary changes as requested
    with open(tempfile_name, "r") as file:
        versions = json.load(file)

    if dev_version:
        versions[project_name]["dev"] = dev_version
    if test_version:
        versions[project_name]["test"] = test_version
    if prod_version:
        versions[project_name]["production"] = prod_version

    with open(tempfile_name, "w") as file:
        json.dump(versions, file)

    # Upload the modified versions.json to the bucket
    upload_file_to_S3(tempfile_name, "data/versions.json", s3_client)
    s3_client.close()
    
    tempdir.cleanup()


def remove_previous_versions(project_name: str, current_version: str, bucket: str = "urbanintelligencedevdata") -> None:
    """Delete all versions (excluding the current) from a project.

    Delete ALL files and folders (except the current_version) for a given project_name from the given AWS S3 bucket.

    Args:
        project_name: Project name in versions.json to update/add.
        current_version: Current version of the project to keep to. E.g. '1.9.2', '2023_12_18', 'v1.2.8'.
        bucket: The AWS S3 bucket to remove the previous versions from.

    Returns:
        None.
    """

    # Get all the subfolders and objects within this project folder
    s3_client =  create_aws_client('s3')
    result = s3_client.list_objects(Bucket=bucket, Prefix=f"data/{project_name}/", Delimiter='/')
    version_folders = [version_folder.get('Prefix') for version_folder in result.get('CommonPrefixes')]
    s3_client.close()

    # Obviosuly, we should not delete the folder with the new data in it!
    version_folders.remove(f"data/{project_name}/{current_version}/")

    # The client can tag objections for deletion, but can't go ahead with it. Hence, use the Bucket Resource.
    bucket_client = boto3.resource('s3').Bucket(bucket) ### boto3.resource is not be supported soon. Better find a way around this before it happens
    for version_folder in version_folders:
        bucket_client.objects.filter(Prefix=version_folder).delete()
    

class _ProgressBar(object):
    """Display the progress of an uploading file.

    Using a tqdm progress bar, indicate the progress of an uploading file. This is to be used in the Callback function as the ProgressBar class will be updated on each call.

    Attributes:
        None.
    """
    
    def __init__(self, filename: str):
        """Initialises ProgressBar to be zero."""
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()
        self.pbar = tqdm.tqdm(desc=f"Uploading {filename}", total=100, leave=False, dynamic_ncols=True)

    def __call__(self, bytes_uploaded: float):
        """Update the progress bar with the bytes_uploaded and refresh the percentage bar."""
        with self._lock:
            self._seen_so_far += bytes_uploaded
            self.pbar.n = round((self._seen_so_far / self._size) * 100, 2)
            self.pbar.refresh()