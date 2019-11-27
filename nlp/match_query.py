from glove_cluster import TextMatcher
import pandas as pd
import json

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
with open('../query.json', 'r') as f:
    q = json.load(f)

print(q)
index=Searcher.get_results(q['role'].split(' '),sentences)

pd.DataFrame(df.iloc[index]).T.to_json('../result.json')
