import Stemmer

class Tokenizer2:

    def __init__(self, stopwordsfile):
        self.stemmer = Stemmer.Stemmer("english")
        self.stopwords = self.buildStopWords(stopwordsfile)
    
    def buildStopWords(self, file):
        reader = open(file, 'r')
        return reader.read().splitlines()
    
    def removeStopWords(self, words):
        return [word for word in words if not word in self.stopwords] 

    
    def process(self, words):
        words = self.stemmer.stemWords(words)
        words = self.removeStopWords(words)

        return words