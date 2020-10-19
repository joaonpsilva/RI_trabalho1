from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


class Tokenizer3Porter:

    def __init__(self, stopwordsfile):
        self.stemmer = PorterStemmer()
        self.stopwords = self.buildStopWords(stopwordsfile)

    def buildStopWords(self, file):
        reader = open(file, 'r')
        return reader.read().splitlines()

    def removeStopWords(self, words):
        return [word for word in words if not word in self.stopwords]

    def process(self, words):
        words = self.removeStopWords(words)
        words = [self.stemmer.stem(word) for word in words]

        return words
