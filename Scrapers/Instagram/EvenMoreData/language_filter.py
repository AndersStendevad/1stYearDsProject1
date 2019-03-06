from langdetect import detect

def language_filter(infile, outfile, language):
    inf = open(infile)
    outf = open(outfile, "w")
    for line in inf:
        newline = line.strip().split("\n \n")
        for i in newline:
            try:    
                if detect(i) == language and i != "":
                    outf.write(i)
                    outf.write("\n")
            except Exception:
                pass
    inf.close()
    outf.close()

inlist = ["amager.txt", "kbhk.txt", "nørrebro.txt", "østerbro.txt", "torvehallerne.txt", "valby.txt", "vesterbro.txt"]
#outlist = ["amager_lang-DA.txt", "kbhk_lang-DA.txt", "nørrebro_lang-DA.txt", "østerbro_lang-DA.txt", "torvehallerne_lang-DA.txt", "valby_lang-DA.txt", "vesterbro_lang-DA.txt"]

for i in inlist:
    j = i.split('.')
    language_filter(i, j[0] + "_lang-DA.txt", "da")