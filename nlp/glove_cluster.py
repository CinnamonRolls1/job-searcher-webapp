import itertools
from gensim.models.word2vec import Text8Corpus
from gensim.models import Word2Vec
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import pandas as pd
import numpy as np

def remove_stopwords(sentences) :
    new_sentences = []
    for i in sentences :
        new_sentence=[]
        for j in i :
            if j not in (stop_words):
                new_sentence.append(j)

        new_sentences.append(new_sentence)

    return new_sentences

df = pd.read_csv('data job posts.csv')

sentences = df['Title'].values
new_sentences = []
for i in sentences:
    if type(i) == str :
        new_sentences.append(i)


sentences = new_sentences
sentences = list(map(lambda x : x.lower(),sentences))
sentences = list(map(lambda x: x.split(" "),sentences))

sentences = remove_stopwords(sentences)


model = Word2Vec(sentences)


X=model[model.wv.vocab]

print(model.n_similarity(['intern','software'],model.wv.vocab))
