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
        words2 = []
        words = self.removeStopWords(words)
        for word in words:
            words2.append(self.stemmer.stem(word))

        return words2
