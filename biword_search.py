from preprocessing import preprocess_text_stemming

def biword_query_search(query, biword_index):
    # Convert the query to lowercase
    query = query.casefold()
    # Preprocess the query and convert it to a tuple of biwords
    query_biword = tuple(preprocess_text_stemming(query))
    # Return the documents that contain the biword
    return biword_index[query_biword]