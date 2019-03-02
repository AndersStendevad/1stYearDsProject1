import re
from nltk.stem.snowball import DanishStemmer
from nltk.corpus import stopwords

stemmer = DanishStemmer()
danish_stopwords = stopwords.words('danish')

with open('Infomedia/infomedia_locations.txt', 'r') as loc:
    for line in loc:
        with open('Infomedia/' + line.strip() + '_infomedia_articles.txt') as text:
            lines = text.readlines()
            lines_no_html = [re.sub('<.*?>', ' ', line) for line in lines]
            lines_no_special = [re.sub('[^a-zåøæ.]', ' ', line.lower()) for line in lines_no_html]
            lines_one_space = [re.sub(' +', ' ', line) for line in lines_no_special]
            list_of_lines = [line.split('.') for line in lines_one_space if len(line) > 1]
        one_big_list = sum(list_of_lines, [])
        #no_stopwords_list = [word for word in one_big_list if i not in danish_stopwords]
        #stemmed_words = [stemmer.stem(word) for word in no_stopwords_list]
        #no_short_words = [word for word in stemmed_words if len(word) > 3]
        log = open('Infomedia/' + line.strip() + '_infomedia_articles_clean.txt', 'w')
        for sentence in one_big_list:
            for word in sentence.split():
                word = stemmer.stem(word)
                if len(word) > 3 and word not in danish_stopwords:
                    log.write(word)
                    log.write(' ')
            log.write('\n')
        log.close() 