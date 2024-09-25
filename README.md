# CSD-358 Information Retrieval Assignment 2:
### By: 
```
Nimansh Endlay (2210110438) CSE'26
Preksha Khera (2110110391) CSE'25
```
## Vector Space Model
The Vector Space Model (VSM) is an algebraic model used for representing text documents (and any objects, in general) as vectors of identifiers, such as index terms. It is widely used in information retrieval and text mining for tasks such as document ranking and similarity measurement.

### Key Concepts

1. **Documents and Terms**:
   - Each document in a corpus is represented as a vector.
   - Each dimension of the vector corresponds to a separate term (word) from the document.

2. **Term Frequency (TF)**:
   - The frequency of a term in a document. It indicates how often a term appears in a document.

3. **Inverse Document Frequency (IDF)**:
   - A measure of how important a term is. It is the logarithm of the total number of documents divided by the number of documents containing the term.

4. **TF-IDF Weighting**:
   - Combines TF and IDF to give a weight to each term in a document. The weight increases with the number of occurrences within a document and decreases with the number of documents that contain the term.

5. **Cosine Similarity**:
   - A measure of similarity between two vectors. It is the cosine of the angle between the vectors, which is computed as the dot product of the vectors divided by the product of their magnitudes.

### Steps in VSM

1. **Indexing**:
   - Create an inverted index where each term maps to a list of documents in which it appears, along with the term frequency in each document.

2. **Query Processing**:
   - Convert the query into a vector using the same term weighting scheme (e.g., TF-IDF).

3. **Similarity Computation**:
   - Compute the cosine similarity between the query vector and each document vector in the corpus.

4. **Ranking**:
   - Rank the documents based on their similarity scores to the query.

### Conclusion

The Vector Space Model is a powerful and intuitive method for text representation and similarity measurement, making it a cornerstone of many information retrieval systems.

## Overview

This project aims to implements a ranked retrieval system using the Vector Space Model (VSM). The system indexes a corpus of documents and allows for searching using free text queries. The documents are ranked by cosine similarity based on tf-idf (term frequency-inverse document frequency) scores.

## Files and Their Functions

### `main.py`

This is the main entry point of the application. It provides a menu-driven interface to:
1. Run custom input queries.
2. Run predefined test cases.
3. Print all indexes and scores.
4. Exit the application.

### `indexing.py`

This file contains the `Indexer` class, which is responsible for:
- Indexing the corpus of documents.
- Creating an inverted index where each term maps to a list of (doc_id, term frequency) tuples.
- Storing document lengths for normalization.

### `searching.py`

This file contains the `Searcher` class, which is responsible for:
- Searching the indexed documents for a given query.
- Ranking the documents based on cosine similarity using tf-idf scores.

### `evaluation.py`

This file contains the `Evaluator` class, which is responsible for:
- Computing the inverse document frequency (idf) for terms.
- Processing the query to compute tf-idf weights.
- Ranking documents based on cosine similarity.

### `preprocessing.py`

This file contains the `Preprocessor` class, which is responsible for:
- Preprocessing text by tokenizing, lemmatizing, stemming, and removing stop words and non-alphanumeric terms.

## How to Run the Code

1. **Install Dependencies**: Ensure you have the required NLTK data files. You can download them using the following commands:
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    ```

2. **Prepare the Corpus**: Place your documents in a directory named `corpus`.

3. **Run the Application**: Execute the `main.py` file.
    ```bash
    python main.py
    ```

4. **Menu Options**:
    - **Run Custom Input**: Enter your query when prompted.
    - **Run Predefined Test Cases**: The application will run predefined queries.
    - **Print all the indexes and scores**: Displays the inverted index and document lengths.
    - **Exit**: Terminates the application.

## Explanation

### Indexing

- **Inverted Index**: The `Indexer` class creates an inverted index where each term maps to a list of (doc_id, term frequency) tuples.
- **Document Lengths**: Document lengths are stored for normalization purposes.

### Searching

- **Query Processing**: The `Evaluator` class preprocesses the query and computes tf-idf weights.
- **Ranking**: Documents are ranked based on cosine similarity between the query vector and document vectors.

### Preprocessing

- **Tokenization**: Text is tokenized into terms.
- **Lemmatization and Stemming**: Terms are reduced to their base and root forms.
- **Stop Words Removal**: Common stop words are removed.
- **Non-Alphanumeric Removal**: Non-alphanumeric terms are removed.

### Evaluation

- **Initialization**: The `Evaluator` class is initialized with an `Indexer` instance.
- **IDF Calculation**: The `compute_idf` method calculates the inverse document frequency for a term.
- **Query Processing**: The `process_query` method preprocesses the query, computes term frequencies, and calculates tf-idf weights.
- **Document Ranking**: The `rank_documents` method computes cosine similarity scores and ranks the documents based on these scores.

## Sample Input and Output

### Sample Input

1. **Custom Query**: "Developing your Zomato business account and profile is a great way to boost your restaurant’s online reputation"
2. **Predefined Query**: "Warwickshire, came from an ancient family and was the heiress to some land"

### Sample Output

#### Custom Query
```
Query 1: Developing your Zomato business account and profile is a great way to boost your restaurant’s online reputation
Output:
Rank  Document                       Similarity Score
--------------------------------------------------
1     zomato.txt                     0.21964664528869027
2     swiggy.txt                     0.13497448842990908
3     messenger.txt                  0.061426692344884126
4     instagram.txt                  0.060819695911374864
5     Discord.txt                    0.0557099428374534
6     bing.txt                       0.053539590341553596
7     youtube.txt                    0.05024279126496341
8     paypal.txt                     0.04825964036664642
9     reddit.txt                     0.04668948587151671
10    flipkart.txt                   0.041784176720284824
```

#### Predefined Query
```
Query 2: Warwickshire, came from an ancient family and was the heiress to some land
Output:
Rank  Document                       Similarity Score
--------------------------------------------------
1     shakespeare.txt                0.12214792901832719
2     levis.txt                      0.025614307383182853
3     google.txt                     0.021422046845524578
4     nike.txt                       0.01966741650747592
5     zomato.txt                     0.018064597247571968
6     Adobe.txt                      0.0168133659390181
7     huawei.txt                     0.014518852716692747
8     skype.txt                      0.01283137925906369
9     blackberry.txt                 0.011982761696773
10    Dell.txt                       0.011096292154272795
```
