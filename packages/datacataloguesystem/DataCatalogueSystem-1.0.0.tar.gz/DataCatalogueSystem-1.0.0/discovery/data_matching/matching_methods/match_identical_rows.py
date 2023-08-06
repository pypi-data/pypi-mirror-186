"""
Calculate a similarity percentage with set operations (intersection vs union) for (possible) categorical data
"""

import numpy
from discovery.data_matching.data_match_interface import DataMatcher


class MatchIdenticalRows(DataMatcher):
    @staticmethod
    def run_process(series1, series2, **kwargs):
        stringified_column_a = series1.apply(str)
        stringified_column_b = series2.apply(str)

        categorical_similarity = len(numpy.intersect1d(stringified_column_a, stringified_column_b)) / len(
            numpy.union1d(stringified_column_a, stringified_column_b)) * 100
        return categorical_similarity
