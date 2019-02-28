from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import os

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print ("Topic", topic_idx)
        # length of feature names is 8172 at max, but it tries accessing indices up to 30k
        print([i for i in topic.argsort()[:-no_top_words-1:-1]])
        #" ".join([feature_names[i]

def readFilesToList():
    corpus = []
    for file in os.listdir("./Data/"):
        with open("./Data/"+file,encoding='utf-8') as TempFile:
            Data = TempFile.read()
            corpus.append(Data.strip("\n"))
    return corpus

def Sklearn(corpus):
    vectorizer = TfidfVectorizer(
    lowercase=True, preprocessor=None,
    tokenizer=None, stop_words=None,
    ngram_range=(1, 1),vocabulary=None,
    )
    X = vectorizer.fit_transform(corpus)
    return X, vectorizer
    
corpus = readFilesToList()
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=10000, stop_words='english')
tf = tf_vectorizer.fit_transform(corpus)
tf_feature_names = tf_vectorizer.get_feature_names()

    

X = Sklearn(corpus)[0]
vectorizer = Sklearn(corpus)[1]
lda = LatentDirichletAllocation(n_components=10, random_state=0, learning_method = 'online')
lda.fit_transform(X)
print(lda.components_)
display_topics(lda, tf_feature_names, 10)