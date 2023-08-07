"""
Entrypoint to the discovery project
Reads a filesystem and tries to make some analysis based off of it
"""
import itertools
import json
import os

import yaml
import logging.config
from typing import Type

# set up local logging before importing local libs
# TODO: do this a better way
if __name__ == "__main__":
    with open('logging_conf.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    logger = logging.getLogger(__name__)

from discovery import metadata
from discovery.utils.visualizer import Visualizer
from discovery.data_matching.data_match_interface import DataMatcher
from discovery.data_matching.dataframe_matcher import DataFrameMatcher
from discovery.data_matching.matching_methods import *


class DiscoveryClient:
    def __init__(self, discovery_config: dict):
        self.config = discovery_config
        self.loaded_catalogue: dict[str:metadata.CatalogueItem] = {}
        self.visualiser = Visualizer()
        self.dataframe_matcher = DataFrameMatcher()

    def create_visual(self, pathname: str):
        """Build a visual based on stored metadata
        Args:
            pathname: The path to draw the visual

        Returns: None
        """
        # TODO: find a fancy python way to do this
        metadata_list = []
        for item in self.loaded_catalogue.values():
            metadata_list.append(item.get_metadata())
        self.visualiser.draw(metadata_list, pathname)

    def construct_relationships(self, methods: list[Type[DataMatcher]]):
        """Construct a set of relationships between columns in the dataframes
        Args:
            methods: A list of methods to use when constructing the relationships

        Returns: None
        """
        for item1, item2 in itertools.combinations(self.loaded_catalogue.values(), 2):
            self._match_metadata(item1, item2, methods)

    def _match_metadata(self, origin_item: metadata.CatalogueItem, target_item: metadata.CatalogueItem, methods):
        """Run the dataframe matcher with the two given dataframes
        Update the metadata to reflect the changes
        """
        # TODO: paged matching for large dataframes
        origin_data = origin_item.get_data()
        target_data = target_item.get_data()
        origin_metadata = origin_item.get_metadata()
        target_metadata = target_item.get_metadata()
        for col1, col2 in itertools.product(origin_metadata.columns.values(), target_metadata.columns.values()):
            # results = self.dataframe_matcher.match_dataframes(reference_dataframe, subject_dataframe)
            result = self.dataframe_matcher.match_columns(
                methods=methods,
                col_meta1=col1,
                col_meta2=col2,
                series1=origin_data[col1.name],
                series2=target_data[col2.name]
            )
            # keep just the average for now
            result_average = result[1]
            col1.add_relationship(
                result_average, target_item.get_checksum(), col2.name
            )

    def add_catalogue_item(self, catalogue_item: metadata.CatalogueItem):
        """Adds a metadata item to the ones loaded in memory

        Args:
            catalogue_item: The desired catalogue item to add

        Returns: None
        """
        self.loaded_catalogue[catalogue_item.get_id()] = catalogue_item

    def write_catalogue(self, path: str):
        """Write all loaded metadata to a json file

        WARNING: overwrites previous entry

        Args:
            path: The path to write metadata to

        Returns: None
        """
        catalogue_items = [
            item.write_metadata()
            for item in self.loaded_catalogue.values()
        ]
        with open(path, 'w') as catalogue_file:
            catalogue_file.write(json.dumps(catalogue_items))

    def load_file(self, path, catalogue_metadata=None, construct_metadata=False):
        """Uses the from_csv method to load a csv file into the catalogue

        Args:
            path: The path to the file

        Returns: None
        """
        new_item = metadata.from_csv(path)
        new_item.rebuild_metadata_object()
        self.add_catalogue_item(new_item)

    def load_metadata(self, path):
        """Uses the from_metdata method to load in previously created metadata items
        as catalogue items

        Args:
            path: The path to the metadata file

        Returns: None
        """
        new_items = metadata.from_metadata_json(path)
        for new_item in new_items:
            new_item.rebuild_metadata_object()
            self.add_catalogue_item(new_item)

    def scan_local_filesystem(self, path):
        """Read in data from a local filesystem, given a path

        Args:
            path: The root path of the data

        Returns: A generator of each item produced
        """
        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.endswith('csv'):
                    new_item = metadata.from_csv(os.path.join(root, filename))
                    new_item.rebuild_metadata_object()
                    yield new_item
                    self.add_catalogue_item(new_item)


if __name__ == "__main__":
    # locally test the mock filesystem
    launch_config = yaml.safe_load(open("launch_config.yaml"))
    discovery_instance = DiscoveryClient(launch_config)

    from utils.datagen import FakeDataGen

    fake_data = FakeDataGen()
    # fake_files = fake_data.build_df_to_file(1000, "matcher_test", index_type="categoric", continuous_data=5,
    #                                         file_spread=2)
    # discovery_instance.load_file(fake_files[0])
    # discovery_instance.load_file(fake_files[1])
    discovery_instance.load_metadata("newtest.json")

    discovery_instance.construct_relationships(
        methods=[
            MatchColumnNamesLCS,
            MatchIdenticalColumnNames
        ]
    )

    discovery_instance.write_catalogue("newtest.json")

    discovery_instance.create_visual("test_visual")
