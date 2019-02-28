import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import FeatureUnion
import pickle
import os

def main():
    corpus = readFilesToList()
    Sklearn(corpus)

###

def readFilesToList():
    corpus = []
    naborhoods = []
    for file in os.listdir("./Data/"):
        naborhoods.append(file)
        with open("./Data/"+file,encoding='utf-8') as TempFile:
            Data = TempFile.read()
            corpus.append(Data.strip("\n"))
    pickle.dump(naborhoods, open("naborhoods.pickle", "wb"))
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
    pickle.dump(sorted(vectorizer.vocabulary_.items()), open("vocabulary.pickle", "wb"))
    pickle.dump(X, open("tfidf.pickle", "wb"))

main()
