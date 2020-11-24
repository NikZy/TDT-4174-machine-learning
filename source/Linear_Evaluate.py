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


f = open("../models/linear.txt", 'r')
theta = []
for i in f.readline().split(','):
    theta.append(float(i))
f.close()



testSetSize = 1000
x_var = []
y_var = []

for i in range(2000 + testSetSize):
    tempList = []
    for e in df.keys():
        if(e == 'price'):
            y_var.append(df[e][i])
        else:
            
            tempList.append(df[e][i])
    tempList.append(1)
    x_var.append(tempList)

def predict(x, thet):
    sum = 0
    for i in range(len(x)):
        sum+= x[i] * thet[i]
    return sum

def compare(i):
    pred = predict(x_var[i], theta)
    pri = y_var[i]
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
    pri = y_var[i]
    return abs(pred - pri)

NormalizedMeanAbsoluteErrorLinear = 0
NormalizedMeanAbsoluteErrorFromAverage = 0
MeanAbsoluteErrorLinear = 0
MeanAbsoluteErrorFromAverage = 0

for i in range(2000, 2000 + testSetSize):
    MeanAbsoluteErrorLinear += ((compare(i) * 367127) + 540088)/ testSetSize
    MeanAbsoluteErrorFromAverage += ((compareAvrage() * 367127) + 540088)/ testSetSize
    NormalizedMeanAbsoluteErrorLinear += compare(i)/ testSetSize
    NormalizedMeanAbsoluteErrorFromAverage += compareAvrage()/ testSetSize

print ("Normalized MAE using linear regression:", NormalizedMeanAbsoluteErrorLinear)
print ("Normalized MAE using guess average:    ",NormalizedMeanAbsoluteErrorFromAverage)

print ("MAE using linear regression:", MeanAbsoluteErrorLinear)
print ("MAE using guess average:    ", MeanAbsoluteErrorFromAverage)