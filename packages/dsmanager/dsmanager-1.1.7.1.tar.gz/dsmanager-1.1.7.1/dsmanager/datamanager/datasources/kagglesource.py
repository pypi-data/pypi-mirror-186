"""@Author: Rayane AMROUCHE

Kaggle Sources Handling.
"""

import io
import zipfile

from typing import Any
from kaggle.api import KaggleApi  # type: ignore # pylint: disable=import-error

from tqdm import tqdm  # type: ignore

from dsmanager.datamanager.datasources.datasource import DataSource

from dsmanager.datamanager.utils._func import find_type
from dsmanager.datamanager.datastorage import DataStorage


class KaggleSource(DataSource):
    """Inherited Data Source Class for kaggle sources."""

    schema = DataStorage(
        {
            "source_type": "kaggle",
            "dataset": "User/Dataset",
            "file_name": "file_in_dataset",
            **DataSource.file_schema,
        }
    )

    @staticmethod
    def _unzip(res: bytes):
        str_res_temp = b""
        with zipfile.ZipFile(io.BytesIO(res)) as my_zip_file:
            for contained_file in my_zip_file.namelist():
                with my_zip_file.open(contained_file) as cur_zip:
                    for line in cur_zip.readlines():
                        str_res_temp += line
        str_res = io.StringIO(str_res_temp.decode("utf-8"))
        return str_res

    @staticmethod
    def _dataset_download_file(
        api: Any, dataset: str, file_name: str, chunk_size=1048576
    ) -> Any:
        if "/" in dataset:
            api.validate_dataset_string(dataset)
            response = api.process_response(
                api.datasets_download_file_with_http_info(
                    owner_slug=dataset.split("/")[0],
                    dataset_slug=dataset.split("/")[1],
                    file_name=file_name,
                    _preload_content=False,
                )
            )
        else:
            response = api.process_response(
                api.datasets_download_file_with_http_info(
                    owner_slug=api.get_config_value(api.CONFIG_NAME_USER),
                    dataset_slug=dataset,
                    file_name=file_name,
                    _preload_content=False,
                )
            )

        size = int(response.headers["Content-Length"])
        size_read = 0
        res = b""
        with tqdm(total=size, unit="B", unit_scale=True, unit_divisor=1024) as pbar:
            while True:
                data = response.read(chunk_size)
                if not data:
                    break
                res += data
                size_read = min(size, size_read + chunk_size)
                pbar.update(len(data))

        try:
            str_res = io.StringIO(res.decode("utf-8"))
        except UnicodeDecodeError as _:
            str_res = KaggleSource._unzip(res)
        return str_res

    @staticmethod
    def read_source(dataset: str, filename: str = "", **kwargs: Any) -> Any:
        """Kaggle source reader.

        Args:
            dataset (str): Dataset to look for.
            filename (str, optional): File of the dataset to load. Defaults to "".

        Returns:
            Any: Data from source.
        """
        api = KaggleApi()
        api.authenticate()
        if filename:
            file = KaggleSource._dataset_download_file(api, dataset, filename)
            if "file_type" not in kwargs:
                kwargs["file_type"] = find_type(filename)
            data = super(KaggleSource, KaggleSource).encode_files(file, **kwargs)
        else:
            data = api
        return data

    def read(self, source_info: dict, **kwargs: Any) -> Any:
        """Handle source and returns the source data.

        Args:
            source_info (dict): Source metadatas.

        Returns:
            Any: Source datas.
        """
        args = self.setup_fileinfo(source_info, **kwargs)
        data = self.read_source(
            source_info["dataset"], source_info["file_name"], **args
        )

        self.logger.info(
            "Get '%s' from kaggle's dataset '%s'.",
            source_info["file_name"],
            source_info["dataset"],
        )
        return data

    def read_db(self, source_info: dict, **kwargs: Any) -> Any:
        """Read source and returns a kaggle source engine.

        Args:
            source_info (dict): Source metadatas.

        Returns:
            Any: Source engine.
        """
        args = source_info["args"] if "args" in source_info else {}

        self.load_source(source_info, **kwargs)
        api = self.read_source("", "", **args)

        self.logger.info("Connect to kaggle.")

        return api
