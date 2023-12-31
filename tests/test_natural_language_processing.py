import unittest
from fake_news_detection import tokenizer, stop_words, stemmer

class TestNaturalLanguageProcessing(unittest.TestCase):
    def test_tokenizer(self):
        article = 'This is some news! With multiple sentences and words.'
        tokens = tokenizer(article)
        self.assertEqual(len(tokens), 10)

    def test_stop_words(self):
        article = 'The quick brown fox jumps over the lazy dog.'
        tokens = [token for token in tokenizer(article) if token not in stop_words]
        self.assertEqual(len(tokens), 5)

    def test_stemmer(self):
        article = 'The quick brown fox jumps over the lazy dog.'
        tokens = [stemmer(token) for token in tokenizer(article)]
        self.assertEqual(len(tokens), 5)
