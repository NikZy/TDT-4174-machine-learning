from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.metrics import explained_variance_score


X_test = pd.read_csv('../data/x_test').iloc[:, 1:]
Y_test = pd.read_csv('../data/Y_test')
#df = pd.read_csv('../data/processed_removed_outliers_normalized.csv')
#df = df.iloc[:,1:]


f = open("../models/linear.txt", 'r')
theta = []
for i in f.readline().split(','):
    theta.append(float(i))
f.close()

4035474464592.696

testSetSize = len(X_test)
x_var = []
y_var = []

x_var = []
y_var = []

#scaler = StandardScaler()
#Y_test = pd.DataFrame(scaler.fit_transform(Y_test), columns=Y_test.columns)

for i in range(len(X_test)):
    tempList = []
    y_var.append(Y_test['price'][i])
    for e in X_test.keys():
        tempList.append(X_test[e][i])
    tempList.append(1)
    x_var.append(tempList)


def predict(x, thet):
    sum = 0
    for i in range(len(x)):
        #print(x[i])
        sum+= x[i] * thet[i]
    return sum

def compareAbs(i):
    pred = predict(x_var[i], theta)
    pri = y_var[i]
    diff = abs(pred - pri)

    space1  = ' ' * (20 - len(str(pred)))
    space2  = ' ' * abs(len(str(round(pred))) - len(str(round(pri))))

    print(i, (' ' * (5-len(str(i) )) ),'prediction|price:', pred, space1, pri)
    print(i, (' ' * (5-len(str(i) )) ),'difference:      ',space2 + str(diff))
    return abs(pred - pri)
def compareSquare(i):
    pred = predict(x_var[i], theta)
    pri = y_var[i]
    diff = (pred - pri)**2

    space1  = ' ' * (20 - len(str(pred)))
    space2  = ' ' * abs(len(str(round(pred))) - len(str(round(pri))))

    print(i, (' ' * (5-len(str(i) )) ),'prediction|price:', pred, space1, pri)
    print(i, (' ' * (5-len(str(i) )) ),'difference:      ',space2 + str(diff))
    return (pred - pri)**2
def compareAvrageAbs():
    pred = Y_test.mean(axis=0)['price']
    pri = y_var[i]
    return abs(pred - pri)
def compareAvrageSquare():
    pred = Y_test.mean(axis=0)['price']
    pri = y_var[i]
    return (pred - pri)**2

MeanAbsoluteErrorLinear = 0
MeanSquarerrorLinear = 0
MeanAbsoluteErrorFromAverage = 0
MeanSquareErrorFromAverage = 0

for i in range(testSetSize):

    MeanAbsoluteErrorLinear += compareAbs(i)/ testSetSize
    MeanSquarerrorLinear += compareSquare(i)/ testSetSize
    MeanAbsoluteErrorFromAverage += compareAvrageAbs()/ testSetSize
    MeanSquareErrorFromAverage += compareAvrageSquare()/ testSetSize

print ("MAE using linear regression:", MeanAbsoluteErrorLinear)
print ("MAE using guess average:    ", MeanAbsoluteErrorFromAverage)

print ("MSE using linear regression:", MeanSquarerrorLinear)
print ("MSE using guess average:    ", MeanSquareErrorFromAverage)
