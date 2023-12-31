import nltk
from nltk.tokenize import word_tokenize

def tokenizer(text):
    return word_tokenize(text.lower())
