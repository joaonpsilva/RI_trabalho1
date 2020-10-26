from Corpus import CorpusReader
from Tokenizer1 import Tokenizer1
from Tokenizer2 import Tokenizer2
from Posting import Posting
import time
import sys
import heapq
import argparse
import os
import psutil

process = psutil.Process(os.getpid())

class Indexer():
    def __init__(self, corpus, tokenizer):
        self.corpusreader = corpus
        self.tokenizer = tokenizer
        self.idMap = {}
        self.invertedIndex = {}
        self.docID = 1
    
    def hasEnoughMemory(self):
        return True

    def index(self):

        while self.hasEnoughMemory():

            data = self.corpusreader.getNextChunk()
            if data is None:
                print("Finished")
                return

            for document in data:   #Iterate over Chunk of documents
                doi, title, abstract = document[0], document[1], document[2]
                self.idMap[self.docID] = doi

                tokens = self.tokenizer.process(title, abstract)


                for word in tokens:  #Iterate over token of documents

                    if word not in self.invertedIndex:
                        self.invertedIndex[word] = [Posting(self.docID)]
                    else:
                        if self.docID != self.invertedIndex[word][-1].documentId:
                            self.invertedIndex[word].append(Posting(self.docID))
                
                self.docID+=1


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-tokenizer", type=int, choices=[1,2], required=True, help="tokenizer")
    parser.add_argument("-f", type=str, default="all_sources_metadata_2020-03-13.csv", help="text")
    parser.add_argument("-user", type=bool , default=False , help="Opção de menu de pesquisa de termos")
    args = parser.parse_args()

    corpusreader = CorpusReader(args.f)
    if args.tokenizer == 1:
        tokenizer = Tokenizer1()
    else:
        tokenizer = Tokenizer2('snowball_stopwords_EN.txt')

    indexer = Indexer(corpusreader, tokenizer)
    
    t1 = time.time()
    indexer.index()
    t2 = time.time()

    print('seconds: ', t2-t1)
    print('Indexer memory               : ', sys.getsizeof(indexer.invertedIndex))
    print("Total memory used by programm: ", process.memory_info().rss)
    
    keyList = list(indexer.invertedIndex.keys())
    print('Vocabulary size: ', len(keyList))

    lessUsed = heapq.nsmallest(10, indexer.invertedIndex.items(), key=lambda item: (item[0], len(item[1])))
    print("First 10 terms with 1 doc freq: ", [i[0] for i in lessUsed])
    
    mostUsed = heapq.nlargest(10, indexer.invertedIndex.items(), key=lambda item: len(item[1]))
    print("Higher doc freq: ", [(i[0], len(i[1])) for i in mostUsed])

    if args.user:
        while True:
            termo = input("Introduza o termo a pesquisar: ")
            start_time = time.time()
            termo = termo.lower()
            if termo in indexer.invertedIndex.keys():
                print(indexer.invertedIndex[termo])
            else:
                print("Termo não existente")
                print("Keys parecidas: " , [key for key in indexer.invertedIndex.keys() if termo in key and len(termo) > 0])
            print("---Pesquisa feita em %s seconds ---" % (time.time() - start_time))