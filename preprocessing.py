import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
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


class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))  # Set of stop words
        self.lemmatizer = WordNetLemmatizer()  # Lemmatizer for reducing words to their base form
        self.stemmer = PorterStemmer()  # Stemmer for reducing words to their root form

    def preprocess(self, text):
        terms = nltk.word_tokenize(text.lower())  # Tokenize and convert text to lowercase
        # Lemmatize, stem, and remove stop words and non-alphanumeric terms
        terms = [self.stemmer.stem(self.lemmatizer.lemmatize(term)) for term in terms if term.isalnum() and term not in self.stop_words]
        return terms