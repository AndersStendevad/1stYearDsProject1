import pickle
import pandas as pd

filename = "tfidf.pickle"

pickleData = pd.read_pickle(filename).toarray()
dataFrame = pd.DataFrame(pickleData)
print(dataFrame.head())
