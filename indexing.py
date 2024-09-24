import os
import math
from collections import defaultdict
import numpy as np
from preprocessing import Preprocessor


class Indexer:
    def __init__(self, corpus_dir):
        self.corpus_dir = corpus_dir
        self.dictionary = defaultdict(list)
        self.doc_lengths = {}
        self.doc_count = 0
        self.preprocessor = Preprocessor()

    def index_corpus(self):
        for doc_id, filename in enumerate(os.listdir(self.corpus_dir)):
            self.doc_count += 1
            with open(os.path.join(self.corpus_dir, filename), 'r', encoding='utf-8') as file:
                terms = self.preprocessor.preprocess(file.read())
                term_freqs = defaultdict(int)
                for term in terms:
                    term_freqs[term] += 1
                for term, freq in term_freqs.items():
                    self.dictionary[term].append((doc_id, freq))
                self.doc_lengths[doc_id] = np.linalg.norm([1 + math.log10(freq) for freq in term_freqs.values()])