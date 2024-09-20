import re

def boolean_query_search(query, index):
    # Convert the query to lowercase
    query = query.casefold()
    # Extract individual terms from the query
    query_terms = re.findall(r'\w+', query)
    # Initialize the result set with the documents containing the first term
    result_docs = set(index[query_terms[0]])
    token_idx = 1

    # Process the query terms with boolean operators
    while token_idx < len(query_terms):
        operator = query_terms[token_idx]
        next_docs = set(index[query_terms[token_idx + 1]])

        if operator == 'and':
            result_docs &= next_docs
        elif operator == 'or':
            result_docs |= next_docs
        elif operator == 'not':
            result_docs -= next_docs

        token_idx += 2

    return result_docs