import re
import Stemmer


class Tokenizer2:

    def __init__(self, stopwordsfile):
        self.stemmer = Stemmer.Stemmer("english")
        self.stopwords = self.buildStopWords(stopwordsfile)
        self.specialCases = ["@", "-"]  # Caracters to be specially processed
        self.regex = re.compile('[r"htpps*"]*[^a-zA-Z0-9@\.\' -]')

    def buildStopWords(self, file):
        reader = open(file, 'r')
        return reader.read().splitlines()

    def removeStopWords(self, words):
        return [word for word in words if not word in self.stopwords]

    def matchSpecialCases(self, words):  # Not used since the stemmer already handles the special cases
        return [s for s in words if any(xs in s for xs in self.specialCases)]

    def process(self, *phrases):
        terms = []

        for phrase in phrases:
            phrase = self.regex.sub('', phrase)
            phrase = phrase.lower()
            words = phrase.split(' ')

            words = [word.strip('.\'-') for word in words if len(word.strip('.\'-')) > 2]  # removes small words, https part and remove apostrofes and hifens in the begining and end
            words = self.stemmer.stemWords(words)
            words = self.removeStopWords(words)

            terms += words

        return terms
