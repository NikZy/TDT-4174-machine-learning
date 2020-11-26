import csv
from joblib import dump, load
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.metrics import explained_variance_score

dataset = pd.read_csv('../data/processed_removed_outliers_normalized.csv')

scaler = load('../models/datascaler.joblib')
X_training = pd.read_csv('../data/x_training').iloc[:, 1:]
X_test = pd.read_csv('../data/x_test').iloc[:, 1:]
Y_training = pd.read_csv('../data/y_training').iloc[:, 1]
Y_test = pd.read_csv('../data/Y_test').iloc[:, 1]

dt_unoptimized = load('../models/decision-tree-default.joblib')
dt_best_model = load('../models/decision-tree-optimized.joblib')

# Train
# Train decision tree model
dt_best_model.fit(X_training, Y_training)
dt_unoptimized.fit(X_training, Y_training)

score_train = dt_best_model.score(X_training, Y_training)

# Return the coefficient of determination R^2 of the prediction.
score_test = dt_best_model.score(X_test, Y_test)

score_train_default = dt_unoptimized.score(X_training, Y_training)

# Return the coefficient of determination R^2 of the prediction.
score_test_default = dt_unoptimized.score(X_test, Y_test)

dt_predict = dt_best_model.predict(X_test)
dt_predict_untuned = dt_unoptimized.predict(X_test)

explain = explained_variance_score(dt_predict, Y_test)

dt_mean_error_unoptimized = (
    abs(dt_predict_untuned - Y_test) / len(Y_test)).sum()

dt_mean_error = (abs(dt_predict - Y_test) / len(Y_test)).sum()

dt_mean_squared_error = (abs(dt_predict - Y_test)**2 / len(Y_test)).sum()

features = np.column_stack(
    (X_training.columns, dt_best_model.feature_importances_))


results = {
    "mean_error": dt_mean_error,
    "mean_squared_error": dt_mean_squared_error,
    "unoptimized_mean_squared_error": dt_mean_error_unoptimized,
    "unoptimized_mean_error": dt_mean_error_unoptimized,
    "explained_variance_score": explain
}

# Persist results
print(features)
print("Tree depth: {}".format(dt_best_model.get_depth()))
print("Tree number of leaves: {}".format(dt_best_model.get_n_leaves()))
print("Training score default model: " + str(score_train_default))
print("Testing score default model: " + str(score_test_default))

print("Training score: " + str(score_train))
print("Testing score: " + str(score_test))

print("Decision tree unoptimised: {}".format(dt_mean_error_unoptimized))
print("Decision tree mean error: {}".format(dt_mean_error))
print("Decision tree mean sqaured error: {}".format(dt_mean_squared_error))

with open('../results/decistion_tree_results.csv', 'w') as f:  # Just use 'w' mode in 3.x
    writer = csv.DictWriter(f, fieldnames=results.keys())
    writer.writerow(results)


print("Training score: " + str(score_train))
print("Testing score: " + str(score_test))

#print out and save results

stringOutput = ( "Tree depth: {}".format(dt_best_model.get_depth()) + "\nTree number of leaves: {}".format(dt_best_model.get_n_leaves()) + "\nTraining score: " + str(score_train) +"\nDecision tree mean error: {}".format(dt_mean_error) +"\nDecision tree mean sqaured error: {}".format(dt_mean_squared_error))


f = open("../results/decisionTreeResults.txt", 'w')

f.write(stringOutput)
f.close()
