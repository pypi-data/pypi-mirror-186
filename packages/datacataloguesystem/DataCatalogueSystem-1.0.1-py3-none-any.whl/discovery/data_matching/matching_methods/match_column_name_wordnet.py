"""
Calculate the similarity of 2 column names using WordNet
"""

from nltk.corpus import wordnet
from itertools import product

from discovery.data_matching.data_match_interface import DataMatcher


class MatchColumnNamesWordnet(DataMatcher):
    @staticmethod
    def run_process(col_meta1, col_meta2, **kwargs):
        synset_first = wordnet.synsets(col_meta1)
        synset_second = wordnet.synsets(col_meta2)
        wordnet_ratio = 0
        if len(synset_first) > 0 and len(synset_second) > 0:
            wordnet_ratio = max(
                wordnet.wup_similarity(s1, s2) for s1, s2 in product(synset_first, synset_second)) * 100

        return wordnet_ratio
