import uuid
from typing import Iterable

import pandas as pd
import pandas.errors

from discovery.utils.data_handling.catalogue_data import CatalogueData
from discovery.utils.data_handling.data_size import *


class LocalCSVHandler(CatalogueData):
    def __init__(self, path, checksum: uuid.UUID = None, data_size: DataItemSize = None):
        # The specification to be used to replicate reading
        self.data_size = data_size
        self.checksum = checksum
        self.path = path

    def get_manifest(self, update=True) -> dict:
        """Return a json representation of the local CSV that can be used to pull the data again
        We use the checksum as part of this representation, as it can allow us to build a resiliency to path changes

        Note: we do not store any data on the filesystem, this allows replication across file systems
        """
        return {
            "loader": self.__class__.__name__,
            "checksum": self.get_checksum(),
            "path": self.path,
            "data_size": self.get_data_size(update=update, json_representation=True)
        }

    def get_data_size(self, update=False, json_representation=False) -> DataItemSize | dict:
        """Return a size based on the amount of rows and bytes in the data"""
        if update:
            dataframe = next(self.get_data())
            rows = dataframe.shape[0]
            byte_num = int(dataframe.memory_usage(index=True).sum())
            self.data_size = FileDataItemSize(
                no_of_rows=rows,
                no_of_bytes=byte_num
            )

        if json_representation:
            return self.data_size.get_attributes()
        return self.data_size

    def get_data(self, rows: int | None = None) -> pd.DataFrame | Iterable[pd.DataFrame]:
        """Return a generator for the data

        Use lower row counts to preserve memory, and higher row counts for more efficient reading
        Args:
            rows: The amount of rows to generate on each iteration

        Returns: A generator of the dataframe, returning the amount of rows specified each time

        """
        if rows is None:
            yield pd.read_csv(self.path)

        seek_row = 0
        header_df = pd.read_csv(self.path, skiprows=seek_row, nrows=rows)
        df_columns = header_df.columns
        yield header_df

        while True:
            seek_row += rows
            try:
                yield pd.read_csv(self.path, skiprows=seek_row, nrows=rows, usecols=df_columns)
            except pandas.errors.EmptyDataError:
                break
