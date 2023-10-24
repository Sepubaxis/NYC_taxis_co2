# NYC_taxis_co2
Contexto: Interés en invertir en vehículos eléctricos como una respuesta a la necesidad de reducir la contaminación ambiental y alinearse con las tendencias de mercado, al tiempo que se busca un beneficio de costo de precio.

### Objetivos de la Empresa:

En este contexto, una empresa de servicios de transporte de pasajeros, con experiencia en el sector de micros de media y larga distancia, está interesada en expandir su flota de vehículos para incluir automóviles. Su visión es contribuir a un futuro menos contaminado y adaptarse a las tendencias de mercado actuales. Sin embargo, esta expansión implica la necesidad de comprender la relación entre los medios de transporte particulares y la calidad del aire, así como la contaminación sonora. La empresa se plantea la posibilidad de incorporar vehículos eléctricos en su flota, ya sea de manera parcial o total, como parte de su compromiso ambiental.

### Propuesta de Trabajo:

Para apoyar a esta empresa en su proceso de toma de decisiones, nuestro equipo se ha propuesto una serie de tareas. En primer lugar, recopilaremos y depuraremos datos de diversas fuentes, incluyendo información de taxis en la ciudad de Nueva York, datos de viajes compartidos, datos de calidad del aire, datos de contaminación sonora y otros conjuntos de datos relevantes. Este proceso de creación de un DataWarehouse proporcionará la base necesaria para nuestro análisis.

### Análisis y Soluciones:

Realizaremos un análisis en profundidad para comprender la relación entre variables, incluyendo la relación entre la cantidad de viajes y la contaminación del aire, así como la diferencia en el nivel sonoro entre vehículos a combustión y vehículos eléctricos. También evaluaremos el mercado de vehículos eléctricos, su costo y su viabilidad económica. Para respaldar nuestros hallazgos, emplearemos técnicas de machine learning para predecir patrones de viaje y tomar decisiones basadas en datos.

### Impacto Posible:
La implementación de vehículos eléctricos en la flota de la empresa podría tener un impacto positivo en la reducción de la contaminación del aire y del ruido en la ciudad de Nueva York, alineándose con las tendencias ambientales y mejorando la calidad de vida de sus pasajeros.

Este enfoque multidisciplinario, que combina análisis de datos, conocimientos medioambientales y estrategias de mercado, tiene el potencial de orientar a la empresa hacia un futuro más sostenible y respetuoso con el entorno, al tiempo que garantiza la viabilidad de su expansión en el sector del transporte de pasajeros en automóviles.

### KPI (Key Performance Indicator

| KPI | Métrica |
| ------------ | ----------- |
| Dias con mas viajes en la semana | Viajes por dias de la semana |
| Reduccion de co2 Metrica | AVG emision autos combustion interna - AVG emision autos hibridos_electricos |
| Promedio de km recorridos por dia | Km Total / Cantidad de autos combustion interna. Lo mismo con electricos_hibridos para comparar |
| Autonomia combustion vs autonomia electricos | Km/Litro * Litros vs Km/Bateria * Bateria |
| Zona con mas cantidad de viajes | Viajes por distritos |

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
En nuestro proyecto, contamos con dos roles principales:

### Data Analysts
Los Data Analysts en nuestro equipo se dedican principalmente a tareas relacionadas con el análisis de datos. Dos de los miembros que desempeñan este rol son:

Fabrizio Mazzucco
Lorena Ravera

Estos profesionales son responsables de extraer, limpiar, analizar y presentar datos de una manera significativa para tomar decisiones informadas.

### Data Engineers
Los Data Engineers en nuestro equipo se centran principalmente en tareas relacionadas con la ingeniería de datos. Tres de los miembros que desempeñan este rol son:

Aymara Falcón
Alexis Alvarez
Victoria Galvez

Estos expertos se encargan de diseñar, implementar y mantener las infraestructuras de datos y pipelines que permiten la recopilación, procesamiento y almacenamiento eficiente de los datos.

Cada uno de estos roles es fundamental para el éxito de nuestro proyecto, y juntos trabajamos en colaboración para garantizar la calidad y la utilidad de los datos que manejamos. 

