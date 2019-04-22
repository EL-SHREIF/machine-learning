import pandas as pd
import sklearn
from sklearn.datasets import load_boston
from sklearn import linear_model
from sklearn.model_selection import train_test_split

data=pd.read_csv('karam.csv')
data = data._get_numeric_data()

Y = pd.DataFrame(data.price)
X = pd.DataFrame(data.drop('price', axis=1))

model = linear_model.LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 4 )

model.fit(x_train,y_train)

print(model.score(x_test,y_test))

