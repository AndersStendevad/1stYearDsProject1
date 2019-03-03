from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import os
import nltk

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print ("Topic", topic_idx)
        print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words-1:-1]]))

danish_stopwords = nltk.corpus.stopwords.words('danish')
danish_stopwords += nltk.corpus.stopwords.words('english')
extra_stopwords = ["kr", "så", "str", "to", "dk", "www", "https", "vores", "mere", "kan", "in", "ved", "kun", "dine" \
                    "amager", "copenhagen", "københavn", "kbhk", "nørrebro", "østerbro", "torvehallerne", "valby", "vesterbro" \
                    "cph", "kbh", "denmark", "danmark", "kl", "stk", "pr", "dkk", "ca", "cm", "dag", "hele", "helt", "es" \
                    "se", "tak", "få", "får"]
for i in extra_stopwords:
    danish_stopwords.append(i)

def lda1(filename):
    with open(filename) as f:
        tf_vectorizer = CountVectorizer(max_features=10000, stop_words=danish_stopwords)
        tf = tf_vectorizer.fit_transform(open(filename))
        tf_feature_names = tf_vectorizer.get_feature_names()
        lda = LatentDirichletAllocation(n_components=6, random_state=0, learning_method = 'online', )
        lda.fit_transform(tf)
        display_topics(lda, tf_feature_names, 10)

<<<<<<< HEAD

inlist = ["amager_lang-DA.txt", "kbhk_lang-DA.txt", "nørrebro_lang-DA.txt", "østerbro_lang-DA.txt", "torvehallerne_lang-DA.txt", "valby_lang-DA.txt", "vesterbro_lang-DA.txt"]
path = "/home/seb/1stYearDsProject1/Instagram/EvenMoreData/"

=======
#lda1("/home/seb/1stYearDsProject1/Instagram/data/amager_lang-DA.txt")
lda1("/Users/neil/Documents/GitHub/1stYearDsProject1/Events/Amager_clean_clean_version.txt")
>>>>>>> refs/remotes/origin/master
