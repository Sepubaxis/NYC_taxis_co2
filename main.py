from fastapi import FastAPI
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

app = FastAPI()

df = pd.read_csv('Autos Electicos.csv')
knn = NearestNeighbors(n_neighbors=10, metric='euclidean')
knn.fit(df[['Price', 'FastCharge_MiH']])


@app.get("/Autos-electricos-recomendados")
def recomendacion(price: float, fastcharge: float):
    # Asegúrate de que los valores de entrada sean números de punto flotante
    if not isinstance(price, float) or not isinstance(fastcharge, float):
        return {"error": "Los valores de entrada deben ser números de punto flotante"}

    query = [[price, fastcharge]]
    distances, indices = knn.kneighbors(query)
    recommended_indices = indices[0][1:]
    
    # Usar np.any() para verificar si recommended_indices no está vacío
    if not np.any(recommended_indices):
        return {"message": "No se encontraron recomendaciones"}
    
    recommended_cars = df.iloc[recommended_indices]
    return recommended_cars.to_dict(orient='records')


#--------------------------------------------------------------------------------------------------------


