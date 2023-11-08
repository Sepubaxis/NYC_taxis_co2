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


@app.get("/Autos electricos recomendados")
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




import joblib

# Cargar el modelo Random Forest previamente entrenado
model_rf = joblib.load('random_forest_model.pkl')


@app.get("/Zonas demanda")
def prediccion(ID_destino: int, dia: int, hora: int):
    # Validar que los valores de día, hora e ID estén dentro del rango deseado
    if dia < 1 or dia > 7:
        return {"error": "El valor de día debe estar entre 1 y 7."}
    if hora < 1 or hora > 24:
        return {"error": "El valor de hora debe estar entre 1 y 24."}
    if ID_destino < 1 or ID_destino > 263:
        return {"error": "El valor de zona_actual debe estar entre 1 y 263."}

    localizacion = {
        'PULocationID': [ID_destino],
        'dayofweek': [dia],
        'hour': [hora],
    }
    loc = pd.DataFrame(localizacion)

    # Realizar la predicción de probabilidad de encontrar un viaje en la zona actual
    demanda = model_rf.predict(loc)

    # Obtener las 5 zonas más probables
    zonas_probables = zonas_mas_probables(model_rf, ID_destino, hora, dia, 5)

    # Normalizar las probabilidades 
    suma_total = sum(zonas_probables)
    probabilidad_en_esa_zona = min(demanda[0] / suma_total, 1) * 100

    return {
        "probabilidad_en_esa_zona": round(probabilidad_en_esa_zona, 2),
        "demas_zonas_probables": zonas_probables
    }

def zonas_mas_probables(model_rf, zona_actual, hora, dia_semana, top_n):
    zonas = list(range(1, 263))  # Rango de IDs de ubicación
    zonas.remove(zona_actual)  
    probabilidades = []

    for zona in zonas:
        localizacion = {
            'PULocationID': [zona],
            'dayofweek': [dia_semana],
            'hour': [hora],
        }
        loc = pd.DataFrame(localizacion)
        probabilidad = model_rf.predict(loc)
        probabilidades.append((zona, probabilidad[0]))

    # Ordenar por probabilidad en orden descendente
    probabilidades.sort(key=lambda x: x[1], reverse=True)

    # Obtener las top_n zonas más probables 
    zonas_probables = [zona for zona, probabilidad in probabilidades[:top_n]]

    return zonas_probables

