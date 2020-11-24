from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.metrics import explained_variance_score

df = pd.read_csv('../data/processed_removed_outliers_normalized.csv')
df = df.iloc[:,1:]
x_varLog = []
y_varLog = []
thetaLog = []
testSetSize = 1000

f = open("../models/logistic.txt", 'r')

for i in f.readline().split(','):
    thetaLog.append(float(i))
f.close()


for i in range(2000 + testSetSize):
    tempListLog = []
    for e in df.keys():
        if(e == 'price'):
            y_varLog.append(((df[e][i]) / 6) +0.5)
        else:
            tempListLog.append(df[e][i])
    tempListLog.append(1)
    x_varLog.append(tempListLog)

def predict(x, thet):
    sum = 0
    for i in range(len(x)):
        sum+= x[i] * thet[i]
    return (1 / (1 + (2.7183**-sum)))

def compare(i):
    pred = ((predict(x_varLog[i], thetaLog) - 0.5) * 6) 
    pri = ((y_varLog[i] - 0.5) * 6) 
    
    predscaled = (pred* 367127) + 540088
    priscaled = (pri* 367127) + 540088
    diffscaled = abs(predscaled - priscaled)

    space1  = ' ' * (20 - len(str(predscaled)))
    space2  = ' ' * abs(len(str(round(predscaled))) - len(str(round(diffscaled))))

    print(i, (' ' * (5-len(str(i) )) ),'prediction|price:', predscaled, space1, priscaled)
    print(i, (' ' * (5-len(str(i) )) ),'difference:      ',space2 + str(diffscaled))

    return abs(pred - pri)

def compareAvrage():
    pred = df.mean(axis=0)['price']
    pri = ((y_varLog[i] - 0.5) * 6)
    return abs(pred - pri)


NormalizedMeanAbsoluteErrorLogistic= 0
NormalizedMeanAbsoluteErrorFromAverage = 0
MeanAbsoluteErrorLogistic = 0
MeanAbsoluteErrorFromAverage = 0

for i in range(2000, 2000 + testSetSize):
    MeanAbsoluteErrorLogistic += ((compare(i) * 367127) + 540088) / testSetSize
    MeanAbsoluteErrorFromAverage += ((compareAvrage() * 367127) + 540088)/ testSetSize
    NormalizedMeanAbsoluteErrorLogistic += compare(i)/ testSetSize
    NormalizedMeanAbsoluteErrorFromAverage += compareAvrage()/ testSetSize

print ("Normalized MAE using logistic regression:", NormalizedMeanAbsoluteErrorLogistic)
print ("Normalized MAE using guess average:      ",NormalizedMeanAbsoluteErrorFromAverage)

print ("MAE using logistic regression:", MeanAbsoluteErrorLogistic)
print ("MAE using guess average:      ", MeanAbsoluteErrorFromAverage)