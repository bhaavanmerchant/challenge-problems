#!/usr/bin/python3
from SearchEngine import SearchEngine

import sys

class QuerySystem:
    search_engine = None

    def __init__(self):
        self.search_engine = SearchEngine()

    def get_queries_from_file(self, filename='query.txt'):
        with open('query.txt', 'r') as query_file:
            return query_file.readlines()
        return None

    def search_query(self, query):
        results = []
        for (document, score) in self.search_engine.search(query.lower()):
            results.append((document, str(score)))
        return results

    def store_result(self, query, result):
        with open('output/' + query + '.txt', 'w') as output_file:
            for (doc, score) in result:
                output_file.write(doc+'\n')

    def print_result(self, result):
        for (document, score) in result:
            print(document + " : " + str(score))

query_system = QuerySystem()
if len(sys.argv) > 1:
    query_system.print_result(query_system.search_query(sys.argv[1]))
else:
    queries = query_system.get_queries_from_file()
    for query in queries:
        query = query.strip()
        query_system.store_result(query, query_system.search_query(query))
