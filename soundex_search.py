import os
from preprocessing import preprocess_text_stemming

def soundex_query_search(query, directory):
    def soundex(word):
        # Convert the word to lowercase
        word = word.casefold()
        soundex_codes = ("bfpv", "cgjkqsxz", "dt", "l", "mn", "r")
        soundex_code = [word[0].upper()]

        # Generate the Soundex code for the word
        for char in word[1:]:
            for index, code_group in enumerate(soundex_codes):
                if char in code_group:
                    digit = str(index + 1)
                    if digit != soundex_code[-1]:
                        soundex_code.append(digit)
        return ''.join(soundex_code)[:4].ljust(4, '0')

    # Split the query into terms and generate their Soundex codes
    query_terms = query.casefold().split()
    query_soundex_codes = [soundex(term) for term in query_terms]
    result_files = set()
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Preprocess the content using stemming
                tokens = preprocess_text_stemming(content)
                # Generate Soundex codes for the tokens
                token_soundex_codes = [soundex(token) for token in tokens]
                # Check if all query Soundex codes are in the token Soundex codes
                if all(query_code in token_soundex_codes for query_code in query_soundex_codes):
                    result_files.add(file_name)

    return result_files
