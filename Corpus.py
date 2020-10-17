import csv

class CorpusReader():

    def __init__(self, csvfile):
        self.csvfile = csvfile
        self.file = open(self.csvfile, 'r')
        self.reader = csv.reader(self.file, delimiter=',')
        next(self.reader)   #Get rid of headers
        self.doc = self.nextLine()    #Store next value to return so that can check before if exists
    
    def hasNext(self):
        return not self.doc is None
    
    def nextDocument(self):
        temp = self.doc
        self.doc = self.nextLine()
        return temp
 
    def nextLine(self):     #Read line of csv

        while True:

            try:
                line = next(self.reader)
            except StopIteration:           #End of file
                return None
            
            hashid, title, abstract = line[0],line[2],line[7]

            if hashid == '' or abstract == '':       #ignore documents with empty hash and abstarct 
                continue

            return hashid, title, abstract 
