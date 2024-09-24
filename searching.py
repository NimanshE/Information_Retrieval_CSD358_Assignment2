from evaluation import Evaluator

class Searcher:
    def __init__(self, indexer):
        self.evaluator = Evaluator(indexer)

    def search(self, query, preprocessor):
        ranked_docs = self.evaluator.rank_documents(query, preprocessor)
        return [(doc_id, score) for doc_id, score in ranked_docs]