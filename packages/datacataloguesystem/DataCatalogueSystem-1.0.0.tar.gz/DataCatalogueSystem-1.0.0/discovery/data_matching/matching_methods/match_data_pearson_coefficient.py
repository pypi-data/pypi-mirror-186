"""
Calculate the Pearson correlation coefficient between the 2 columns if they are both numerical
"""


from discovery.data_matching.data_match_interface import DataMatcher


class MatchDataPearsonCoefficient(DataMatcher):
    @staticmethod
    def run_process(series1, series2, **kwargs):
        pearson_correlation_coefficient = abs(series1.corr(series2)) * 100
        return pearson_correlation_coefficient
