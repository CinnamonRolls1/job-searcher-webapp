from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from copy import deepcopy
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

class cluster:
    def __init__(self):
        pass

    def build(self,df) :
        #TF-IDF Vectorization
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(df['TITLE'].values.astype('U'))
        X = np.append(X,vectorizer.fit_transform(df['DESCRIPTION'].values.astype('U')),axis=1)

        # #Label Encoding of output column
        # y = self.data_frame['IT'].values
        # labelencoder = LabelEncoder()
        # y = labelencoder.fit_transform(y)
        #
        # #train/test split
        # X_train,X_test,y_train, y_test = train_test_split(X,y)

        #train cluster model
        model = KMeans(n_clusters=2, init='k-means++', max_iter=100000, n_init=1)
        model.fit(X)
        y_predict = model.predict(X)

        # #results
        # acc_train = accuracy_score(y_train,y_train_predict)
        # acc_test = accuracy_score(y_test,y_test_predict)
        #
        # print("training accuracy: ",acc_train)
        # print("test accuracy: ",acc_test)



def main():
    df = pd.read_json("../scraper/scraper/indeed_data.json",orient='records')
    obj=cluster()
    print(df)
    #print(obj.data_frame)
    #obj.build(df)
    #obj.kmeans()

if __name__ == '__main__':
    main()
