import sys
import pandas as pd
import numpy as np
from contextlib import ExitStack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

files = ['amager.txt','kbhk.txt','nørrebro.txt','østerbro.txt','torvehallerne.txt','valby.txt','vesterbro.txt']

def main():
    corpus = readFilesToList(files)
    Sklearn(corpus)

###

def readFilesToList(files):
    corpus = []
    for i,file in enumerate(files):
        with open(file,encoding='utf-8') as TempFile:
            Data = TempFile.read()
            corpus.append(Data.strip("\n"))
    return corpus

def Sklearn(corpus):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(X.shape)

###

def instagramIntoDataframe(filename):
    dataFrame = pd.DataFrame([])
    with open(filename,encoding="utf-8") as file:
        for line in file:
            Data = line.strip().split()
            for i in Data:
                try:
                    dataFrame.loc[i] += 1
                except:
                    s = pd.Series([1]).rename(i)
                    dataFrame = dataFrame.append(s)
        dataFrame.columns = [filename]
        print(dataFrame.to_dict())



main()
'''
def main():
    with open('amager.txt',encoding='utf-8') as file1:
        with open('kbhk.txt',encoding='utf-8') as file2:
            vectorizer = CountVectorizer()
            X = vectorizer.fit_transform(files)
            #print(vectorizer.get_feature_names())

            print(X.shape)
            print(X.toarray())


files = ['amager.txt','kbhk.txt']
corpus = []
### Instagram from .txt to CSV
for i,file in enumerate(files):
    with open(file,encoding='utf-8') as TempFile:
        Data = TempFile.readlines()
        corpus.append(Data)

files = ['amager.txt','kbhk.txt']
corpus = []
### Instagram from .txt to CSV
for i,file in enumerate(files):
    with open(file,encoding='utf-8') as TempFile:
        Data = TempFile.readlines()
        corpus.append(Data)

with open("amager.txt",encoding='utf-8') as TempFile:
    corpus = TempFile.read()

'''
