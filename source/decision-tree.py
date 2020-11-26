
from joblib import dump
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.metrics import explained_variance_score

dataset = pd.read_csv('../data/processed_removed_outliers_normalized.csv')

X_training = pd.read_csv('../data/x_training').iloc[:, 1:]
X_test = pd.read_csv('../data/x_test').iloc[:, 1:]
Y_training = pd.read_csv('../data/y_training').iloc[:, 1]
Y_test = pd.read_csv('../data/Y_test').iloc[:, 1]

# Possible parameter values
depths = np.arange(1, 21)
num_leafs = [1, 5, 10, 20, 50, 100]
dt_unoptimized = tree.DecisionTreeRegressor()

param_grid = {
    "min_samples_split": [10, 20, 40],
    "max_depth": depths,
    "min_samples_leaf": num_leafs
}

grid_cv_dt = GridSearchCV(estimator=dt_unoptimized,
                          param_grid=param_grid, cv=5)
grid_cv_dt.fit(X_training, Y_training)

print(grid_cv_dt.best_params_)
print(grid_cv_dt.best_score_)

dt_best_model = grid_cv_dt.best_estimator_


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

print("Training score default model: " + str(score_train_default))
print("Testing score default model: " + str(score_test_default))

print("Training score: " + str(score_train))
print("Testing score: " + str(score_test))

# Persist models
dump(dt_unoptimized, '../models/decision-tree-default.joblib')
dump(dt_best_model, '../models/decision-tree-optimized.joblib')
