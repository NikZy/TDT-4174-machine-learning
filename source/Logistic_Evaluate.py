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
Y_training = pd.read_csv('../data/Y_training')
#df = pd.read_csv('../data/processed_removed_outliers_normalized.csv')
#df = df.iloc[:,1:]

x_varLog = []
y_varLog = []
thetaLog = []
testSetSize = len(X_test)
min = Y_training.min(axis=0)['price']
max = Y_training.max(axis=0)['price']

f = open("../models/logistic.txt", 'r')

for i in f.readline().split(','):
    thetaLog.append(float(i))
f.close()
#227491.80341677365

for i in range(len(X_test)):
    tempList = []
    y_varLog.append(Y_test['price'][i])
    for e in X_test.keys():
        tempList.append(X_test[e][i])
    tempList.append(1)
    x_varLog.append(tempList)

def predict(x, thet):
    sum = 0
    for i in range(len(x)):
        sum+= x[i] * thet[i]
    return (1 / (1 + (2.7183**-sum)))

def compare(i):
    pred = predict(x_varLog[i], thetaLog) * (max-min) + min
    pri = y_varLog[i]
    
    diff= abs(pred - pri)

    space1  = ' ' * (20 - len(str(pred)))
    space2  = ' ' * abs(len(str(round(pred))) - len(str(round(diff))))

    print(i, (' ' * (5-len(str(i) )) ),'prediction|price:', pred, space1, pri)
    print(i, (' ' * (5-len(str(i) )) ),'difference:      ',space2 + str(diff))

    return abs(pred - pri)

def compareAvrage():
    pred = Y_test.mean(axis=0)['price']
    pri = y_varLog[i]
    return abs(pred - pri)


MeanAbsoluteErrorLogistic = 0
MeanAbsoluteErrorFromAverage = 0

for i in range(testSetSize):
    MeanAbsoluteErrorLogistic += compare(i)/ testSetSize
    MeanAbsoluteErrorFromAverage += compareAvrage()/ testSetSize

print ("MAE using logistic regression:", MeanAbsoluteErrorLogistic)
print ("MAE using guess average:      ", MeanAbsoluteErrorFromAverage)
