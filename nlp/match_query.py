from glove_cluster import TextMatcher
import pandas as pd

Searcher = TextMatcher()
Searcher.load('indeed_data.bin')
print(list(Searcher.model.wv.vocab))
sentences = pd.read_csv('../datasets/indeed_data.csv').iloc[:,0].values
#print(sentences)
new_sentences = []
for i in sentences:
    if type(i) == str :
        new_sentences.append(i)


sentences = new_sentences
sentences = list(map(lambda x : x.lower(),sentences))
sentences = list(map(lambda x: x.split(" "),sentences))

sentences = Searcher.remove_stopwords(sentences)
Searcher.get_results(['administrator','controller','project'],sentences)
