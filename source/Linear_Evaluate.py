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
#import training set data (only for finding average)
Y_training = pd.read_csv('../data/Y_training')

#import fitted model
f = open("../models/linear.txt", 'r')
#linear model coefficients
theta = []
for i in f.readline().split(','):
    theta.append(float(i))
f.close()

#initialize variables
#size of the test set
testSetSize = len(X_test)
x_var = []
y_var = []

#format data so its corresponding to represenatation in "linear_regression_from_scrtach.py"
for i in range(len(X_test)):
    tempList = []
    y_var.append(Y_test['price'][i])
    for e in X_test.keys():
        tempList.append(X_test[e][i])
    #add a constant term (konstantledd)
    tempList.append(1)
    x_var.append(tempList)

#make prediction from input and linear combination with theta as cofficients
def predict(x, thet):
    sum = 0
    for i in range(len(x)):
        sum+= x[i] * thet[i]
    return sum

#compares entry i's prediction to actual value and returns absolute differance
def compareAbs(i):
    pred = predict(x_var[i], theta)
    pri = y_var[i]
    return abs(pred - pri)

#compares entry i's prediction to actual value and returns squared differance
def compareSquare(i):
    pred = predict(x_var[i], theta)
    pri = y_var[i]
    return (pred - pri)**2

#compares avrage of the training set to actual value and returns absolute differance
def compareAvrageAbs(i):
    pred = Y_training.mean(axis=0)['price']
    pri = y_var[i]
    return abs(pred - pri)

#compares avrage of the training set to actual value and returns squared differance
def compareAvrageSquare(i):
    pred = Y_training.mean(axis=0)['price']
    pri = y_var[i]
    return (pred - pri)**2

#set up variables for MAE and MSE
MeanAbsoluteErrorLinear = 0
MeanSquarerrorLinear = 0
MeanAbsoluteErrorFromAverage = 0
MeanSquareErrorFromAverage = 0

#Calculate MAE and MSE for guess average and linear model
for i in range(testSetSize):

    MeanAbsoluteErrorLinear += compareAbs(i)/ testSetSize
    MeanSquarerrorLinear += compareSquare(i)/ testSetSize
    MeanAbsoluteErrorFromAverage += compareAvrageAbs(i)/ testSetSize
    MeanSquareErrorFromAverage += compareAvrageSquare(i)/ testSetSize

#print out and save results

stringOutput = ("MAE using linear regression:" + str(MeanAbsoluteErrorLinear) + 
"\nMAE using guess average:      " + str(MeanAbsoluteErrorFromAverage) + 
"\nMSE using linear regression:" + str(MeanSquarerrorLinear) + 
"\nMSE using guess average:      " + str(MeanSquareErrorFromAverage))

print (stringOutput)

f = open("../results/linearResults.txt", 'w')

f.write(stringOutput)
f.close()
