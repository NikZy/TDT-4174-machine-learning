
from joblib import dump, load
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import tree
from sklearn.metrics import explained_variance_score

dataset = pd.read_csv('../data/processed_removed_outliers_normalized.csv')

# and all attributes along 1-axis, except index 1, which is price
# All values along 0-axis and, but only the price column
X = dataset.iloc[:, 2:]  # Splice dataframe: All items along 0-axis (values)
Y = dataset.iloc[:, 1]
#Y_scaler = scaler.fit_transform(Y)

# Split data into training data and test data
X_training, X_test, Y_training, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0)

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

results = {
    "mean_error": dt_mean_error,
    "mean_squared_error": dt_mean_squared_error,
    "unoptimized_mean_squared_error": dt_mean_error_unoptimized,
    "unoptimized_mean_error": dt_mean_error_unoptimized,
    "explained_variance_score": explain
}

# Persist results
dump(results, "../results/decision_tree_results.py")
print("Training score default model: " + str(score_train_default))
print("Testing score default model: " + str(score_test_default))

print("Training score: " + str(score_train))
print("Testing score: " + str(score_test))

print("Decision tree unoptimised: {}".format(dt_mean_error_unoptimized))
print("Decision tree mean error: {}".format(dt_mean_error))
print("Decision tree mean sqaured error: {}".format(dt_mean_squared_error))
