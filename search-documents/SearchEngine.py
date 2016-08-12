#!/usr/bin/python3
import pickle

class SearchEngine:
    index = {}

    def __init__(self):
        self.index = pickle.load(open("index.p", "rb"))

    def get_query_lists(self, query):
        word_list = query.split(" ")
        return ( word_list,
                [" ".join(phrase) for phrase in zip(word_list, word_list[1:])], # Bigram phrases
                [" ".join(phrase) for phrase in zip(word_list, word_list[1:],   # Trigram phrases
                                                                word_list[2:])])

    def get_score(self, query_lists):
        score = {}
        index = self.index

        def ngram_scorer(ngram_list, score_power_factor):
            for ngram in ngram_list:
                if ngram in index:
                    for k,v in index[ngram].items():
                        if k not in score:
                            score[k] = 0
                        score[k] += 1/v**score_power_factor
        (unigram_list, bigram_list, trigram_list) = query_lists
        ngram_scorer(trigram_list, 3)
        ngram_scorer(bigram_list, 2)
        ngram_scorer(unigram_list, 1)
        return score

    def search(self, query):
        results = []
        for key, value in sorted(self.get_score(
                                    self.get_query_lists(query)).items(),
                                    key=lambda x:x[1], reverse=True):
            results.append((key,value))
        return results
