from glove_cluster import TextMatcher
import pandas as pd

Searcher = TextMatcher()
Searcher.load('indeed_data.bin')
print(list(Searcher.model.wv.vocab))
df = pd.read_csv('../datasets/indeed_data.csv')
sentences = df.iloc[:,0].values
#print(sentences)
new_sentences = []
for i in sentences:
    if type(i) == str :
        new_sentences.append(i)


sentences = new_sentences
sentences = list(map(lambda x : x.lower(),sentences))
sentences = list(map(lambda x: x.split(" "),sentences))

sentences = Searcher.remove_stopwords(sentences)
index=Searcher.get_results(['administrator','controller','project'],sentences)

pd.DataFrame(df.iloc[index]).T.to_json('../result.json')
