"""
Calculate the similarity of 2 column names using the Levenshtein distance
"""

from Levenshtein import ratio

from discovery.data_matching.data_match_interface import DataMatcher


class MatchColumnNamesLevenshtein(DataMatcher):
    @staticmethod
    def run_process(col_meta1, col_meta2, **kwargs):
        return ratio(col_meta1.name, col_meta2.name) * 100
