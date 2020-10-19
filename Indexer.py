from Corpus import CorpusReader
from Tokenizer1 import Tokenizer1
from Tokenizer2 import Tokenizer2
import time
import sys
import heapq

corpusreader = CorpusReader('all_sources_metadata_2020-03-13.csv')
tokenizer1 = Tokenizer1()
tokenizer2 = Tokenizer2('snowball_stopwords_EN.txt')
idMap = {}
invertedIndex = {}
docID = 1

t1 = time.time()
while corpusreader.hasNext():
    hashid, title, abstract = corpusreader.nextDocument()

    idMap[docID] = hashid

    words = tokenizer1.process(title, abstract)
    words = tokenizer2.process(words)

    for word in words:
        if word not in invertedIndex:
            invertedIndex[word] = [1,docID]
        else:
            if docID != invertedIndex[word][-1]:
                invertedIndex[word].append(docID)
            invertedIndex[word][0]+=1
    
    docID+=1


print(time.time()-t1, ' seconds')
print(sys.getsizeof(invertedIndex), ' bytes')

keyList = list(invertedIndex.keys())
print('Vocabulary size: ', len(keyList))

sortedkeyList = sorted(keyList)
first10 = []
c = 0
for word in sortedkeyList:
    if invertedIndex[word][0] == 1:
        first10.append(word) 
        c+=1
        if c == 10:
            break
print("First 10 terms with 1 doc freq: ", first10)


mostUsed = heapq.nlargest(10, invertedIndex.items(), key=lambda item: item[1][0])
print("Higher doc freq: ", [(i[0], i[1][0]) for i in mostUsed])





#Using tuple (little less eficient but + understandable)
'''
t1 = time.time()
while corpusreader.hasNext():
    hashid, title, abstract = corpusreader.nextDocument()

    idMap[docID] = hashid

    words = tokenizer1.process(title, abstract)
    words = tokenizer2.process(words)

    for word in words:
        if word not in invertedIndex:
            invertedIndex[word] = (1,[docID])
        else:
            if docID != invertedIndex[word][1][-1]:
                temp = invertedIndex[word][1]
                temp.append(docID)
                invertedIndex[word] = (invertedIndex[word][0]+1, temp) 
    
    docID+=1

print(time.time()-t1)
'''
