"""
A set of functions that will build catalogue items for us
Unfortunately it's hard to find a clean way to systematically attach json to data builders, our approach is to have
non backwards-compatible readers that are versioned for the current implementation of this file
"""
import copy
import json
import logging
from jsonschema import validate

from discovery.metadata.catalogue_item import CatalogueItem
from discovery.metadata.catalogue_metadata import CatalogueMetadata
from discovery.utils.data_handling.local_csv_handler import LocalCSVHandler
from discovery.utils.data_handling import data_size
from discovery.utils.data_handling.catalogue_data import *

logger = logging.getLogger(__name__)

# Ensure that versions remain consistent
BUILDER_VERSION = 1


def from_csv(
        path: str,
        dataframe_metadata: CatalogueMetadata = None
):
    """Construct a metadata object by providing a csv file"""
    data = LocalCSVHandler(path)
    if dataframe_metadata is None:
        # if no metadata is provided, build an empty one
        dataframe_metadata = CatalogueMetadata(data_manifest=data.get_manifest())
    return CatalogueItem(metadata=dataframe_metadata, data=data)


DICT_LOADERS = {
    "LocalCSVHandler": LocalCSVHandler,
    "default": CatalogueData
}
LOADER_DICTS = {val: key for key, val in DICT_LOADERS.items()}
DICT_DATA_SIZES = {
    "file": data_size.FileDataItemSize,
    "default": data_size.DataItemSize
}


def from_metadata_json(
        metadata_json_path: str
) -> [CatalogueItem]:
    """Construct a set of catalogue items from a json descriptor file
    For now, we can just re-run the loader
    """
    metadata_json = json.load(open(metadata_json_path))
    new_items = []

    for catalogue_pair in metadata_json:
        item_id, catalogue_json = list(catalogue_pair.items())[0]
        data_handling = catalogue_json['data_handling']

        new_metadata = CatalogueMetadata(
            item_id=item_id,
            data_manifest=copy.copy(data_handling),
            tags=catalogue_json['tags']
        )

        data_size_attributes = data_handling.pop('data_size')
        data_size_type = data_size_attributes.pop('size_representation', '')
        data_size_object = DICT_DATA_SIZES.get(data_size_type, data_size.DataItemSize)(**data_size_attributes)
        data_handler = DICT_LOADERS[data_handling.pop('loader', 'default')]
        new_data = data_handler(
            data_size=data_size_object,
            **data_handling
        )

        new_items.append(CatalogueItem(metadata=new_metadata, data=new_data))

    return new_items
