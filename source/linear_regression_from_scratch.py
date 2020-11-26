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
x_var = []
y_var = []

#Transposes X_training from the dataframe to a 2d (this is done to better fit our implemntation gradient decent) list and Y_training as a list
for i in range(len(X_training)):
    tempList = []
    y_var.append(Y_training['price'][i])
    for e in X_training.keys():
        tempList.append(X_training[e][i])
    #add a constant term (konstantledd) for regression
    tempList.append(1)

    x_var.append(tempList)

#import the last fitted model
f = open("../models/linear.txt", 'r')
#coefficients for the linear model
theta = []
for i in f.readline().split(','):
    theta.append(float(i))
f.close()

#support function for gradient decent
def dotProduct(x_i, theta):
    sum = 0
    for j in range(len(x_i)):
        sum += x_i[j] * theta[j]
    return sum

#support function for gradient decent
def vectorLength(v):
    sum = 0
    for i in v:
        sum += i ** 2
    return sum ** 0.5

#gradient decent
def grafdientDecent(thet, y, x, alpha, error, it):
    #initialize gradient
    gradient = [0] * len(x[0])
    
    #find gradient
    for j in range(len(x[0])):
        for i in range(len(x)):
            gradient[j] += (y[i] - dotProduct(x[i], thet)) * x[i][j]
    #step down by gradient * alpha
    for j in range(len(x[0])):
        thet[j] += (alpha * gradient[j])
    #continue itterating if |gradient| > error otherwise return current coefficients
    if vectorLength(gradient) > error:
        it = it+1
        print('Gradient length:', vectorLength(gradient), '\n   ' + 'Iterations:',it)
        return grafdientDecent(thet, y, x, alpha, error, it)
    else:
        it = it+1
        print('\n' + 'Total iterations:',it, '\n')
        return thet

#initiate gradient decent with  0.00003 alpha and 0.1 epsilon
epsilon = 1
alpha = 0.00003
theta = grafdientDecent(theta, y_var, x_var, alpha, epsilon, 0)

#Write fitted model to file
thetaString = str(theta[0])
for i in range(1, len(theta)):
    thetaString += ","+str(theta[i])

f = open("../models/linear.txt", 'w')

f.write(thetaString)
f.close()

theta.sort()
i = 0


#print out the model
print('Name                       Theta')
for key in X_training.keys():
    name = key
    thet  = round(theta[i], 6)

    decimalPointAligner = ''
    if len(str(round(thet, 5))) != len(str(thet)):
        decimalPointAligner = ' '
        
    nameSpace = (15 - len(name)) * ' '
    thetaSpace = (20 - len(str(thet))) * ' '

    print(name + nameSpace , decimalPointAligner, thetaSpace, thet)
    i+=1
