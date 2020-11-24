

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
means = {}
stds = {}
for e in df.keys():
    means[e] = df.mean(axis=0)[e]
    stds[e] = df.std(axis=0)[e]
for i in range(1000):
    tempListLog = []
    for e in df.keys():
        if(e == 'price'):
            y_varLog.append(((df[e][i]) / 6) +0.5)
        else:
            tempListLog.append(df[e][i])
    tempListLog.append(1)
    x_varLog.append(tempListLog)

thetaLog = [0] * len(x_varLog[0])
thetaLog = [-0.031122708341986813,0.029420506270732925,0.16785749486429077,0.03941286959118013,0.023374844258660245,0.49475461564683315,0.11422284507112586,0.02077289165969612,0.17606296942503274,0.1453008172986899,0.07647266349214207,-0.00454123339852773,0.03267837038659651,-0.00020674581626123627,0.1815756421459938,0.14269001561596226,0.032263517924732046]

def firstGradientLog(thet, y, x,):
    gradient = [0] * len(x[0])
    for j in range(len(x[0])):
        for i in range(len(x)):
            gradient[j] += (y[i] - logisticProduct(x[i], thet)) * x[i][j]
    return gradient


def logisticProduct(x_i, theta):
    sum = 0
    for j in range(len(x_i)):
        sum += x_i[j] * theta[j]
    return (1 / (1 + (2.7183**-sum)))


def vectorLength(v):
    sum = 0
    for i in v:
        sum += i ** 2
    return sum ** 0.5


def grafdientDecentLog(thet, y, x, alpha, error, it):

    gradient = [0] * len(x[0])
    for j in range(len(x[0])):
        for i in range(len(x)):
            gradient[j] += (y[i] - logisticProduct(x[i], thet)) * x[i][j]
    print(vectorLength(gradient))
    for j in range(len(x[0])):
        thet[j] += (alpha * gradient[j])
    if vectorLength(gradient) > error:
        it = it+1
        return grafdientDecentLog(thet, y, x, alpha, error, it)
    else:
        print(it)
        return thet


thetaLog = grafdientDecentLog(thetaLog, y_varLog, x_varLog, 0.00085, 0.34, 0)


print(thetaLog[0])
thetaString = str(thetaLog[0])
for i in range(1, len(thetaLog)):
    thetaString += ","+str(thetaLog[i])

f = open("../models/logistic.txt", 'w')

f.write(thetaString)
f.close()