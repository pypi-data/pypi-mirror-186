"""
Implements standard methods expected of data matching techniques

NOTE:
    we're filling out unused parameters on purpose
TODO:
    add decorators for enforcing int values
"""
import pandas as pd
from discovery.metadata import ColMetadata, CatalogueMetadata
from discovery import metadata


class DataMatcher:
    def __init__(self):
        self.name = self.__class__.__qualname__

    def match_columns(
            self,
            col_meta1: metadata.ColMetadata,
            col_meta2: metadata.ColMetadata,
            series1: pd.Series = None,
            series2: pd.Series = None,
            metadata1: metadata.CatalogueItem = None,
            metadata2: metadata.CatalogueItem = None

    ) -> int:
        incoming = locals()
        incoming.pop('self')
        return self.run_process(**incoming)

    @staticmethod
    def run_process(
            col_meta1: ColMetadata,
            col_meta2: ColMetadata,
            series1: pd.Series = None,
            series2: pd.Series = None,
            metadata1: CatalogueMetadata = None,
            metadata2: CatalogueMetadata = None
    ) -> int:
        """
        Run the actual implemented process
        Reiterate the match_columns parameters here, as IDE's can pick it up
        """
        raise NotImplementedError
