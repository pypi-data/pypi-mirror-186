"""
Calculate the normalized distance measure between two numerical columns using Dynamic Time Warping
"""

from dtaidistance import dtw
import pandas as pd
from discovery.data_matching.data_match_interface import DataMatcher


class MatchDataDynamicTimeWarping(DataMatcher):
    @staticmethod
    def run_process(series1: pd.Series = None, series2: pd.Series = None, **kwargs):
        max_distance = len(series1) * max(series1)

        if pd.api.types.is_numeric_dtype(series1) and pd.api.types.is_numeric_dtype(series2):
            return (max_distance - dtw.distance(series1, series2)) / max_distance * 100
        return 0
