

from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.metrics import explained_variance_score

#import data
#training data variables
X_training = pd.read_csv('../data/x_training').iloc[:, 1:]
Y_training = pd.read_csv('../data/y_training')
#setting up lists for use in gradient decent
x_varLog = []
y_varLog = []
#find maximum and minimum price in the training set 
min = Y_training.min(axis=0)['price']
max = Y_training.max(axis=0)['price']


#Transposes X_training from the dataframe to a 2d (this is done to better fit our implemntation gradient decent) list and add rescaled Y_training as a list
for i in range(len(X_training)):
    tempList = []
    #rescale price to a number between 0 and one so it can be fitted by a logistic function, this is further explained in our paper 
    y_varLog.append((Y_training['price'][i] - min) / (max - min))
    for e in X_training.keys():
        tempList.append(X_training[e][i])
    #add a constant term (konstantledd) for regression
    tempList.append(1)
    x_varLog.append(tempList)


#import the last fitted model
f = open("../models/logistic.txt", 'r')

#coefficients for the logistic model
thetaLog = []
for i in f.readline().split(','):
    thetaLog.append(float(i))
f.close()


#support function for gradient decent
def logisticProduct(x_i, theta):
    sum = 0
    for j in range(len(x_i)):
        sum += x_i[j] * theta[j]
    return (1 / (1 + (2.7183**-sum)))


#support function for gradient decent
def vectorLength(v):
    sum = 0
    for i in v:
        sum += i ** 2
    return sum ** 0.5


#gradient decent
def grafdientDecentLog(thet, y, x, alpha, error, it):
    #initialize gradient
    gradient = [0] * len(x[0])
    
    #find gradient
    for j in range(len(x[0])):
        for i in range(len(x)):
            gradient[j] += (y[i] - logisticProduct(x[i], thet)) * x[i][j]
    
    #step down by gradient * alpha
    for j in range(len(x[0])):
        thet[j] += (alpha * gradient[j])
    
    #continue itterating if |gradient| > error otherwise return current coefficients
    if vectorLength(gradient) > error:
        it = it+1
        print('Gradient length:', vectorLength(gradient), '\n   ' + 'Iterations:',it)
        return grafdientDecentLog(thet, y, x, alpha, error, it)
    else:
        it = it+1
        print('\n' + 'Total iterations:',it, '\n')
        return thet


#initiate gradient decent with  0.00004 alpha and 0.3 epsilon
epsilon = 0.3
alpha = 0.00004
thetaLog = grafdientDecentLog(thetaLog, y_varLog, x_varLog, alpha, epsilon, 0)


#Write fitted model to file
thetaString = str(thetaLog[0])
for i in range(1, len(thetaLog)):
    thetaString += ","+str(thetaLog[i])

f = open("../models/logistic.txt", 'w')

f.write(thetaString)
f.close()

thetaLog.sort()

i = 0


#print out the model
print('Name                          Normalized Theta     Scaled up theta')
for key in X_training.keys():
    name = key
    theta  = round(thetaLog[i], 6)
    thetaScaled  = round((thetaLog[i] * (max - min) + min), 6)

    decimalPointAligner1 = ''
    if len(str(round(theta, 5))) != len(str(theta)):
        decimalPointAligner1 = ' '
    decimalPointAligner2 = (1 - len(decimalPointAligner1)) * ' '
    if len(str(round(thetaScaled, 5))) != len(str(thetaScaled)):
        decimalPointAligner2 += ' '

    nameSpace = (15 - len(name)) * ' '
    thetaSpace = (20 - len(str(theta))) * ' '
    thetaScaledSpace = (20 - len(str(thetaScaled))) * ' '

    print(name +  nameSpace, decimalPointAligner1, thetaSpace, theta, decimalPointAligner2 ,  thetaScaledSpace, thetaScaled)
    i+=1
