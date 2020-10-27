import csv
import pandas as pd


class CorpusReader():

    def __init__(self, csvfile, chunkSize=100):
        self.fileIterator = pd.read_csv(csvfile, chunksize=chunkSize, iterator=True)

    def getNextChunk(self):
        try:
            chunk = self.fileIterator.get_chunk()
        except StopIteration:
            return None

        chunk = chunk.dropna(subset=['abstract'])
        chunk = chunk[['doi', 'title', 'abstract']]

        return chunk.values
