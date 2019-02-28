import pickle
import pandas as pd

filename_tfidf = "tfidf.pickle"
filename_vocabulary = "vocabulary.pickle"
filename_naborhoods = "naborhoods.pickle"

pickleData = pd.read_pickle(filename_tfidf)
vocabulary = pd.read_pickle(filename_vocabulary)
naborhoods = pd.read_pickle(filename_naborhoods)

def main(pickleData,vocabulary):
    dataFrame = pd.DataFrame(pickleData.toarray())
    vocabularyDict = vocabularyIntoDict(vocabulary)
    dataFrame.columns = columnWords(vocabulary)
    dataFrame.index = naborhoods
    print(dataFrame)

###
def columnWords(vocabulary):
    list = []
    for i in range(len(vocabulary)):
        list.append(vocabulary[i][0])
    return list

def vocabularyIntoDict(vocabulary):
    vocabularyDict = {}
    for idx in range(len(vocabulary)):
        vocabularyDict[vocabulary[idx][0]]=vocabulary[idx][1]
    return vocabularyDict

###

main(pickleData,vocabulary)
