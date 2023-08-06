import ftplib
import os
from typing import List

import paramiko


class BotFTPPlugin:
    def __init__(self, hostname: str, username: str = None, password: str = None) -> None:
        """
        Connect to an FTP server.
        If no username and password are passed, anonymous will be used by default.

        Args:
            hostname (str): The host used in the connection.
            username (str, optional): The username to login.
            password (str, optional): The password to login.
        """
        self._ftp_server = ftplib.FTP(hostname)
        self._ftp_server.login(username, password)

    def upload_file(self, file_path: str) -> None:
        """
        Upload a file to the current folder.

        Args:
            file_path (str): The path of the file to be uploaded.
        """
        file_name = os.path.basename(file_path)
        with open(file_path, "rb") as file:
            self._ftp_server.storbinary(f"STOR {file_name}", file)

    def download_file(self, file_name: str, destination_folder: str) -> None:
        """
        Download a file from the current folder using the file name.

        Args:
            file_name (str): The name of the file to be downloaded.
            destination_folder (str): The path of the folder where the file will be saved.
        """
        file_path = os.path.join(destination_folder, file_name)
        with open(file_path, "wb") as file:
            self._ftp_server.retrbinary(f"RETR {file_name}", file.write)

    def rename_file(self, from_name: str, to_name: str) -> None:
        """
        Rename a file on the server.

        Args:
            from_name (str): The current file name/path.
            to_name (str): The new file name/path.
        """
        self._ftp_server.rename(from_name, to_name)

    def delete_file(self, file_name: str) -> None:
        """
        Delete a file on the server.

        Args:
            file_name (str): The name/path of the file to be deleted.
        """
        self._ftp_server.delete(file_name)

    def get_current_directory(self) -> str:
        """
        Get the current working directory.

        Returns:
            str: The path of the current directory.
        """
        return self._ftp_server.pwd()

    def set_current_directory(self, dir_path: str) -> None:
        """
        Change to the specified directory.

        Args:
            dir_path (str): The name/path of the directory.
        """
        self._ftp_server.cwd(dir_path)

    def create_directory(self, dir_path: str) -> str:
        """
        Create a new directory on the server.

        Args:
            dir_path: The name/path of the directory to be created.

        Returns:
            str: The full path of the created directory.
        """
        dir_path = self._ftp_server.mkd(dir_path)
        return dir_path

    def remove_directory(self, dir_path: str) -> None:
        """
        Remove a directory on the server.

        Args:
            dir_path (str): The name/path of the directory to be removed.
        """
        self._ftp_server.rmd(dir_path)

    def list_files(self) -> None:
        """
        Prints the files and folders presents in the current folder.
        """
        self._ftp_server.dir()

    def get_files_list(self) -> List[str]:
        """
        Get the list of all file and folder names in the current working directory.

        Returns:
            List[str]: The list with the name of the files.
        """
        return self._ftp_server.nlst()

    def disconnect(self) -> None:
        """
        Close the connection with the server.
        """
        self._ftp_server.quit()


class BotSFTPPlugin:
    def __init__(self, hostname: str, port: int = 22, username: str = None, password: str = None) -> None:
        """
        Connect to an SFTP server over a SSH session.

        Args:
            hostname (str): The host used in the connection.
            port (int): The port to use in the connection. Defaults to 22.
            username (str): The username to login.
            password (str): The password to login.
        """
        self._transport = paramiko.Transport((hostname, port))
        self._transport.connect(username=username, password=password)
        self._sftp_server = paramiko.SFTPClient.from_transport(self._transport)

    def upload_file(self, file_name: str, destination_path: str = None) -> None:
        """
        Upload a file to a destination folder in the server.

        Args:
            file_name (str): The local file to be uploaded.
            destination_path (str): The path of the folder where the file will be saved.
                Defaults to the current working directory.
        """
        if not destination_path:
            destination_path = self.get_current_directory()

        filename = os.path.basename(file_name)
        file_path = os.path.join(destination_path, filename)

        self._sftp_server.put(file_name, file_path)

    def download_file(self, file_name: str, destination_folder: str) -> None:
        """
        Download a file from the server.

        Args:
            file_name (str): The name/path of the file to be downloaded.
            destination_folder (str): The path of the folder where the file will be saved.
        """
        filename = os.path.basename(file_name)
        file_path = os.path.join(destination_folder, filename)

        self._sftp_server.get(file_name, file_path)

    def rename_file(self, from_name: str, to_name: str) -> None:
        """
        Rename a file on the server.

        Args:
            from_name (str): The current file name/path.
            to_name (str): The new file name/path.
        """
        self._sftp_server.rename(from_name, to_name)

    def delete_file(self, file_name: str) -> None:
        """
        Delete a file on the server.

        Args:
            file_name (str): The name/path of the file to be deleted.
        """
        self._sftp_server.remove(file_name)

    def get_current_directory(self) -> str:
        """
        Get the current working directory.

        Returns:
            str: The path of the current directory.
        """
        cwd = self._sftp_server.getcwd()
        if not cwd:
            return "/"
        return cwd

    def set_current_directory(self, dir_path: str) -> None:
        """
        Change to the specified directory.

        Args:
            dir_path (str): The name/path of the directory.
        """
        self._sftp_server.chdir(dir_path)

    def create_directory(self, dir_path: str) -> None:
        """
        Create a new directory on the server.

        Args:
            dir_path: The name/path of the directory to be created.
        """
        self._sftp_server.mkdir(dir_path)

    def remove_directory(self, dir_path: str) -> None:
        """
        Remove a directory on the server.

        Args:
            dir_path (str): The name/path of the directory to be removed.
        """
        self._sftp_server.rmdir(dir_path)

    def get_files_list(self) -> List[str]:
        """
        Get the list of all file and folder names in the current working directory.

        Returns:
            List[str]: The list with the name of the files.
        """
        return self._sftp_server.listdir()

    def disconnect(self):
        """
        Close the connection with the server.
        """
        self._sftp_server.close()
