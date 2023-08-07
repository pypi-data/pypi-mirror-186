"""
The simplest possible solution to matching column data
"""

from discovery.data_matching.data_match_interface import DataMatcher


class MatchIdenticalColumnNames(DataMatcher):
    @staticmethod
    def run_process(col_meta1, col_meta2, **kwargs):
        return int(col_meta1.name == col_meta2.name) * 100
