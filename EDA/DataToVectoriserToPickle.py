import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import FeatureUnion
import pickle
import os

files = ['amager.txt','kbhk.txt','nørrebro.txt','østerbro.txt','torvehallerne.txt','valby.txt','vesterbro.txt']

def main():
    corpus = readFilesToList(files)
    Sklearn(corpus)

###

def readFilesToList(files):
    corpus = []
    for file in os.listdir("./Data/"):
        with open("./Data/"+file,encoding='utf-8') as TempFile:
            Data = TempFile.read()
            corpus.append(Data.strip("\n"))
    return corpus

def Sklearn(corpus):
    vectorizer = TfidfVectorizer(
    lowercase=True, preprocessor=None,
    tokenizer=None, stop_words=None,
    ngram_range=(1, 1),vocabulary=None,
    )
    X = vectorizer.fit_transform(corpus)
    #print(vectorizer.get_feature_names())
    print(X.shape)
    pickle.dump(X, open("tfidf.pickle", "wb"))

main()
