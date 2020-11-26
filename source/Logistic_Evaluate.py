from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.metrics import explained_variance_score

#import test data
X_test = pd.read_csv('../data/x_test').iloc[:, 1:]
Y_test = pd.read_csv('../data/Y_test')
#import training set data (only for finding average, max and min)
Y_training = pd.read_csv('../data/Y_training')

#import fitted model
f = open("../models/logistic.txt", 'r')
#logistic model coefficients
thetaLog = []
for i in f.readline().split(','):
    thetaLog.append(float(i))
f.close()

#initialize variables
#size of the test set
x_varLog = []
y_varLog = []
testSetSize = len(X_test)
min = Y_training.min(axis=0)['price']
max = Y_training.max(axis=0)['price']


#format data so its corresponding to represenatation in "linear_regression_from_scrtach.py"
for i in range(len(X_test)):
    tempList = []
    y_varLog.append(Y_test['price'][i])
    for e in X_test.keys():
        tempList.append(X_test[e][i])
    #add a constant term (konstantledd)
    tempList.append(1)
    x_varLog.append(tempList)

#make prediction from logistic funtion of the linear combination of inputs with theta as cofficients
def predict(x, thet):
    sum = 0
    for i in range(len(x)):
        sum+= x[i] * thet[i]
    return (1 / (1 + (2.7183**-sum)))

#compares entry i's prediction to actual value and returns absolute differance
def compareAbs(i):
    pred = predict(x_varLog[i], thetaLog) * (max-min) + min
    pri = y_varLog[i]
    return abs(pred - pri)

#compares entry i's prediction to actual value and returns squared differance
def compareSquare(i):
    pred = predict(x_varLog[i], thetaLog) * (max-min) + min
    pri = y_varLog[i]
    return (pred - pri)**2

#compares avrage of the training set to actual value and returns absolute differance
def compareAvrageAbs(i):
    pred = Y_training.mean(axis=0)['price']
    pri = y_varLog[i]
    return abs(pred - pri)

#compares avrage of the training set to actual value and returns squared differance
def compareAvrageSquare(i):
    pred = Y_training.mean(axis=0)['price']
    pri = y_varLog[i]
    return (pred - pri)**2

#set up variables for MAE and MSE
MeanAbsoluteErrorLogistic = 0
MeanAbsoluteErrorFromAverage = 0
MeanSquaredErrorLogistic = 0
MeanSquaredErrorFromAverage = 0

#Calculate MAE and MSE for guess average and linear model
for i in range(testSetSize):
    MeanAbsoluteErrorLogistic += compareAbs(i)/ testSetSize
    MeanSquaredErrorLogistic += compareSquare(i)/ testSetSize
    MeanAbsoluteErrorFromAverage += compareAvrageAbs(i)/ testSetSize
    MeanSquaredErrorFromAverage += compareAvrageSquare(i)/ testSetSize

#print out results
print ("MAE using logistic regression:", MeanAbsoluteErrorLogistic)
print ("MAE using guess average:      ", MeanAbsoluteErrorFromAverage)

print ("MSE using logistic regression:", MeanSquaredErrorLogistic)
print ("MSE using guess average:      ", MeanSquaredErrorFromAverage)
