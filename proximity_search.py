import os
from preprocessing import preprocess_text_stemming

def proximity_query_search(query, directory, proximity):
    # Convert the query to lowercase
    query = query.casefold()
    # Preprocess the query using stemming
    query_terms = preprocess_text_stemming(query)
    result_files = set()
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Preprocess the content using stemming
                tokens = preprocess_text_stemming(content)

                # Check for proximity of query terms in the tokens
                for idx in range(len(tokens)):
                    if tokens[idx] == query_terms[0]:
                        for pos in range(idx + 1, min(idx + proximity + 1, len(tokens))):
                            if tokens[pos] == query_terms[1]:
                                result_files.add(file_name)
                                break

    return result_files