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
        self.data_frame=pd.read_csv("data.csv", usecols = ['Title', 'IT'])
        self.vectorized=None
        self.test=None

    def vectorize(self) :
        #TF-IDF Vectorization
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(self.data_frame['Title'].values.astype('U'))

        #Label Encoding of output column
        y = self.data_frame['IT'].values
        labelencoder = LabelEncoder()
        y = labelencoder.fit_transform(y)

        #train/test split
        X_train,X_test,y_train, y_test = train_test_split(X,y)

        #train cluster model
        model = KMeans(n_clusters=2, init='k-means++', max_iter=100000, n_init=1)
        model.fit(X_train)
        y_train_predict = model.predict(X_train)
        y_test_predict = model.predict(X_test)

        #results
        acc_train = accuracy_score(y_train,y_train_predict)
        acc_test = accuracy_score(y_test,y_test_predict)

        print("training accuracy: ",acc_train)
        print("test accuracy: ",acc_test)


    '''def vectorize(self):
        lis=[]
        le=LabelEncoder()
        vectorizer = TfidfVectorizer(stop_words='english')
        v=TfidfVectorizer(stop_words='english')
        """for i in range(0,len(self.data_frame)-1):
            temp=self.data_frame['Title'][i].apply(lambda x: np.str_(x))
            x=vectorizer.fit_transform(temp)
            lis.append(x)"""
        temp1=self.data_frame['Title'].values.astype('U')
        temp=temp1[:15000]
        temp2=temp1[15001:len(temp1)-1]
        #print(temp)
        vectorizer.fit(temp)
        lis=vectorizer.transform(temp)
        vector=lis.toarray()
        v.fit(temp2)
        self.test=deepcopy(v.transform(temp2))
        #print("lis.shape",lis.shape,type(lis))
        #print("vocabulary",vectorizer.vocabulary)
        self.vectorized= deepcopy(lis)
        #df=pd.DataFrame(lis)
        #df.to_csv('vectorized.csv', index=False)
        #print(lis)
        no_clusters=2
        model = KMeans(n_clusters=no_clusters, init='k-means++', max_iter=100000, n_init=1)
        model.fit(self.vectorized)
        order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names()

        print("cluster members")
        for i in range(no_clusters):
            print("Cluster",i,":")
            for ind in order_centroids[i, :100]:
                print(terms[ind])

        ######################################################
        lis=deepcopy(np.asarray(pd.read_csv("data.csv", usecols=['Title', 'IT'])))
        print(lis)
        #for i in range(len(self.test)):
            #print("*************",temp[i])
            #print("#######3", type(str(temp[i])))
        predicted=model.predict(le.fit_transform(self.test))'''


def main():
    obj=cluster()
    #print(obj.data_frame)
    obj.vectorize()
    #obj.kmeans()

if __name__ == '__main__':
    main()
