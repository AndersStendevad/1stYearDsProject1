import sys
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

filename = sys.argv[1]

### Instagram from .txt to CSV

def main():
    with open(filename) as file:
        #dict = instagramIntoDataframe(filename)
        #corpus = [filename]
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(file)
        print(vectorizer.get_feature_names())

        print(X.shape)
        print(X.toarray())    


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
