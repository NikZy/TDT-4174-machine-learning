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
x_var = []
y_var = []

means = {}
stds = {}
for e in df.keys():
    means[e] = df.mean(axis=0)[e]
    stds[e] = df.std(axis=0)[e]
    print(means[e], e)
for i in range(1000):
    tempList = []
    for e in df.keys():
        if(e == 'price'):
            y_var.append(df[e][i])
        else:
            tempList.append(df[e][i])
    tempList.append(1)
    x_var.append(tempList)
theta = [1] * len(x_var[0])


def firstGradient(thet, y, x,):
    gradient = [0] * len(x[0])
    for j in range(len(x[0])):
        for i in range(len(x)):
            gradient[j] += (y[i] - dotProduct(x[i], thet)) * x[i][j]
    return gradient

def dotProduct(x_i, theta):
    sum = 0
    for j in range(len(x_i)):
        sum += x_i[j] * theta[j]
    return sum

def vectorLength(v):
    sum = 0
    for i in v:
        sum += i ** 2
    return sum ** 0.5


def grafdientDecent(thet, y, x, alpha, error, it):

    gradient = [0] * len(x[0])
    for j in range(len(x[0])):
        for i in range(len(x)):
            gradient[j] += (y[i] - dotProduct(x[i], thet)) * x[i][j]
    for j in range(len(x[0])):
        thet[j] += (alpha * gradient[j])
    if vectorLength(gradient) > error:
        print(vectorLength(gradient))
        it = it+1
        return grafdientDecent(thet, y, x, alpha, error, it)
    else:
        print(it)
        return thet

alpha = vectorLength(firstGradient(theta, y_var, x_var))
theta = [0] * len(x_var[0])


theta = grafdientDecent(theta, y_var, x_var,0.0001, 0.001, 0)  # for 1000


print(theta[0])
thetaString = str(theta[0])
for i in range(1, len(theta)):
    thetaString += ","+str(theta[i])

f = open("../models/linear.txt", 'w')

f.write(thetaString)
f.close()

i = -1
for e in df.keys():
    if(i >= 0): 
        print(e, theta[i])
    i += 1