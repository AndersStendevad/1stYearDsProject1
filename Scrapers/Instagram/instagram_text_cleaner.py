import re
from nltk.stem.snowball import DanishStemmer
from nltk.corpus import stopwords
import sys
import emoji

stemmer = DanishStemmer()

danish_stopwords = stopwords.words('danish')

path = sys.argv[1]
name = re.findall(r"[^.]*", path)

def extract_emojis(str):
    return ''.join(c for c in str if c in emoji.UNICODE_EMOJI)

#with open('/Volumes/ESD-USB/Infomedia/amager_infomedia_articles.txt') as text:
def clean(path):
    with open(path) as text:
        lines = text.readlines()
        extracted_emojis = [extract_emojis(word) for word in lines]
        lines_no_html = [re.sub('<.*?>', ' ', line) for line in lines]
        lines_no_special = [re.sub('[^a-zåøæ]', ' ', line.lower()) for line in lines_no_html]
        lines_one_space = [re.sub(' +', ' ', line) for line in lines_no_special]
        list_of_lines = [line.split() for line in lines_one_space]
    one_big_list = sum(list_of_lines, [])
    no_stopwords_list = [word for word in one_big_list if word not in danish_stopwords]
    stemmed_words = [stemmer.stem(word) for word in no_stopwords_list]
    no_short_words = [word for word in stemmed_words if len(word) > 2]
    return no_short_words, extracted_emojis

log = open(name[0] + '_clean_version.txt', 'w')
clean_text_list = clean(path)[0]
for word in clean_text_list:
    log.write(word)
    log.write(' ')
log.close()

log = open(name[0] + '_emojis.txt', 'w')
clean_text_list = clean(path)[1]
for word in clean_text_list:
    log.write(word)
    log.write(' ')
log.close()