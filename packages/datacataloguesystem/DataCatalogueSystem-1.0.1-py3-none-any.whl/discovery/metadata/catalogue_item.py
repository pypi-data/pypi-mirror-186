import uuid
from typing import Iterable

import pandas as pd
from pandas.api.types import is_numeric_dtype

from discovery.metadata.catalogue_metadata import CatalogueMetadata, ColMetadata, NumericColMetadata, \
    CategoricalColMetadata
from discovery.utils.data_handling.catalogue_data import CatalogueData


class CatalogueItem:
    """Catalogue item abstraction used to organise data into more understandable sets"""

    def __init__(
            self,
            metadata: CatalogueMetadata,
            data: CatalogueData
    ):
        self._metadata = metadata
        self._data = data
        self._id = uuid.uuid4()

    def get_id(self) -> uuid:
        """return the UUID ID of this catalogue item

        Returns:
            The UUID of the class as a UUID object
        """
        return self._id

    def update_tags(self, tag_update: dict):
        """Updates the tags that have been assigned to this catalogue item

        WARNING: overwrites previous values

        Args:
            tag_update (dict): A dictionary of {tag_name: tag_value}

        Returns:
            None
        """
        self._metadata.tags.update(tag_update)

    def get_data(self, rows: int | None = None) -> pd.DataFrame | Iterable[pd.DataFrame]:
        """Return a generator for the data

        Use lower row counts to preserve memory, and higher row counts for more efficient reading
        If the row amount is not specified, return the entire dataframe
        Args:
            rows: The amount of rows to generate on each iteration

        Returns: A generator of the dataframe, returning the amount of rows specified each time

        """
        data_generator = self._data.get_data(rows)
        if rows is None:
            return next(data_generator)
        return data_generator

    def get_checksum(self, update=True):
        """Return a checksum for the given dataframe

        Allows for abstracting checksum calculations into the reader itself
        If update is set to True, the checksum needs to be rebuilt,
        not rebuilding the checksum can be used for static data
        """
        return self._data.get_checksum(update=update)


    def get_metadata(self) -> CatalogueMetadata:
        """Return the metadata for this catalogue item

        Returns: A CatalogueMetadata object
        """
        return self._metadata

    def write_metadata(self) -> dict:
        """Return the metadata as a json compatible object

        Returns: A dictionary representation of the metadata
        """
        return {
            f"{str(self.get_id())}": {
                "data_handling": self._data.get_manifest(),
                "tags": {
                    name: value
                    for name, value in self._metadata.tags.items()
                },
                "columns": {
                    column_name: _write_metadata_column(column)
                    for column_name, column in self._metadata.columns.items()
                }
            }
        }

    def rebuild_metadata_object(self):
        """This method rebuilds all metadata that is reliant on the dataframe
        TODO: currently unable to read dataframe as chunks

        Metadata being regenerated is as follows:
        - data_checksum
        - data size
        - number of rows
        - column metadata

        This method can be used for when data gets updated, or the checksum does not match the loaded data
        Returns: None
        """
        dataframe: pd.DataFrame = self.get_data()
        column_metadata = {}
        for column in dataframe.columns:
            column_metadata[column] = resolve_metadata_column(column, dataframe[column])

        self._metadata = CatalogueMetadata(
            item_id=self.get_id(),
            data_manifest=self._data.get_manifest(),
            columns=column_metadata,
            tags=self._metadata.tags
        )


def resolve_metadata_column(name: str, series: pd.Series) -> ColMetadata:
    """Creates column metadata based on a column name, and column values
    Args:
        name: The name of the column
        series: The series to be evaluated

    Returns: A Col Metadata object
    """
    continuity = series.nunique() / series.count()
    if is_numeric_dtype(series):
        return NumericColMetadata(name, series.dtype, continuity, *get_series_statistical_values(series))
    return CategoricalColMetadata(name, series.dtype, continuity)


def _write_metadata_column(column: ColMetadata):
    """Return a column as a json compatible object"""
    return {
        "name": column.name,
        "attributes": column.get_attributes(stringify=True),
        "relationships": [{
            "certainty": relationship.certainty,
            "target_hash": relationship.target_hash,
            "target_column_name": relationship.target_column_name
        } for relationship in column.relationships]
    }


def get_series_statistical_values(series: pd.Series):
    """If the column is numeric, get statistics on it

    Args:
        series: A numeric pandas series

    Returns: A tuple of the following:
                The average (mean) value of the column
                The minimum value of the column
                The maximum value of the column
                The probability that the column represents continuous data

    """
    return (
        series.mean(),
        series.min(),
        series.max()
    )
