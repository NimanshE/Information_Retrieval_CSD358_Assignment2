import math
import numpy as np
from collections import defaultdict

class Evaluator:
    def __init__(self, indexer):
        self.indexer = indexer  # Indexer instance containing the inverted index and document lengths

    def compute_idf(self, term):
        df = len(self.indexer.dictionary[term])  # Document frequency of the term
        return math.log10(self.indexer.doc_count / df) if df else 0  # Compute IDF, handle zero division

    def process_query(self, query, preprocessor):
        query_terms = preprocessor.preprocess(query)  # Preprocess the query text
        query_term_freqs = defaultdict(int)  # Term frequencies in the query
        for term in query_terms:
            query_term_freqs[term] += 1  # Count term frequency
        query_vector = {}  # Query vector for term weights
        for term, freq in query_term_freqs.items():
            tf = 1 + math.log10(freq)  # Compute term frequency weight
            idf = self.compute_idf(term)  # Compute inverse document frequency
            query_vector[term] = tf * idf  # Compute TF-IDF weight
        query_length = np.linalg.norm(list(query_vector.values()))  # Compute query vector length for normalization
        return query_vector, query_length

    def rank_documents(self, query, preprocessor):
        query_vector, query_length = self.process_query(query, preprocessor)  # Process the query
        scores = defaultdict(float)  # Document scores
        for term, query_weight in query_vector.items():
            if term in self.indexer.dictionary:
                for doc_id, freq in self.indexer.dictionary[term]:
                    doc_weight = 1 + math.log10(freq)  # Compute document term weight
                    scores[doc_id] += query_weight * doc_weight  # Accumulate score for the document
        for doc_id in scores:
            scores[doc_id] /= (self.indexer.doc_lengths[doc_id] * query_length)  # Normalize the scores
        ranked_docs = sorted(scores.items(), key=lambda item: (-item[1], item[0]))  # Sort documents by score
        return ranked_docs[:10]  # Return top 10 ranked documents