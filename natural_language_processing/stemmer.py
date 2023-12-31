import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def stemmer(word):
    return lemmatizer.lemmatize(word)
