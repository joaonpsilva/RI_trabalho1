class Posting:

    def __init__(self, docId):
        self.documentId = docId
    
    def __repr__(self):
        return str(self.documentId)