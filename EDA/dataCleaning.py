import sys
import pandas as pd
import numpy as np

filename = sys.argv[1]

### Instagram from .txt to CSV

def main():
    instagramIntoDataframe(filename)

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
        print(dataFrame)

main()
