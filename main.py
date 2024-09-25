import os
from indexing import Indexer
from searching import Searcher
from preprocessing import Preprocessor

def execute_queries(searcher, preprocessor, corpus_dir, queries):
    for i, query in enumerate(queries, 1):
        print(f"Query {i}: {query}")
        print("Output:")
        results = searcher.search(query, preprocessor)  # Search for the query
        print(f"{'Rank':<5} {'Document':<30} {'Similarity Score':<15}")
        print("-" * 50)
        for rank, (doc_id, score) in enumerate(results, 1):
            print(f"{rank:<5} {os.listdir(corpus_dir)[doc_id]:<30} {score:<15}")
        print()

def print_indexes(indexer):
    print("Inverted Index:")
    for term, postings in indexer.dictionary.items():
        print(f"{term}: {postings}")

def main():
    corpus_dir = 'corpus'  # Directory containing the corpus of documents
    indexer = Indexer(corpus_dir)  # Create an Indexer instance
    indexer.index_corpus()  # Index the corpus
    preprocessor = Preprocessor()  # Create a Preprocessor instance
    searcher = Searcher(indexer)  # Create a Searcher instance

    while True:
        print("Menu:")
        print("1. Run Custom Input")
        print("2. Run Predefined Test Cases")
        print("3. Print all the indexes")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            query = input("Enter your query: ")
            execute_queries(searcher, preprocessor, corpus_dir, [query])
        elif choice == '2':
            predefined_queries = [
                "Developing your Zomato business account and profile is a great way to boost your restaurant’s online reputation",
                "Warwickshire, came from an ancient family and was the heiress to some land"
            ]
            execute_queries(searcher, preprocessor, corpus_dir, predefined_queries)
        elif choice == '3':
            print_indexes(indexer)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()