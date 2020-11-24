import pandas as pd
from joblib import dump
import scipy as stats
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


raw_data = pd.read_csv('../data/kc_house_data.csv')
df = raw_data.copy()

# Define a longitude latitude center
latSqrdList = [0]*len(df['lat'])
latcenter = 47.63
longcenter = -122.2
for i in range(len(df['lat'])):
    latSqrdList[i] += (df.at[i, 'lat'] - latcenter) ** 2
    latSqrdList[i] += (df.at[i, 'long'] - longcenter) ** 2
    latSqrdList[i] = -(latSqrdList[i] ** 0.5)

df['center_distance'] = latSqrdList

# Combine built and renovated features
lastFixedList = [0]*len(df['yr_renovated'])
for i in range(len(df['yr_built'])):
    lastFixedList[i] = (2020 - max(df.at[i, 'yr_built'],
                                   df.at[i, 'yr_renovated'])) / df.at[i, 'sqft_living']

df['last_fixed'] = lastFixedList


# Drop unnecessary features
df.drop(['id', 'date', 'yr_renovated', 'yr_built',
         'lat', 'long'], axis=1, inplace=True)

df.to_csv('../data/processed.csv')


# df.to_csv('../data/processed_removed_outliers.csv')

# Normalize values
copy = df.copy()
y = df['price']
copy.drop('price', axis=1)
scaler = StandardScaler()
dataset_scaled = scaler.fit_transform(copy)

dump(scaler, '../models/datascaler.joblib')
# scaled_reverse = scaler.inverse_transform(dataset)
# df_scaled_reverse = pd.DataFrame(scaled_reverse, columns=dataset.columns)
df_norm = pd.DataFrame(dataset_scaled, columns=copy.columns)
df_norm['price'] = df['price']

print(df_norm.min(axis=0)['bedrooms'])


# Remove outliers
z = np.abs(stats.stats.zscore(df_norm))
print(z)
print(np.where(z > 3))
df_norm = df_norm[(z < 3).all(axis=1)]
print(df_norm.min(axis=0)['bedrooms'])
df_norm.to_csv('../data/processed_removed_outliers_normalized.csv')

# Split into train test split
X = df_norm.iloc[:, 1:]  # Splice dataframe: All items along 0-axis (values)

# and all attributes along 1-axis, except index 1, which is price
# All values along 0-axis and, but only the price column
Y = df_norm.iloc[:, 0]
# Y_scaler = scaler.fit_transform(Y)
# Split data into training data and test data
X_training, X_test, Y_training, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=0)

X_training.to_csv('../data/x_training')
X_test.to_csv('../data/x_test')
Y_training.to_csv('../data/y_training')
Y_test.to_csv('../data/Y_test')
print(Y)
