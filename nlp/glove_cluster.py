import itertools
from gensim.models.word2vec import Text8Corpus
from gensim.models import Word2Vec
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
import pandas as pd
import numpy as np

class TextMatcher:

    def __init__(self):
        self.model = None

    def remove_stopwords(self,sentences) :
        new_sentences = []
        for i in sentences :
            new_sentence=[]
            for j in i :
                if j not in (stop_words):
                    new_sentence.append(j)

            new_sentences.append(new_sentence)

        return new_sentences

    def build(self, df):

        sentences = df.values
        print(sentences)
        new_sentences = []
        for i in sentences:
            if type(i) == str :
                new_sentences.append(i)


        sentences = new_sentences
        sentences = list(map(lambda x : x.lower(),sentences))
        sentences = list(map(lambda x: x.split(" "),sentences))

        sentences = self.remove_stopwords(sentences)


        self.model = Word2Vec(sentences)

    def save(self,filename) :
        self.model.save(filename)

    def load(self,filename) :
        self.model=Word2Vec.load(filename)

    def get_results(self,sentence,sentences):

        for i in sentences :
            print(i,sentence)
            print(self.model.n_similarity(sentence,i))






def main():
    Searcher = TextMatcher()
    #Searcher.build(pd.read_csv('../datasets/indeed_data.csv').iloc[:,0])
    #Searcher.save('indeed_data.bin')
    Searcher.load('indeed_data.bin')
    pd.DataFrame({'words':list(Searcher.model.wv.vocab)}).to_csv('vocab.csv')
    #print(Searcher.model.wv.vocab)
if __name__ == '__main__':
    main()
