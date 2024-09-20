import os
from collections import defaultdict
from preprocessing import preprocess_text_lemmatization, preprocess_text_stemming
from nltk.util import ngrams

def build_index(directory):
    index = defaultdict(set)
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Preprocess the content using lemmatization
                tokens = preprocess_text_lemmatization(content)
                for token in tokens:
                    # Add the file name to the index for each token
                    index[token].add(file_name)
    return index

def build_biword_index(directory):
    biword_index = defaultdict(set)
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Preprocess the content using stemming
                tokens = preprocess_text_stemming(content)
                # Generate biwords (2-grams) from the tokens
                biword_list = ngrams(tokens, 2)
                for biword in biword_list:
                    # Add the file name to the biword index
                    biword_index[biword].add(file_name)
    return biword_index