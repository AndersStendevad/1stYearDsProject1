import re
from nltk.corpus import stopwords
import sys


path = sys.argv[1]
name = re.findall(r"[^.]*", path)

def clean(path):
    with open(path) as text:
        lines = text.readlines()
        lines_no_html = [re.sub('<.*?>', ' ', line) for line in lines]
        lines_no_special = [re.sub('[^a-zåøæ]', ' ', line.lower()) for line in lines_no_html]
        lines_one_space = [re.sub(' +', ' ', line) for line in lines_no_special]
        list_of_lines = [line.split() for line in lines_one_space]

    return list_of_lines

log = open(name[0] + '_clean_version.txt', 'w')
clean_text_list = clean(path)
for word in clean_text_list:
    log.write(' '.join(word))
    log.write('\n')
log.close()