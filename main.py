import os
from indexing import Indexer
from searching import Searcher
from preprocessing import Preprocessor

def execute_queries(searcher, preprocessor, corpus_dir):
    queries = [
        "Developing your Zomato business account and profile is a great way to boost your restaurant’s online reputation",
        "Warwickshire, came from an ancient family and was the heiress to some land"
    ]

    for i, query in enumerate(queries, 1):
        print(f"Output{i}:")
        results = searcher.search(query, preprocessor)
        for doc_id, score in results:
            print(f"('{os.listdir(corpus_dir)[doc_id]}', {score})")
        print()

if __name__ == "__main__":
    corpus_dir = 'corpus'
    indexer = Indexer(corpus_dir)
    indexer.index_corpus()
    preprocessor = Preprocessor()
    searcher = Searcher(indexer)
    execute_queries(searcher, preprocessor, corpus_dir)