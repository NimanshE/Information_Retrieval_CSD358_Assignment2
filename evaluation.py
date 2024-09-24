import math
import numpy as np
from collections import defaultdict


class Evaluator:
    def __init__(self, indexer):
        self.indexer = indexer

    def compute_idf(self, term):
        df = len(self.indexer.dictionary[term])
        return math.log10(self.indexer.doc_count / df) if df else 0

    def process_query(self, query, preprocessor):
        query_terms = preprocessor.preprocess(query)
        query_term_freqs = defaultdict(int)
        for term in query_terms:
            query_term_freqs[term] += 1
        query_vector = {}
        for term, freq in query_term_freqs.items():
            tf = 1 + math.log10(freq)
            idf = self.compute_idf(term)
            query_vector[term] = tf * idf
        query_length = np.linalg.norm(list(query_vector.values()))
        return query_vector, query_length

    def rank_documents(self, query, preprocessor):
        query_vector, query_length = self.process_query(query, preprocessor)
        scores = defaultdict(float)
        for term, query_weight in query_vector.items():
            if term in self.indexer.dictionary:
                for doc_id, freq in self.indexer.dictionary[term]:
                    doc_weight = 1 + math.log10(freq)
                    scores[doc_id] += query_weight * doc_weight
        for doc_id in scores:
            scores[doc_id] /= (self.indexer.doc_lengths[doc_id] * query_length)
        ranked_docs = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
        return ranked_docs[:10]