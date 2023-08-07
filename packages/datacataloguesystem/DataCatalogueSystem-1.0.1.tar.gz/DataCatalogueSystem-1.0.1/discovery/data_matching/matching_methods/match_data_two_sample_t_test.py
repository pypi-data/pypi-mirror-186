"""
Determine if the unknown population means of the two groups are equal
"""

import numpy as np
import scipy.stats as stats

from discovery.data_matching.data_match_interface import DataMatcher


class MatchDataTwoSampleTTest(DataMatcher):
    @staticmethod
    def run_process(series1, series2, **kwargs):
        # Normalize the data
        series1 = series1 / np.max(np.abs(series1), axis=0)
        series2 = series2 / np.max(np.abs(series2), axis=0)

        # First, we determine if the 2 groups have the same variance
        # A ratio of less than 4:1 indicates we should consider the variances equal
        variance_a = np.var(series1)
        variance_b = np.var(series2)
        if min(variance_a, variance_b) == 0:
            equal_variances = max(variance_a, variance_b) < 4
        else:
            equal_variances = (max(variance_a, variance_b) / min(variance_a, variance_b)) < 4

        # Perform the two sample T-test
        result_statistic, result_p_value = stats.ttest_ind(series1, series2, equal_var=equal_variances)

        # If the p-value is greater than 0.05, we accept the null hypothesis that the mean of the two groups is equal
        # Otherwise, we reject it, and claim that the means are different
        return result_p_value > 0.05
