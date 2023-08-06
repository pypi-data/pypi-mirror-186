"""@Author: Rayane AMROUCHE

Local Sources Handling.
"""

import os

from typing import Any

import paramiko  # type: ignore

from dsmanager.datamanager.datasources.datasource import DataSource

from dsmanager.datamanager.utils._func import find_type
from dsmanager.datamanager.datastorage import DataStorage


class SshSource(DataSource):
    """Inherited Data Source Class for ssh sources."""

    schema = DataStorage(
        {
            "source_type": "ssh",
            "server": "ssh_server_address",
            "port": 21,
            "username_env_name": "ssh_username_environment_variable_name",
            "password_env_name": "ssh_password_environment_variable_name",
        }
    )

    @staticmethod
    def read_source(
        server: str,
        port: int,
        username_env_name: str,
        password_env_name: str,
        path: str,
        **kwargs: Any
    ) -> Any:
        """Ftp source reader.

        Args:
            server (str): Server address.
            port (int): Port of the server.
            username_env_name (str): Name of the username env variable.
            password_env_name (str): Name of the password env variable.
            path (str): Path of the file in the server.

        Returns:
            Any: Data from source.
        """
        user = os.getenv(username_env_name, "")
        passwd = os.getenv(password_env_name, "")

        try:
            transport = paramiko.Transport((server, port))
            transport.connect(None, user, passwd)
            engine = paramiko.SFTPClient.from_transport(transport)
        except paramiko.SSHException as _:
            engine = paramiko.SSHClient()
            engine.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            engine.connect(server, port=port, username=user, password=passwd)

        if path and isinstance(engine, paramiko.SFTPClient):
            file = engine.open(path)
            if "file_type" not in kwargs:
                kwargs["file_type"] = find_type(path)
            data = super(SshSource, SshSource)._encode_files(file, **kwargs)
            engine.close()
        else:
            data = engine
        return data

    def read(self, source_info: dict, **kwargs: Any) -> Any:
        """Handle source and returns the source data.

        Args:
            source_info (dict): Source metadatas.

        Returns:
            Any: Source datas.
        """
        args = self._setup_fileinfo(source_info, **kwargs)
        ssh_server = source_info["server"]
        ssh_port = source_info["port"]
        ssh_username = source_info["username_env_name"]
        ssh_password = source_info["password_env_name"]
        ssh_path = source_info["path"]

        data = self.read_source(
            ssh_server, ssh_port, ssh_username, ssh_password, ssh_path, **args
        )

        self.logger.info("Get '%s' from ssh server '%s'.", ssh_path, ssh_server)
        return data

    def read_db(self, source_info: dict, **kwargs: Any) -> Any:
        """Read source and returns an ssh source engine.

        Args:
            source_info (dict): Source metadatas.

        Raises:
            Exception: Raised if missing needed metadatas.

        Returns:
            Any: Source engine.
        """
        args = self._setup_fileinfo(source_info, **kwargs)

        engine = self.read_source(
            source_info["server"],
            source_info["port"],
            source_info["username_env_name"],
            source_info["password_env_name"],
            "",
            **args
        )

        self.logger.info("Connect to the ssh server '%s'.", source_info["server"])

        return engine
