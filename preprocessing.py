import re
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Set the NLTK data path
nltk.data.path.append('/Users/nimanshendlay/nltk_data')

# Download the required NLTK data
nltk.download('stopwords', download_dir='/Users/nimanshendlay/nltk_data')
nltk.download('wordnet', download_dir='/Users/nimanshendlay/nltk_data')
nltk.download('punkt', download_dir='/Users/nimanshendlay/nltk_data')
nltk.download('averaged_perceptron_tagger', download_dir='/Users/nimanshendlay/nltk_data')

def get_wordnet_pos(treebank_tag):
    # Map POS tag to first character lemmatize() accepts
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def preprocess_text_lemmatization(text):
    # Convert text to lowercase
    text = text.casefold()
    # Remove non-word characters
    text = re.sub(r'\W+', ' ', text)
    # Tokenize the text
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    # Get POS tags for tokens
    pos_tags = pos_tag(tokens)
    # Lemmatize tokens and remove stopwords
    processed_tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags if word not in stop_words and len(word) > 1]
    return processed_tokens

def preprocess_text_stemming(text):
    # Convert text to lowercase
    text = text.casefold()
    # Remove non-word characters
    text = re.sub(r'\W+', ' ', text)
    # Tokenize the text
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    # Stem tokens and remove stopwords
    processed_tokens = [stemmer.stem(word) for word in tokens if word not in stop_words and len(word) > 1]
    return processed_tokens