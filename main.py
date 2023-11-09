from fastapi import FastAPI
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

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

taxi_df = pd.read_csv('taxi_ML.csv')

# Seleccionar las características (X) y la variable objetivo (y)
features = ['PULocationID', 'dayofweek', 'hour']
target = 'demanda'

X = taxi_df[features]
y = taxi_df[target]

# Se dividen los datos en características (X) y etiquetas (y) en conjuntos de entrenamiento (X_train, y_train) y prueba (X_test, y_test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Se crea una instancia del modelo RandomForestRegressor
model_rf = RandomForestRegressor()
model_rf.fit(X_train, y_train)

#Se utilizan las características del conjunto de prueba (X_test) para hacer predicciones
predictions = model_rf.predict(X_test)


@app.get("/prediccion")
def zonas_demanda(ID_localizacion: int, dia: int, hora: int):
    # Validar que los valores de día, hora e ID estén dentro del rango deseado
    if dia < 1 or dia > 7:
        return {"error": "El valor de día debe estar entre 1 y 7."}
    if hora < 1 or hora > 24:
        return {"error": "El valor de hora debe estar entre 1 y 24."}
    if ID_localizacion < 1 or ID_localizacion > 263:
        return {"error": "El valor de zona_actual debe estar entre 1 y 263."}
    dia_semana = dia % 7  # Calcular el día de la semana a partir del día proporcionado

    localizacion = {
        'PULocationID': [ID_localizacion],
        'dayofweek': [dia_semana],
        'hour': [hora],
    }
    loc = pd.DataFrame(localizacion)

    # Realizar la predicción de probabilidad de encontrar un viaje en la zona actual
    demanda = model_rf.predict(loc)

    #Obtener las 5 zonas más probables
    zonas_probables = zonas_mas_probables(model_rf, ID_localizacion, hora, dia_semana, 5)

    return {
        "probabilidad_en_esa_zona": round(demanda[0], 2),
        "demas_zonas_probables": zonas_probables
    } 

def zonas_mas_probables(model_rf, zona_actual, hora, dia_semana, top_n):
    zonas = list(range(1, 264))  #rango de IDs de ubicación
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
