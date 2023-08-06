"""Connect to Linux servers.

Connect to Linux servers to execute terminal commands, as well as uploading files and/or whole directories to the server.
"""

__all__ = ["Server"]

import paramiko, os, tqdm, warnings, zipfile, tempfile, glob, logging
from typing import Union

class Server(object):
    """
    A Class of a SSH and SFTP client that can execute commands on any Linux server and send files.
    """
    def __init__(self, nickname: str) -> None:
        """Initilise the class.

        Create a SSH and SFTP client with a server. The server nickname must be saved in your UI configuration file, otherwise you will be asked to authenticate yourself.

        Args:
            nickname: The nickname of the server that is saved in the UI configuration file.
        """
        client = paramiko.SSHClient()
        from uintel import config, save_config
        try:
            servers = config["servers"]
            credentials = servers[nickname]
        except KeyError:
            warnings.warn(f"Unfortunately, {nickname} is not in your saved servers.")

            credentials = {
                "address": input(f"What is the address for {nickname}? (e.g. 173.42.60.98) "),
                "username": input(f"What is your username for {nickname}? "),
                "ssh_key": input(f"Do you use a SSH key to connect to {nickname}? (yes/no) ").lower() == "yes"
                }
            if not credentials["ssh_key"]:
                credentials["password"] = input(f"Since you have indicated you do not use a SSH key for {nickname}, what is your password? ")
            else:
                credentials["password"] = None
            
            # Save this new connection to the UI configuration file
            config["servers"][nickname] = credentials
            save_config(config)

        log_level = logging.root.level
        logging.basicConfig(level=logging.ERROR, force=True)
        try:
            if credentials["ssh_key"]:
                # Set it to automatically add the host to known hosts
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname=credentials["address"], username=credentials["username"])
            else:
                client.connect(hostname=credentials["address"], username=credentials["username"], password=credentials["password"])
        except paramiko.SSHException as error:
            raise paramiko.SSHException(f"Unfortunately, your credentials could not be verified. Connection to {credentials['address']} ({nickname}) failed.\n{error}")
        
        self.client = client
        self.sftp_client = client.open_sftp()
    
        logging.basicConfig(level=log_level, force=True)


    def close(self) -> None:
        """Close the connection.
        
        Close the SSH and SFTP connections with the server.
        """
        self.client.close()
        self.sftp_client.close()


    def execute_command(self, command: str, capture_output: bool = False) -> Union[None, tuple]:
        """Execute a command.

        Args:
            command: The command to execute in the server's terminal.
            capture_output: if True, return the output from the command (stdin, stdout, stderr).
        
        Returns:
            The stdin, stdout and stderr if capture_output=True.
        """
        # Execute the command
        stdin, stdout, stderr = self.client.exec_command(command)
        
        error = ''
        for line in stderr.readlines():
            error += line
        if error:
            warnings.warn(f"The command: {command} could not be executed due to: \n{error}")
    
        if capture_output:
            return stdin, stdout, stderr


    def upload_file(self, local_path: str, remote_path: str, show_progress: bool = True, perm: int = 775, group: str = "www-data") -> None:
        """Upload a file.

        Upload a local file to the given remote filepath on the server.

        Args:
            local_path: Filepath to be uploaded.
            remote_path: Filepath on the server to upload to.
            show_progress: If True, show a progress bar as the file uploads.
            perm: The integer of the permissions to update the file with, e.g. 775.
            group: The group to assign the file to.
        """
        def print_progress(transferred, toBeTransferred):
            transferred = round(transferred/1e6, 2) # in MB now
            toBeTransferred = round(toBeTransferred/1e6, 2) # in MB now
            print(f"Progress: {100*transferred/toBeTransferred:.2f}%\t Transferred: {transferred:.2f} / {toBeTransferred:.2f} MB", end="\n" if transferred/toBeTransferred == 1 else "\r")
        
        # Check the directory specified exists
        if not os.path.exists(local_path):
            raise FileNotFoundError(f"The file {local_path} does not exists.")

        # Make sure a directory exists and the old file is deleted
        self.execute_command(f"mkdir {os.path.dirname(remote_path)}")
        self.execute_command(f"rm -f {remote_path}", show_output=True)

        _ = self.sftp_client.put(local_path, remote_path, callback=print_progress if show_progress else None, confirm=True)
        
        if perm:
            self.execute_command(f'chmod {perm} {remote_path}')
        if group:
            self.execute_command(f'chgrp {group} {remote_path}')


    def upload_directory(self, local_directory: str, remote_directory: str, show_progress: bool = True, perm: int = 775, group: str = "www-data") -> None:
        """Upload an entire folder to the server.

        Zip a directory (or a portion using glob notation) and upload it to the remote filepath on the server and uncompress it.

        Args:
            local_directory: The path to the folder to upload. This can also be a glob pattern (e.g. "data/**/*.csv") where a filter is applied. 
            remote_directory: The path on the server to upload to.
            show_progress: If True, show a progress bar as the file uploads.
            perm: The integer of the permissions to update the file with, e.g. 775.
            group: The group to assign the file to.
        """    

        if "*" not in local_directory:
            # Convert normal path to glob notation to get everything underneath
            base_directory = local_directory
            local_directory = os.path.join(local_directory, "*")
        else:
            base_directory = local_directory[:local_directory.index("*")]

        all_files = [fp for fp in glob.glob(local_directory, recursive=True) if os.path.isfile(fp)]
        
        if len(all_files) == 0:
            raise RuntimeError(f"No files matching: {local_directory} were found.")
        
        # Make the zip file
        temp_dir = tempfile.TemporaryDirectory()
        local_path = os.path.join(temp_dir.name, "zipped_dir.zip")
        with zipfile.ZipFile(local_path, "w", compression=zipfile.ZIP_DEFLATED) as zip:
            for filepath in tqdm.tqdm(all_files, "Creating ZIP file", total=len(all_files), leave=False, dynamic_ncols=True):
                zip.write(filepath, arcname=os.path.relpath(filepath, base_directory))

        # Upload the zip file
        remote_path = f"{remote_directory if remote_directory.endswith('/') else remote_directory + '/'}zipped_dir.zip"
        self.upload_file(local_path, remote_path, show_progress, perm, group)
        # Unzip and overwrite on the server
        self.execute_command(f"unzip -q -o {remote_path} -d {remote_directory}")
        # Delete the zip files on the server and local path
        self.execute_command(f"rm {remote_path}")
        temp_dir.cleanup()
        
        if perm:
            self.execute_command(f'chmod -R {perm} {remote_directory}')
        if group:
            self.execute_command(f'chgrp -R {group} {remote_directory}')
