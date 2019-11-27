from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from copy import deepcopy
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class cluster:
    def __init__(self):
        pass

    def build(self,df) :

        #Imputation
        from sklearn.impute import SimpleImputer
        imp = SimpleImputer(missing_values=np.nan,strategy='mean')
        #imp.fit(df)
        #df = imp.transform(df)

        #TF-IDF Vectorization
        vectorizer = TfidfVectorizer(stop_words='english')
        X1 = vectorizer.fit_transform(df['TITLE'].values.astype('U')).toarray()
        X2=vectorizer.fit_transform(df['DESCRIPTION'].values.astype('U')).toarray()
        print(X1.shape,X2.shape,X1.dtype,X2.dtype)

        X = np.append(X1,X2,axis=1)



        # #Label Encoding of output column
        # y = self.data_frame['IT'].values
        # labelencoder = LabelEncoder()
        # y = labelencoder.fit_transform(y)
        #
        # #train/test split
        # X_train,X_test,y_train, y_test = train_test_split(X,y)

        #train cluster model
        model = KMeans(n_clusters=2, init='k-means++', max_iter=100000, n_init=1)
        print('fitting...')
        model.fit(X)
        print('predicting...')
        y_predict = model.predict(X)

        print(y_predict)

        X = np.append(X,y_predict.reshape(-1,1),axis=1)
        df = pd.concat([df,pd.DataFrame({"cluster":y_predict})],axis=1)
        print(df)
        df.to_json('../output_indeed.json',orient='records')


        # #results
        # acc_train = accuracy_score(y_train,y_train_predict)
        # acc_test = accuracy_score(y_test,y_test_predict)
        #
        # print("training accuracy: ",acc_train)
        # print("test accuracy: ",acc_test)



def main():
    df = pd.read_json("../datasets/indeed_data.json",orient='records')
    obj=cluster()
    #print(df[['SALARY','LOCATION']])
    print(df)
    print(pd.DataFrame(df.iloc[:,0]))
    obj.build(df)
    #obj.kmeans()

if __name__ == '__main__':
    main()
