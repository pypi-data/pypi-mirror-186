"""@Author: Rayane AMROUCHE

Data Sources Handling.
"""

from typing import Any
from logging import Logger

import pandas as pd  # type: ignore

from dsmanager.datamanager.datastorage import DataStorage


class DataSource:
    """Data Source Class."""

    def __init__(self, logger: Logger) -> None:
        """Init a Data Source.

        Args:
            logger (Logger): Passed down logger from the Data Manager.
        """
        self.logger = logger

    _file_schema = DataStorage(
        {
            "file_type": "csv | excel | text | json | ...",
            "encoding": "utf-8",
            "args": {"pandas_read_file_argument_keyword": "value_for_this_argument"},
        }
    )

    @staticmethod
    def _setup_fileinfo(source_info: dict, **kwargs: Any) -> dict:
        DataSource._load_source(source_info, **kwargs)
        args = source_info["args"] if "args" in source_info else {}
        if "file_type" in source_info:
            args["file_type"] = source_info["file_type"]
        if "encoding" in source_info:
            args["encoding"] = source_info["encoding"]
        return args

    @staticmethod
    def _encode_files(
        file: Any, file_type: str = "csv", encoding: str = "utf-8", **kwargs: Any
    ) -> Any:
        data = None
        if file_type == "csv":
            data = pd.read_csv(file, **kwargs)
        elif file_type == "excel":
            data = pd.read_excel(file, **kwargs)
        elif file_type == "json":
            data = pd.Series(file)
        elif file_type == "text":
            with open(file, "r", encoding=encoding) as file_obj:
                data = file_obj.read()
        else:
            raise Exception("File type unknown or not supported.")
        return data

    @staticmethod
    def _load_source(source_info: dict, **kwargs: Any) -> None:
        if "args" not in source_info:
            source_info["args"] = {}
        source_info["args"].update(**kwargs)

    def read(self, source_info: dict, **kwargs: Any) -> None:
        """Read source and returns the source data.

        Args:
            source_info (dict): Source metadatas.

        Raises:
            NotImplementedError: Raised if missing needed metadatas.
        """
        DataSource._load_source(source_info, **kwargs)
        raise NotImplementedError("This source does not handle read.")

    def read_db(self, source_info: dict, **kwargs: Any) -> None:
        """Read source and returns a source engine.

        Args:
            source_info (dict): Source metadatas.

        Raises:
            NotImplementedError: Raised if missing needed metadatas.
        """
        DataSource._load_source(source_info, **kwargs)
        raise NotImplementedError("This source does not handle read_db.")
