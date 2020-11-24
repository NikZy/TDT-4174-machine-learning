import pandas as pd
import scipy as stats
import numpy as np
from sklearn.preprocessing import StandardScaler


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

# Remove outliers
df[(np.abs(stats.stats.zscore(df)) < 3).all(axis=1)]

df.to_csv('../data/processed_removed_outliers.csv')

# Normalize values
scaler = StandardScaler()
dataset_scaled = scaler.fit_transform(df)

#scaled_reverse = scaler.inverse_transform(dataset)
#df_scaled_reverse = pd.DataFrame(scaled_reverse, columns=dataset.columns)
df_norm = pd.DataFrame(dataset_scaled, columns=df.columns)
print(df_norm.mean(axis=0)["bedrooms"])
df_norm.to_csv('../data/processed_removed_outliers_normalized.csv')
