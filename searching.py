from evaluation import Evaluator

class Searcher:
    def __init__(self, indexer):
        self.evaluator = Evaluator(indexer)  # Evaluator instance for ranking documents

    def search(self, query, preprocessor):
        ranked_docs = self.evaluator.rank_documents(query, preprocessor)  # Rank documents for the query
        return [(doc_id, score) for doc_id, score in ranked_docs]  # Return document IDs and scores