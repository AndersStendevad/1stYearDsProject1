### Titel: FacebookProfileCSVtoTxt.py
## By Anders Stendevad
# 19-02-18

import sys

filename = sys.argv[1]

text_file = open("Output.txt", "w")
with open(filename,encoding="utf-8") as file:
    for line in file:
        Data = line.strip().split(",")
        text_file.write(Data[1])
        text_file.write("\n")
text_file.close()
