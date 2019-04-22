import pandas as pd
import sklearn
from sklearn.datasets import load_boston
import numpy as np
import pickle
from sklearn import linear_model
from sklearn.model_selection import train_test_split




data=pd.read_csv('Social_Network_Ads.csv')
data.Gender.replace( [ 'Male' , 'Female'] , [1,0] , inplace = True )

min=data.EstimatedSalary.min()
max=data.EstimatedSalary.max()
c1=data.EstimatedSalary
c1=(c1-min)/(max-min)
data.EstimatedSalary=c1

data = data._get_numeric_data()

max=0

for i in range (1,100):
    data.reindex(np.random.permutation(data.index))
    data = data._get_numeric_data()
    target = pd.DataFrame(data.Purchased)
    datat = pd.DataFrame(data.drop('Purchased', axis=1))
    datat = pd.DataFrame(datat.drop('User ID', axis=1))
    X_train, X_test, y_train, y_test = train_test_split(datat, target, test_size=0.2)
    model = linear_model.LogisticRegression()
    hi=model.fit(X_train,np.ravel(y_train,order='C'))
    acc=model.score(X_test, y_test)
    print(acc)
    if(acc>max):
        print("saving it")
        # save the model to disk
        filename = "final_model.sav"
        pickle.dump(model, open(filename, 'wb'))
        max=acc


print (max)
