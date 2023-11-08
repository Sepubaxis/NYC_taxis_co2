import pandas as pd
df = pd.read_csv('Autos Electicos.csv')
from sklearn.neighbors import NearestNeighbors
knn = NearestNeighbors(n_neighbors=10, metric='euclidean')
knn.fit(df[['Price', 'FastCharge_MiH']])
def recommend_cars_by_knn(price, fastcharge):
    query = [[price, fastcharge]]
    distances, indices = knn.kneighbors(query)
    recommended_indices = indices[0][1:]  
    return df.iloc[recommended_indices]