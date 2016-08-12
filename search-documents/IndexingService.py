#!/usr/bin/python3
import glob
import pickle
import re

from sklearn.feature_extraction.text import TfidfVectorizer


class IndexingService:
    index = {}
    documents, tf = None, None

    def __init__(self):
        self.documents = glob.glob("data/*")
        self.tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3),
                                        min_df = 0, stop_words = 'english')

    def generate_inverted_index(self):
        for doc_file in self.documents:
            filtered_text = self.filter_text(self.get_file_content(doc_file))
            tfidf_matrix =  self.tf.fit_transform(filtered_text)
            feature_names = self.tf.get_feature_names()
            dense = tfidf_matrix.todense()
            document = dense[0].tolist()[0]
            phrase_scores = [pair for pair in zip(
                                range(0, len(document)), document)
                                 if pair[1] > 0]
            sorted_phrase_scores = sorted(phrase_scores,
                                    key=lambda t: t[1] * -1)
            doc_index = {}
            for key, score in sorted_phrase_scores:
                phrase = feature_names[key]
                if phrase not in self.index:
                    self.index[phrase] = {}
                self.index[phrase][doc_file] = score


    def filter_text(self, text):
        text = (re.sub("\[\d+\]","", "".join(text))).strip('\n') # Make the text annotation free
        text = ''.join([i if ord(i) < 128 else ' ' for i in text]) # Remove non-ascii characrers.
        # TODO: Remove entire words which have non-ascii chars instead of just individual chars
        text = text.split(".")
        return text

    def get_file_content(self, filename):
        doc = open(filename, 'r')
        content = doc.readlines()
        doc.close()
        return content

    def save_index(self):
        pickle.dump(self.index, open("index.p", "wb"))

indexing_service = IndexingService()
indexing_service.generate_inverted_index()
indexing_service.save_index()
