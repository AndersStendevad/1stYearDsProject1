from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import os
import nltk

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print ("Topic", topic_idx)
        print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words-1:-1]]))

danish_stopwords = nltk.corpus.stopwords.words('danish')
extra_stopwords = ["kr", "så", "str", "to", "of", "dk", "www", "https", "vores", "mere", "kan", "and", "in", "is", "ved"]
for i in extra_stopwords:
    danish_stopwords.append(i)

def lda1(filename):
    with open(filename) as f:
        tf_vectorizer = CountVectorizer(max_features=10000, stop_words=danish_stopwords)
        tf = tf_vectorizer.fit_transform(open(filename))
        tf_feature_names = tf_vectorizer.get_feature_names()
        lda = LatentDirichletAllocation(n_components=10, random_state=0, learning_method = 'online')
        lda.fit_transform(tf)
        print(lda.components_)
        display_topics(lda, tf_feature_names, 10)

#lda1("/home/seb/1stYearDsProject1/Instagram/data/amager_lang-DA.txt")
lda1("/Users/neil/Documents/GitHub/1stYearDsProject1/Events/Amager_clean_clean_version.txt")