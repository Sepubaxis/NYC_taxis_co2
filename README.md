# NYC_taxis_co2

### Contexto
En un mundo cada vez más consciente de la importancia de la sostenibilidad y la reducción de la contaminación ambiental, una nueva empresa de taxis está decidida a tomar medidas significativas. Su enfoque se centra en la inversión en vehículos eléctricos como una forma de reducir las emisiones de dióxido de carbono (CO2) y, al mismo tiempo, buscar beneficios económicos mediante la eficiencia de costos.

Para lograr este objetivo, la empresa ha recurrido a una consultora. La misión de esta consultora es evaluar exhaustivamente los datos relacionados con la operación de taxis, las emisiones de CO2 y las tendencias del mercado de vehículos eléctricos. Este análisis permitirá a la empresa tomar decisiones informadas que contribuyan a la reducción de la contaminación y, al mismo tiempo, maximizar sus beneficios económicos.

A través de la exploración de datos y el análisis de tendencias, esperamos aportar soluciones significativas que beneficien tanto a la empresa como al planeta.

### Objetivos
Nuestro equipo se ha comprometido a ayudar a esta empresa en su proceso de toma de decisiones mediante la consecución de los siguientes objetivos:

* **Recopilación y Depuración de Datos:** En primer lugar, nos enfocaremos en la recopilación y depuración de datos de diversas fuentes. Esto incluirá información sobre la operación de taxis en la ciudad de Nueva York, las emisiones de CO2 asociadas a diferentes modelos de automóviles, la disponibilidad de estaciones de carga para vehículos eléctricos y otros conjuntos de datos relevantes

* **Creación de un Data Warehouse en Google Cloud:** Estableceremos un Data Warehouse en la plataforma de Google Cloud.

* **Desarrollo de un Dashboard Interactivo:** Presentaremos un dashboard interactivo que permitirá a los interesados visualizar análisis de valor en función de los KPI (Indicadores Clave de Desempeño) que hemos propuesto.

* **Implementación de un Modelo de Machine Learning:** Desarrollaremos un modelo de Machine Learning que estará diseñado para
***(rellenar más adelante cuando definamos su función específica).***

### KPI (Key Performance Indicator

| KPI | Métrica |
| ------------ | ----------- |
| Porcentaje de reducción de emisiones| reduccion_emisiones = ((Eco2_combustible - Eco2_electricos) / Eco2_combustible) * 100 |
| Distancia promedio por viaje | Distancia Promedio por Viaje = Distancia Total Recorrida / Número Total de Viajes|
| Horario de mayor demanda |Hora de Mayor Demanda = Hora con el Mayor Número de Viajes |
|Diferencia de autonomía entre vehículos de combustión y eléctricos | Km/Litro * Litros vs Km/batería * batería |
| Precio promedio del viaje |Precio Promedio del Viaje = Total de Precios de Viajes / Número Total de Viajes |

### Herramientas Utilizadas:

#### Python:
La herramienta mas importante de nuestro proyecto, cuenta con librerias como **Pandas**, **Numpy**, **Seaborn** y **Matplotlib**. A traves de la comodidad de trabajo que ofrece las Jupyter Notebooks realizamos transformaciones de datos (ETL) y en analizis exploratorio de los datos (EDA)
#### Google Cloud Platform (GCP)
es una de las principales plataformas de servicios en la nube, y su elección como plataforma para alojar y gestionar tus datos y aplicaciones puede depender de varios factores que hacen que sea una opción favorable en muchas situaciones. Aquí te indico algunas razones por las cuales utilizamos GCP:
- Escalabilidad y Flexibilidad: GCP ofrece una amplia gama de servicios que te permiten escalar tus aplicaciones y recursos de manera eficiente. Puedes aumentar o disminuir tus recursos según tus necesidades, lo que es especialmente beneficioso para proyectos que experimentan fluctuaciones en la demanda.
- Potencia y Rendimiento: GCP utiliza la infraestructura de Google, que es conocida por su velocidad y capacidad de procesamiento, esto facilitó el trabajo en equipo desde la nube como alternativa a trabajar de manera local.
- Machine Learning e Inteligencia Artificial: Tiene herramientas de google predefinidas para implementar.
- Big Data y Análisis Avanzado: GCP proporciona servicios y herramientas sólidos para el procesamiento de big data que pudimos utilizar, como BigQuery.

## Roles
En nuestro proyecto, contamos con tres roles fundamentales:

### Data Analysts
Los Data Analysts en nuestro equipo se dedican principalmente a tareas relacionadas con el análisis de datos. Dos de los miembros que desempeñan este rol son:

- Victoria Galvez
- Lorena Ravera

Estos profesionales son responsables de extraer, limpiar, analizar y presentar datos de una manera significativa para tomar decisiones informadas.

### Data Engineers
Los Data Engineers en nuestro equipo se centran principalmente en tareas relacionadas con la ingeniería de datos. Tres de los miembros que desempeñan este rol son:

- Aymara Falcón
- Alexis Alvarez
- Fabrizio Mazzucco

Estos expertos se encargan de diseñar, implementar y mantener las infraestructuras de datos y pipelines que permiten la recopilación, procesamiento y almacenamiento eficiente de los datos.

Cada uno de estos roles es fundamental para el éxito de nuestro proyecto, y juntos trabajamos en colaboración para garantizar la calidad y la utilidad de los datos que manejamos. 

### Machine Learning
El rol de Machine Learning está a cargo de:

- Fabrizio Mazzucco
- Lorena Ravera

Estos profesionales se enfocan en el desarrollo de modelos de machine learning y la implementación de soluciones basadas en inteligencia artificial para mejorar la toma de decisiones y automatizar procesos.

Cada uno de estos roles es fundamental para el éxito de nuestro proyecto, y juntos trabajamos en colaboración para garantizar la calidad y la utilidad de los datos que manejamos, así como para aprovechar el potencial del machine learning en nuestro proyecto.
