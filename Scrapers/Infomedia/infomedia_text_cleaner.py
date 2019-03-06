import re

with open('infomedia_locations.txt', 'r') as loc:
    for line in loc:
        with open(line.strip() + '_infomedia_articles.txt') as text:
            lines = text.readlines()
            lines_no_html = [re.sub('<.*?>', ' ', line) for line in lines]
            lines_no_special = [re.sub('[^a-zåøæ]', ' ', line.lower()) for line in lines_no_html]
            lines_one_space = [re.sub(' +', ' ', line) for line in lines_no_special]
            log = open(line.strip() + '_infomedia_articles_clean.txt', 'w')
            log.write(lines_one_space[0])
            log.close()