from Corpus import CorpusReader
from Tokenizer1 import Tokenizer1
from Tokenizer2 import Tokenizer2

corpusreader = CorpusReader('all_sources_metadata_2020-03-13.csv')
tokenizer1 = Tokenizer1()
tokenizer2 = Tokenizer2('snowball_stopwords_EN.txt')
idMap = {}
idCount = 1

while corpusreader.hasNext():
    hashid, title, abstract = corpusreader.nextDocument()

    idMap[idCount] = hashid

    words = tokenizer1.process(title, abstract)
    words = tokenizer2.process(words)

    print(words)
    exit(0)