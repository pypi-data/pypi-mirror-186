from typing import Generator, Callable

import pandas as pd
from pandas.util import hash_pandas_object

from .data_size import DataItemSize


class CatalogueData:
    """Catalogue data abstraction which allows interaction with the data, ideally avoids storing data in memory"""
    checksum = None
    data_size: DataItemSize = DataItemSize()

    def get_manifest(self, update=True) -> dict:
        """Return a dictionary representation of the data that is being used"""
        return {
            "data_loader": "undefined",
            "data_size": self.get_data_size(update=update, json_representation=True)
        }

    def get_data_size(self, update=True, json_representation=False) -> DataItemSize | dict:
        """Return a representation of the data size, this is usually a row count and byte count,
        but for more complex data implementations it might have to be something more abstract

        if update is set to False, just use the one already made, but only if one has already been generated
        if json_representation is set to True, return a dictionary representation of the size instead
        """
        if update and self.data_size:
            self.data_size = DataItemSize()

        if json_representation:
            return self.data_size.get_attributes()
        return self.data_size

    def get_data(self, rows: int = None) -> Generator:
        raise NotImplemented

    def get_checksum(self, update=True) -> int:
        """Return a checksum for the given dataframe

        Allows for abstracting checksum calculations into the reader itself
        If update is set to True, the checksum needs to be rebuilt,
        not rebuilding the checksum can be used for static data
        """
        if update:
            dataframe = next(self.get_data())
            self.checksum = int(hash_pandas_object(dataframe).sum())
        return self.checksum
