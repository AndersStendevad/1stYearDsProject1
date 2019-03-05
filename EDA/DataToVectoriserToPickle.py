import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import FeatureUnion
import pickle
import os
import re

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
	streets = re.findall(r"(\b\w*gade\w*\b)", corpus[0])
	shops = re.findall(r"(\b\w*shop\w*\b)", corpus[0])
	places = ['amagerbrogade', 'remix5', 'remix', 'torsdage','fredag','mandag','onsdage','korsgade','bragesgade','valhalsgade', 'kapelvej','dkårhusgade','dkøsterbrogade','dkblegdamsvej','øårhusgade','dkjagtvej','dklyngbyvej','dkserridslevvej','dksionsgade', 'telefon', 'bellmansgade', 'tirsdag','onsdag','amagers', 'nordrefrihavnsgade', 'viborggade', 'nordhavn', 'trianglen', 'østerbros', 'lyngbyvej', 'torvehallernes', 'frihavnsgade', 'strandboulevarden', 'nyhavn', 'østebros', 'nørrebrogade', 'nørrebros', 'nytorv', 'kastrup', 'copenhagen', 'amager', 'amagerstrand', 'nyamagerbrogade', 'københavn', 'amagerbro', 'sundby', 'tårnby', 'kbh', 'kbhk', 'reffen', 'reffencph', 'nørrebro', 'ravnsborggade', 'nordvest', 'holbæk', 'christianshavn', 'nørrebronx', 'frederiksberg', 'valby', 'hvidovre', 'torvehallerne', 'torvehallernekbh', 'elledanmark', 'valby', 'vesterbro', 'vesterbrogade', 'vesterbronx', 'istedgade', 'saxogade', 'istedgade110', 'aarhus', 'odense', 'aalborg', 'hellerup', 'østerbro', 'cph', 'blågårdsgade', 'cphk', 'upcopenhagen', 'kl', '02', '15', '18', '2010', 'lyngby', 'oslo', 'norge', 'stellaalice', 'østerbrogade', 'odensegade', 'århusgade', 'cm', 'str', 'kbhv', 'norway', 'vesterbros', 'hasserisgade', 'prinsensgade', 'kirkegårdsgade', 'prinsensgade', 'kødbyen', 'langgade', 'valbys', 'værkstedvej', 'skolegade', 'sydhavnen', 'torvehaller', 'torvehallen', 'torvehal', 'valdemarsgade', 'vesterbroere', 'vesterbroerne', 'jernbanevej', 'kulbanevej', 'voervadsbro', 'østerbroere', 'vestergård', 'svanemøllen', 'ryparken' ]
	streets.extend(places)
	streets.extend(shops)
	vectorizer = TfidfVectorizer(lowercase=True, preprocessor=None, tokenizer=None, analyzer="word" ,stop_words=set(streets), token_pattern=r"(?u)\b\w\w\w\w+\b",ngram_range=(1, 1),max_df=0.5, vocabulary=None)
	X = vectorizer.fit_transform(corpus)
    #print(vectorizer.get_feature_names())
	print(X.shape)
	pickle.dump(sorted(vectorizer.vocabulary_.items()), open("vocabulary.pickle", "wb"))
	pickle.dump(X, open("tfidf.pickle", "wb"))

main()
