"""
Calculate the similarity of 2 column names using the Longest Contiguous Matching Subsequence
"""

from difflib import SequenceMatcher

from discovery.data_matching.data_match_interface import DataMatcher


class MatchColumnNamesLCS(DataMatcher):
    @staticmethod
    def run_process(col_meta1, col_meta2, **kwargs):
        return SequenceMatcher(None, col_meta1.name, col_meta2.name).ratio() * 100
