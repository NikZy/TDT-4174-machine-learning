

from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.metrics import explained_variance_score

df = pd.read_csv('../data/processed_and_normalized.csv')

x_var = []
y_var = []

x_varLog = []
y_varLog = []
means = {}
stds = {}
for e in df.keys():
    means[e] = df.mean(axis=0)[e]
    stds[e] = df.std(axis=0)[e]
# for i in range(len(df['id'])):
for i in range(1000):
    tempList = []

    tempListLog = []
    remove = False
    for e in df.keys():
        if(e == 'price'):
            y_var.append((df[e][i] - means[e]) / stds[e])
            y_varLog.append((df[e][i] - means[e]) / stds[e])
            if(abs((df[e][i] - means[e]) / stds[e])) > 3:
                remove = True
        else:
            tempList.append((df[e][i] - means[e]) / stds[e])

            tempListLog.append((df[e][i] - means[e]) / stds[e])
            if(abs((df[e][i] - means[e]) / stds[e])) > 3:
                remove = True
    if not remove:
        x_var.append(tempList)
        x_varLog.append(tempListLog)
theta = [1] * len(x_var[0])

thetaLog = [1] * len(x_var[0])


def firstGradient(thet, y, x,):
    gradient = [0] * len(x[0])
    for j in range(len(x[0])):
        for i in range(len(x)):
            gradient[j] += (y[i] - dotProduct(x[i], thet)) * x[i][j]
    return gradient


def firstGradientLog(thet, y, x,):
    gradient = [0] * len(x[0])
    for j in range(len(x[0])):
        for i in range(len(x)):
            gradient[j] += (y[i] - logisticProduct(x[i], thet)) * x[i][j]
    return gradient


def dotProduct(x_i, theta):
    sum = 0
    for j in range(len(x_i)):
        sum += x_i[j] * theta[j]
    return sum


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


alpha = vectorLength(firstGradient(theta, y_var, x_var))
alphaLog = vectorLength(firstGradientLog(theta, y_varLog, x_varLog))
theta = [1] * len(x_var[0])
thetaLog = [-3] * len(x_varLog[0])

# theta = grafdientDecent(theta, y_var, x_var, 0.0000000001325* alpha,1000, 0)#for 10000

theta = grafdientDecent(theta, y_var, x_var,
                        0.0000000238 * alpha, 10, 0)  # for 1000
thetaLog = grafdientDecentLog(
    thetaLog, y_var, x_var, 0.00001 * alphaLog, 860, 0)  # for 1000
print(theta)
print(thetaLog)
# print(grafdientDecent(theta, y_var, x_var, 0.000003067* alpha,10, 0))# for 100
