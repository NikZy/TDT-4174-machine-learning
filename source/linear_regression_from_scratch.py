from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.metrics import explained_variance_score

dataset = pd.read_csv('../data/processed_removed_outliers_normalized.csv')

scaler = load('../models/datascaler.joblib')
X_training = pd.read_csv('../data/x_training').iloc[:, 1:]
Y_training = pd.read_csv('../data/y_training')

#df = pd.read_csv('../data/processed_removed_outliers_normalized.csv')
#df = df.iloc[:,1:] 
x_var = []
y_var = []



#scaler = StandardScaler()
#Y_training = pd.DataFrame(scaler.fit_transform(Y_training), columns=Y_training.columns)

for i in range(len(X_training)):
    tempList = []
    y_var.append(Y_training['price'][i])
    #print(Y_training['price'][i])
    for e in X_training.keys():
        tempList.append(X_training[e][i])
        #print(X_training[e][i], e)
    tempList.append(1)
    x_var.append(tempList)


f = open("../models/linear.txt", 'r')
theta = []
for i in f.readline().split(','):
    theta.append(float(i))
f.close()


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
        it = it+1
        print('Gradient length:', vectorLength(gradient), '\n   ' + 'Iterations:',it)
        return grafdientDecent(thet, y, x, alpha, error, it)
    else:
        print('\n' + 'Total iterations:',it, '\n')
        return thet



theta = grafdientDecent(theta, y_var, x_var,0.00003, 0.1, 0)


thetaString = str(theta[0])
for i in range(1, len(theta)):
    thetaString += ","+str(theta[i])

f = open("../models/linear.txt", 'w')

f.write(thetaString)
f.close()

theta.sort()
i = 0


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
