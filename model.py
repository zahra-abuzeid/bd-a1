import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import sys
import os
print("I AM IN MODEL")
df = pd.read_csv('res_dpre.csv')

kmeans_columns = ['age']
le = LabelEncoder()
df['gender_encoded'] = le.fit_transform(df['gender'])
kmeans_columns.append('gender_encoded')
categorical_columns = ['event_location_district', 'event_location_region']
df = pd.get_dummies(df, columns=categorical_columns)

kmeans_columns.extend(df.columns[df.columns.str.startswith('event_location_district_')])
kmeans_columns.extend(df.columns[df.columns.str.startswith('event_location_region_')])
k = 3
data = df[kmeans_columns]

kmeans = KMeans(n_clusters=k, random_state=0)
df['cluster'] = kmeans.fit_predict(data)
cluster_counts = df['cluster'].value_counts().sort_index()


cluster_counts.to_csv('k.txt', header=False)
os.system("./final.sh")