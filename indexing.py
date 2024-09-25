import os
import math
from collections import defaultdict
import numpy as np
from preprocessing import Preprocessor

class Indexer:
    def __init__(self, corpus_dir):
        self.corpus_dir = corpus_dir  # Directory containing the corpus of documents
        self.dictionary = defaultdict(list)  # Inverted index: term -> list of (doc_id, frequency)
        self.doc_lengths = {}  # Document lengths for normalization
        self.doc_count = 0  # Total number of documents
        self.preprocessor = Preprocessor()  # Preprocessor instance for text preprocessing

    def index_corpus(self):
        # Iterate over all files in the corpus directory
        for doc_id, filename in enumerate(os.listdir(self.corpus_dir)):
            self.doc_count += 1  # Increment document count
            with open(os.path.join(self.corpus_dir, filename), 'r', encoding='utf-8') as file:
                terms = self.preprocessor.preprocess(file.read())  # Preprocess the document text
                term_freqs = defaultdict(int)  # Term frequencies in the current document
                for term in terms:
                    term_freqs[term] += 1  # Count term frequency
                for term, freq in term_freqs.items():
                    self.dictionary[term].append((doc_id, freq))  # Add term frequency to the inverted index
                # Calculate and store the document length for normalization
                self.doc_lengths[doc_id] = np.linalg.norm([1 + math.log10(freq) for freq in term_freqs.values()])