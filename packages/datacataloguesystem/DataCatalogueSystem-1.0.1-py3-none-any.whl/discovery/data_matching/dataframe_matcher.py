"""
Takes two dataframes and tries to match them column by column
"""
import logging
from typing import Type

# TODO: currently not working out of the box, must be run with the following statements...
# >>> import nltk
# >>> nltk.download('wordnet')
# >>> nltk.download('omw-1.4')
import pandas as pd
import numpy

from discovery.data_matching.data_match_interface import DataMatcher
from discovery.metadata import CatalogueMetadata, NumericColMetadata, ColMetadata

logger = logging.getLogger(__name__)


class DataFrameMatcher:
    @staticmethod
    def match_columns(
            methods: list[Type[DataMatcher]],
            col_meta1: ColMetadata,
            col_meta2: ColMetadata,
            series1: pd.Series = None,
            series2: pd.Series = None,
            metadata1: CatalogueMetadata = None,
            metadata2: CatalogueMetadata = None,
            weights: list[int] = None
    ) -> (dict, int):
        """
        Calculate the similarity of 2 columns using a combination of methods
        Weights is given as an ordered list of weights to apply to each method, respective to the order of the methods

        Returns a dictionary of individual similarity values, followed by an overall average
        """

        weights = weights or []
        # forward fill weights with 1's
        filled_weights = [1] * len(methods)
        filled_weights[:len(weights)] = weights
        similarity_ref = {}
        overall_similarity = 0

        for index, method in enumerate(methods):
            try:
                method_instance = method()

                logger.debug(f"Matching columns using {method_instance.name}")
                similarity = method_instance.run_process(**{
                    "col_meta1": col_meta1,
                    "col_meta2": col_meta2,
                    "series1": series1,
                    "series2": series2,
                    "metadata1": metadata1,
                    "metadata2": metadata2
                })
                # update the similarity reference with applied method and weight
                similarity_ref.update({method_instance.name: (similarity, filled_weights[index])})
                overall_similarity += similarity * filled_weights[index]

            except Exception as exc:
                logger.error(f"Something unexpected went wrong running method {method.__qualname__}, skipping...")
                logger.error(exc)
                # something went wrong, invalidate the method and ensure the weight is correct
                filled_weights[index] = 0

        # get the average similarity, if overall_similarity is zero then something probably went wrong, set to zero
        average_similarity = (overall_similarity / sum(filled_weights)) if overall_similarity else 0
        logger.debug("Matching complete")

        return similarity_ref, average_similarity

    @staticmethod
    def match_column_in_dataframe(df1: pd.DataFrame, column1: NumericColMetadata,
                                  metadata2: CatalogueMetadata, df2: pd.DataFrame):
        """
        Find the best match of a column in another dataframe
        :param df1:
        :param column1:
        :param metadata2:
        :param df2:
        :return:
        """
        scores = {}
        no_of_tests = {}
        average_differences = {}
        minimum_differences = {}
        maximum_differences = {}
        for column2 in metadata2.columns:
            # LCS name test
            lcs_percentage = DataFrameMatcher.match_name_lcs(column1.name, column2.name)

            # Levenshtein name test
            levenshtein_percentage = DataFrameMatcher.match_name_levenshtein(column1.name, column2.name)

            # Data type test
            data_type_matches = 100 if column1.col_type == column2.col_type else 0

            # Continuity test
            continuity_percentage = 100 * (1 - abs(column1.continuity - column2.continuity))

            # Numerical values test
            numerical_percentage = 100 * (1 - abs(column1.is_numeric_percentage -
                                                  column2.is_numeric_percentage))

            # Average test
            if column1.mean is not None and column2.mean is not None:
                average_differences[column2.name] = abs(column1.mean - column2.mean)

            # Min test
            try:
                minimum1 = float(column1.minimum)
                minimum2 = float(column2.minimum)
                minimum_differences[column2.name] = abs(minimum1 - minimum2)
            except ValueError:
                pass

            # Max test
            try:
                maximum1 = float(column1.maximum)
                maximum2 = float(column2.maximum)
                maximum_differences[column2.name] = abs(maximum1 - maximum2)
            except ValueError:
                pass

            # Average similarity
            average_similarity = lcs_percentage + levenshtein_percentage + data_type_matches + \
                                 continuity_percentage + numerical_percentage

            scores[column2.name] = average_similarity
            no_of_tests[column2.name] = 5

        # Normalize the average differences
        normalized_average_differences = DataFrameMatcher.normalize_values(average_differences)
        for name, similarity in normalized_average_differences.items():
            scores[name] += similarity
            no_of_tests[name] += 1

        # Normalize the minimum differences
        normalized_minimum_differences = DataFrameMatcher.normalize_values(minimum_differences)
        for name, similarity in normalized_minimum_differences.items():
            scores[name] += similarity
            no_of_tests[name] += 1

        # Normalize the maximum differences
        normalized_maximum_differences = DataFrameMatcher.normalize_values(maximum_differences)
        for name, similarity in normalized_maximum_differences.items():
            scores[name] += similarity
            no_of_tests[name] += 1

        for column2 in metadata2.columns:
            scores[column2.name] /= no_of_tests[column2.name]

        best_similarity = 0
        best_name = ''
        for name, similarity in scores.items():
            if similarity > best_similarity:
                best_similarity = similarity
                best_name = name

        return best_name, best_similarity

    @staticmethod
    def normalize_values(dictionary: dict):
        normalized_dictionary = {}
        min_value = numpy.inf
        max_value = 0
        for index, value in dictionary.items():
            if value < min_value:
                min_value = value
            if value > max_value:
                max_value = value

        for index, value in dictionary.items():
            normalized_dictionary[index] = (1 - (value - min_value) / (max_value - min_value)) * 100

        return normalized_dictionary
