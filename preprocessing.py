import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()

    def preprocess(self, text):
        terms = nltk.word_tokenize(text.lower())
        terms = [self.stemmer.stem(self.lemmatizer.lemmatize(term)) for term in terms if term.isalnum() and term not in self.stop_words]
        return terms