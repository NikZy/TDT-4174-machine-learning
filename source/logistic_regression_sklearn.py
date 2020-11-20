
# SkLearn Linear regression
from sklearn.linear_model import LogisticRegression
from joblib import dump
from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.metrics import explained_variance_score
import scipy as stats
import csv

dataset = pd.read_csv('../data/processed_removed_outliers_normalized.csv')

scaler = load('../models/datascaler.joblib')
X_training = pd.read_csv('../data/x_training').iloc[:, 1:]
X_test = pd.read_csv('../data/x_test').iloc[:, 1:]
Y_training = pd.read_csv('../data/y_training').iloc[:, 1]
Y_test = pd.read_csv('../data/Y_test').iloc[:, 1]

Y_training = stats.stats.zscore(Y_training)


regressor = LogisticRegression()
regressor.fit(X_training, Y_training)

# Persist model
dump(regressor, '../models/logistic-regression-sklearn.joblib')

# Predicting the Test set results
y_pred = regressor.predict(X_test)

explain = regressor.score(X_test, Y_test)

linear_explained_var = explained_variance_score(y_pred, Y_test)
print(linear_explained_var)

score_train = regressor.score(X_training, Y_training)

# Return the coefficient of determination R^2 of the prediction.
score_test = regressor.score(X_test, Y_test)


dt_predict = regressor.predict(X_test)

explain = explained_variance_score(dt_predict, Y_test)


dt_mean_error = (abs(dt_predict - Y_test) / len(Y_test)).sum()

dt_mean_squared_error = (abs(dt_predict - Y_test)**2 / len(Y_test)).sum()

results = {
    "mean_error": str(dt_mean_error),
    "mean_squared_error": str(dt_mean_squared_error),
    "explained_variance_score": str(explain)
}

with open('../results/logistic_regression_sklearn_results.csv', 'w') as f:  # Just use 'w' mode in 4.x
    writer = csv.DictWriter(f, fieldnames=results.keys())
    writer.writerow(results)

# Persist results
print("Training score: " + str(score_train))
print("Testing score: " + str(score_test))

print("Linear regression  mean error: {}".format(dt_mean_error))
print("Linear regression mean sqaured error: {}".format(dt_mean_squared_error))
