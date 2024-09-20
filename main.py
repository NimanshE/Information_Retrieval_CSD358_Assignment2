import os
from indexing import build_index, build_biword_index
from boolean_search import boolean_query_search
from biword_search import biword_query_search
from proximity_search import proximity_query_search
from soundex_search import soundex_query_search
from preprocessing import preprocess_text_lemmatization, preprocess_text_stemming

# Directory containing the text files
directory = "/Users/nimanshendlay/Desktop/Shiv_Nadar/SEM5/CSD358(IR)/assignment_1/Information_Retrieval_CSD358_Assignment1/Corpus"
# Build the indices
index = build_index(directory)
bigram_index = build_biword_index(directory)

def run_predefined_tests():
    # Boolean Query Search
    print("Boolean Queries")
    query1 = 'technology and phone'
    result1 = boolean_query_search(query1, index)
    print(f"Result for query '{query1}': {result1}")

    query2 = 'deliveries or food'
    result2 = boolean_query_search(query2, index)
    print(f"Result for query '{query2}': {result2}")

    # Biword Query Search
    print("\nBiword Index Queries")
    query3 = 'search engine'
    result3 = biword_query_search(query3, bigram_index)
    print(f"Result for query '{query3}': {result3}")

    query4 = 'searching engines'
    result4 = biword_query_search(query4, bigram_index)
    print(f"Result for query '{query4}': {result4}")

    query5 = 'downloaded apps'
    result5 = biword_query_search(query5, bigram_index)
    print(f"Result for query '{query5}': {result5}")

    # Proximity Search
    print("\nProximity Queries")
    query6 = 'easy and passenger'
    proximity6 = 10
    result6 = proximity_query_search(query6, directory, proximity6)
    print(f"Result for query '{query6}' with proximity {proximity6}: {result6}")

    query7 = 'graphic and capabilities'
    proximity7 = 10
    result7 = proximity_query_search(query7, directory, proximity7)
    print(f"Result for query '{query7}' with proximity {proximity7}: {result7}")

    proximity8 = 5
    result8 = proximity_query_search(query7, directory, proximity8)
    print(f"Result for query '{query7}' with proximity {proximity8}: {result8}")

    # Soundex Search
    print("\nSoundex Queries")
    query9 = 'lehri and stainford'
    result9 = soundex_query_search(query9, directory)
    print(f"Result for query '{query9}': {result9}")

    query10 = 'yahu and dauwnloads'
    result10 = soundex_query_search(query10, directory)
    print(f"Result for query '{query10}': {result10}")

def custom_input_search():
    query_type = input("Enter query type (boolean/biword/proximity/soundex): ").strip().lower()
    query = input("Enter your query: ").strip()

    if query_type == 'boolean':
        result = boolean_query_search(query, index)
    elif query_type == 'biword':
        result = biword_query_search(query, bigram_index)
    elif query_type == 'proximity':
        proximity = int(input("Enter proximity value: ").strip())
        result = proximity_query_search(query, directory, proximity)
    elif query_type == 'soundex':
        result = soundex_query_search(query, directory)
    else:
        print("Invalid query type.")
        return

    print(f"Result for query '{query}': {result}")

def view_tokens():
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Preprocess the content using lemmatization and stemming
                tokens_lemmatized = preprocess_text_lemmatization(content)
                tokens_stemmed = preprocess_text_stemming(content)
                print(f"Tokens for file '{file_name}':")
                print(f"Lemmatized: {tokens_lemmatized}")
                print(f"Stemmed: {tokens_stemmed}")

def main():
    while True:
        print("\nMenu:")
        print("1. Run predefined test cases")
        print("2. Give custom input")
        print("3. View tokens for each file")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            run_predefined_tests()
        elif choice == '2':
            custom_input_search()
        elif choice == '3':
            view_tokens()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()