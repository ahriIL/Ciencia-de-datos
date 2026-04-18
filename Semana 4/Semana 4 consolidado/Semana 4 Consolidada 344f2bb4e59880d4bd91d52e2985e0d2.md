# Semana 4 Consolidada

# Ejercicios Complementarios

## Ejercicios de Normalización y Estandarización

---

### Ejercicio 1: Normalización Min-Max

Dados los datos: [10, 20, 30, 40, 50]

1. Aplicar Min-Max normalization manualmente
2. Verificar que el resultado esté entre 0 y 1
    
    <aside>
    
    Xmin = 10
    
    Xmax = 50
    
    **FORMULA:**
    
    (X - Xmin) / (Xmax - Xmin)
    
    Denominador = (50 - 10) = 40
    
    10 Xnm = (10 - 10) / (40) = 0
    
    20 Xnm = (20 - 10) / (40) = 0.25
    
    30 Xnm = (30 - 10) / (40) = 0.5
    
    40 Xnm = (40 - 10) / (40) = 0.75
    
    50 Xnm = (50 - 10) / (40) = 1E
    
    ![image.png](Semana%204%20Consolidada/cb215d12-6b3f-4ff6-a24b-4a8aa9619bdc.png)
    
    </aside>
    
3. Implementar en Python
    
    ```python
    import numpy as np
    
    datos = np.array([10,20,30,40,50])
    
    def Xnormalize(datosX):
        xMin = datosX.min()
        xMax = datosX.max()
        return (datosX - xMin) / (xMax -xMin)
    
    normalized_data = Xnormalize(datos)
    print(normalized_data)
    ```
    
    ![Screenshot 2026-04-16 at 1.00.45 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-16_at_1.00.45_p.m..png)
    

### Ejercicio 2: Estandarización (Z-Score)

Donde μ = media y σ = desviación estándar

Dados los datos: [2, 4, 4, 4, 5, 5, 7, 9]

1. Calcular la media
2. Calcular la desviación estándar
3. Estandarizar cada valor
4. Verificar que la media sea ~0 y std sea ~1
    
    ```python
    import numpy as np
    
    datos = np.array([2,4,4,4,5,5,7,9])
    
    #desviación estandar
    desviacion = np.std(datos)
    
        #sacar media
    media = sum(datos) / len(datos)
    
    # estandarizar cada valor
    ZEstandar = (datos - media) / desviacion
    
    print(f'desviacion: {desviacion}')
    print(f'media: {media}')
    print(f'estandarización: {ZEstandar}')
    
    ```
    
    ![Screenshot 2026-04-16 at 1.26.54 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-16_at_1.26.54_p.m..png)
    

### Ejercicio 3: Comparación de Técnicas

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

datos = np.array([100, 200, 300, 400, 500]).reshape(-1, 1)

# Aplicar:
# 1. MinMaxScaler de sklearn
MMScaler = MinMaxScaler()
datosMMScaler = MMScaler.fit_transform(datos)

# 2. StandardScaler de sklearn
SSScaler = StandardScaler()
datosSSScaler = SSScaler.fit_transform(datos)

print("- - MinMaxScaler - -")
print(datosMMScaler)

print("\n- - StandarScaler - -")
print(datosSSScaler)
# Comparar resultados

'''
En el MinMaxScaler(Nomralización), 0 es e dato minimo que es 100,
mientras que en StandarScaler(Estadarización) el 0 es la media que sería el 300
'''

```

![Screenshot 2026-04-16 at 6.03.05 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-16_at_6.03.05_p.m..png)

---

## Ejercicios de Manejo de Valores Faltantes

---

### Ejercicio 4: Identificación de Valores Faltantes

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

# Ejercicios:
# 1. Identificar valores faltantes con isnull()
nulos = df.isnull()
# 2. Contar valores faltantes por columna
contarNulos = df.isnull().sum()
# 3. Calcular porcentaje de valores faltantes
porcenNulos = (df.isnull().sum() / len(df)) * 100
# 4. Mostrar solo filas con valores faltantes
filasnulos= df[df.isnull().any(axis=1)]

print("- - Conteo de Nulos - -")
print(conteo_nulos)

print("\n- - Porcentaje de Nulos - -")
print(porcentaje_nulos)

print("\n--- Filas con Nulos - -")
print(filas_con_nulos)
```

![Screenshot 2026-04-16 at 6.03.30 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-16_at_6.03.30_p.m..png)

### Ejercicio 5: Estrategias de imputación

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

# Ejercicios:
# 1. Identificar valores faltantes con isnull()
nulos = df.isnull()
# 2. Contar valores faltantes por columna
contarNulos = df.isnull().sum()
# 3. Calcular porcentaje de valores faltantes
porcenNulos = (df.isnull().sum() / len(df)) * 100
# 4. Mostrar solo filas con valores faltantes
filasnulos= df[df.isnull().any(axis=1)]

print("- - Conteo de Nulos - -")
print(contarNulos)

print("\n- - Porcentaje de Nulos - -")
print(porcenNulos)

print("\n--- Filas con Nulos - -")
print(filasnulos)
```

![Screenshot 2026-04-16 at 6.04.01 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-16_at_6.04.01_p.m..png)

![Screenshot 2026-04-16 at 6.04.13 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-16_at_6.04.13_p.m..png)

### Ejercicio 6: imputación avanzada

```python
# Usar sklearn.impute.SimpleImputer

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# mismo df
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

# Probar diferentes estrategias:
# - mean
usarMean = SimpleImputer(strategy='mean')
dfMean = pd.DataFrame(usarMean.fit_transform(df), columns=df.columns)
# - median
usarMedian = SimpleImputer(strategy='median')
dfMedian = pd.DataFrame(usarMedian.fit_transform(df), columns=df.columns)
# - most_frequent
usarMostFq = SimpleImputer(strategy='most_frequent')
dfMostFq = pd.DataFrame(usarMostFq.fit_transform(df), columns=df.columns)
# - constant
usarConstant = SimpleImputer(strategy='constant', fill_value=0)
dfConstant = pd.DataFrame(usarConstant.fit_transform(df), columns=df.columns)

print("- - Media - -")
print(dfMean)

print("\n- - Constante - -")
print(dfConstant)
```

![Screenshot 2026-04-16 at 6.15.41 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-16_at_6.15.41_p.m..png)

## Ejercicio de Detección y Manejo de Outliers

---

### Ejercicio 7: Método IQR (Rango **Intercuartil**)

```python
import numpy as np

datos = [10, 12, 14, 15, 16, 18, 20, 22, 25, 100]

# Calcular:
# 1. Q1 (percentil 25)
q1 = np.percentile(datos, 25)
# 2. Q3 (percentil 75)
q3 = np.percentile(datos, 75)
# 3. IQR = Q3 - Q1
iqr = q3 - q1
# 4. Límite inferior = Q1 - 1.5 * IQR
inferior = q1 - 1.5 * iqr

# 5. Límite superior
superior = q3 + 1.5 * iqr

# 6. Identificar outliers
outliers = [x for x in datos if x < inferior or x > superior]

print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Límites: {inferior} a {superior}")
print(f"Outliers detectados: {outliers}")

```

![Screenshot 2026-04-16 at 6.45.40 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-16_at_6.45.40_p.m..png)

### Ejercicio 8: Metodo Z-Sctor

```
from scipy import stats
import numpy as np

datos = np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100])

# Calcular Z-scores y encontrar valores donde |Z| > 3
z_scores = stats.zscore(datos)
outliers = np.where(np.abs(z_scores) > 3)

print(f"Z-scores de cada dato:\n{np.round(z_scores, 2)}")
print(f"\nValores donde |Z| > 3 (Outliers): {outliers}")

```

![Screenshot 2026-04-17 at 4.59.32 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-17_at_4.59.32_p.m..png)

### Ejercicio 9: Manejo de Outliers

```python
from scipy import stats
import numpy as np

datos = np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100])

q1, q3 = np.percentile(datos, 25), np.percentile(datos, 75)
iqr = q3 - q1
limiteSup = q3 + 1.5 * iqr
limiteInf = q1 - 1.5 * iqr

# Opciones para manejar outliers:
# 1. Eliminar outliers
eliminar = datos[(datos >= limiteInf) & (datos <= limiteSup)]
# 2.替换为边界值 (capping)
capping = np.clip(datos, limiteInf, limiteSup)
# 3. Transformación logarítmica
datosLog = np.log(datos)
# 4. Transformación Box-Cox
datosBoxcox, lmbda = stats.boxcox(datos)
# Aplicar cada método

print(f"Original: {datos}")
print(f"1. Eliminados: {eliminar}")
print(f"2. Capping: {np.round(capping, 2)}")
print(f"3. Logarítmica: {np.round(datosLog, 2)}")
print(f"4. Box-Cox: {np.round(datosBoxcox, 2)}")
```

![Screenshot 2026-04-17 at 4.59.51 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-17_at_4.59.51_p.m..png)

---

## Ejercicios de Transformación de Variables

---

### Ejercicio 10: Codificación de Variables Categóricas

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({
    'color': ['rojo', 'azul', 'verde', 'rojo', 'verde'],
    'talla': ['S', 'M', 'L', 'S', 'M']
})

# Aplicar:
# 1. Label Encoding
encoderColor = LabelEncoder()
encoderTalla = LabelEncoder()

df['color_cod'] = encoderColor.fit_transform(df['color'])
df['talla_cod'] = encoderTalla.fit_transform(df['talla'])

print("- - LabelEncoding - -")
print(df)

mappingColor = dict(zip(encoderColor.classes_, encoderColor.transform(encoderColor.classes_)))
mappingTalla = dict(zip(encoderTalla.classes_, encoderTalla.transform(encoderTalla.classes_)))

print(f'Mapeo de color: {mappingColor}')
print(f'Mapeo de talla: {mappingTalla}')

# 2. One-Hot Encoding con get_dummies
dummies = pd.get_dummies(df['color'], prefix='color')

print("\n- - One-Hot con get_dummies - -")
print(dummies)

# 3. One-Hot Encoding con sklearn
encoder = OneHotEncoder(sparse_output=False)
resultado = encoder.fit_transform(df[['color']])

columnas = encoder.get_feature_names_out(['color'])
dfSklearn = pd.DataFrame(resultado, columns = columnas)

print('\n - - One Hot - -')
print(dfSklearn)

```

![Screenshot 2026-04-17 at 5.00.20 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-17_at_5.00.20_p.m..png)

### Ejercicio 11: Transformaciones Numéricas

```python
import numpy as np

datos = [1, 2, 3, 4, 5, 10, 20, 30]

# Aplicar:
# 1. Logaritmo natural
datosLog = np.log(datos)
# 2. Raíz cuadrada
datosSqrt = np.sqrt(datos)
# 3. Transformación Box-Cox
datosBoxCox , lmbda = stats.boxcox(datos)
# 4. Discretización (binned)
datosBinned = pd.cut(datos, bins=3, labels=["Bajo", "Medio", "Alto"])
resultados = pd.DataFrame({
    'Original': datos,
    'Log': np.round(datosLog, 2),
    'Sqrt': np.round(datosSqrt, 2),
    'Box-Cox': np.round(datosBoxCox, 2),
    'Binned': datosBinned
})

print(resultados)
```

![Screenshot 2026-04-17 at 5.00.36 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-17_at_5.00.36_p.m..png)

### Ejercicio 12: **Feature Engineering**

```
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Creamos un DataFrame de ejemplo
df = pd.DataFrame({
    'ventas': [100, 150, 200, 50, 300],
    'clientes': [10, 15, 25, 5, 30],
    'costo': [80, 120, 150, 60, 200],
    'fecha': pd.to_datetime(['2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04', '2026-01-05'])
})

# 1. Ratio entre dos columnas
df['ticket_promedio'] = df['ventas'] / df['clientes']
# 2. Diferencia entre columnas
df['ganancia'] = df['ventas'] - df['costo']
# 3. Agregar indicadores binarios
df['es_venta_alta'] = (df['ventas'] > 150).astype(int)
# 4. Polynomial Features
poly = PolynomialFeatures(degree=2, include_bias=False)
poly_data = poly.fit_transform(df[['ventas', 'costo']])
df_poly = pd.DataFrame(poly_data, columns=poly.get_feature_names_out(['ventas', 'costo']))
# 5. DateTime features
df['dia_semana'] = df['fecha'].dt.day_name()
df['es_fin_de_semana'] = df['fecha'].dt.dayofweek.isin([5, 6]).astype(int)
df['mes'] = df['fecha'].dt.month

print("- - DataFrame - -")
print(df)
print("\n- - Polynomial Features - -")
print(df_poly.head())
```

![Screenshot 2026-04-17 at 5.02.25 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-17_at_5.02.25_p.m..png)

---

## Ejercicio de Escalamiento de Datos

---

### Ejercicio 13: Comparar Escaladores

```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
import numpy as np
import pandas as pd

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Aplicar cada escalador y comparar resultados
# ¿Cuándo usar cada uno?
minMax = MinMaxScaler().fit_transform(data)
standard = StandardScaler().fit_transform(data)
robust = RobustScaler().fit_transform(data)
maxAbs = MaxAbsScaler().fit_transform(data)

print("--- Datos Originales ---")
print(data)
print("\n--- MinMaxScaler (0 a 1) ---")
print(np.round(minMax, 2))
print("\n--- StandardScaler (Media 0) ---")
print(np.round(standard, 2))
print("\n--- RobustScaler (Resistente a Outliers) ---")
print(np.round(robust, 2))
print("\n--- MaxAbsScaler (-1 a 1) ---")
print(np.round(maxAbs, 2))
```

| **Escalador** | **¿Cuándo usar cada uno?** |
| --- | --- |
| **MinMaxScaler (**Comprime todo entre 0 y 1**)** | Cuando sabes que tus datos no tienen limites fijos |
| **StandardScaler (**Centra los datos en 0**)** | Es un estándar se usa cuando los datos siguen una distribución normal |
| **RobustScaler (**Usa la mediana y el rango intercuartil**)** | No usan media, y los valores externos no mueven el escalado de los normales |
| **MaxAbsScaler (**Divide entre el valor más grande**)** | Se usa mas en matrices dispersas o cuando los datos están centrados en 0 pero tienen diferentes escalas |

![Screenshot 2026-04-17 at 5.03.17 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-17_at_5.03.17_p.m..png)

### Ejercicio 14: Pipeline de procesamiento

```python
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

df = pd.DataFrame({
    'edad': [25, 30, np.nan, 45, 22],
    'salario': [50000, 60000, 120000, np.nan, 30000],
    'ciudad': ['Queretaro', 'CDMX', 'Queretaro', 'Monterrey', 'CDMX'],
    'prioridad': ['Alta', 'Baja', 'Media', 'Alta', 'Baja']
})

# 1. Seleccionar columnas numéricas y categóricas
colNum = ['edad', 'salario']
cols_categoricas = ['ciudad', 'prioridad']

# 2. Aplicar transformaciones apropiadas
numTransf = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

catTransform = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

#3. Combinar en un pipline
preprocesador = ColumnTransformer(
    transformers=[
        ('num', numTransf, colNum),
        ('cat', catTransform, cols_categoricas)
    ])
pipelineF = Pipeline(steps=[('prepro', preprocesador)])
datoslisto = pipelineF.fit_transform(df)

print("--- Matriz resultante lista para el modelo ---")
print(datoslisto)
```

![Screenshot 2026-04-17 at 5.03.39 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-17_at_5.03.39_p.m..png)

---

## Ejercicio de Investigación

---

### Ejercicio 15: Mejores Prácticas

Investigar:

1. ¿Por qué es importante la preparación de datos?
    
    Porque mejora la calidad de los datos, elimina errores y permite que el modelo aprenda correctamente, dando resultados más precisos
    
2. ¿Qué es data leakage y cómo evitarlo?
    
    Cuando el modelo usa información que no debería, lo que da resultados irreales. Se evita reparando bien los datos y aplicando transformaciones solo al conjunto de entretenimiento
    
3. ¿Cuál es la diferencia entre datos de entrenamiento y prueba?
    
    Los datos de entrenamiento se usan para enseñar al modelo, y los de prueba para evaluar qué tan bien funciona sin haberlos visto antes
    

### Ejercicio 16: Técnicas Avanzadas

Investigar:

1. ¿Qué es SMOTE para datos desbalanceados?
    
    SMOTE (Synthetic Minority Over-sampling Technique) es una técnica que genera nuevos datos sintéticos de la clase minoritaria para equilibrar el dataset y mejorar el rendimiento del modelo.
    
2. ¿Qué es la imputación por K-Nearest Neighbors?
    
    Es un método para rellenar datos faltantes usando los valores de los datos más cercanos (vecinos) según su similitud.
    
3. ¿Qué es Target Encoding?
    
    Es una técnica que convierte variables categóricas en números usando el promedio de la variable objetivo para cada categoría.
    

---

# Actividad 3

## **Objetivo**

---

Reforzar los conceptos de regresión lineal simple y limpieza de datos, utilizando datos reales de equipos de béisbol, para predecir el número de carreras (runs) basado en el número de bateos.

## **Instrucciones**

En esta actividad, crearás y evaluarás un modelo de regresión lineal simple con el objetivo de predecir el número de runs de los equipos de béisbol de acuerdo con el número de bateos que tienen.

---

### **Parte 1: Preparación de los datos**

1. **Obtención de los datos:** Guarda la base de datos en una variable. Los datos los encontrarás en la siguiente página: [https://www.espn.com.mx/beisbol/mlb/estadisticas/jugador](https://www.espn.com.mx/beisbol/mlb/estadisticas/jugador)
2. **Limpieza y preparación de los datos:** Evalúa los datos recopilados en busca de valores faltantes o erróneos. Además, realiza la limpieza necesaria, la imputación de datos faltantes y la estandarización de los datos para asegurar su calidad y uniformidad.

```python
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

url = "https://www.espn.com.mx/beisbol/mlb/estadisticas/jugador"
tablas = pd.read_html(url)

df = pd.concat([tablas[0], tablas[1]], axis=1)

print("Datos originales:")
print(df.head())

df.columns = df.columns.str.upper()
df = df.loc[:, ~df.columns.duplicated()]

df[["NOMBRE", "EQUIPO"]] = df["NOMBRE"].str.extract(r'(.+?)([A-Z]{2,3})$')

for col in df.columns:
    if col not in ["NOMBRE", "EQUIPO"]:
        df[col] = df[col].astype(str)
        df[col] = df[col].str.replace(",", "")
        df[col] = df[col].str.replace("%", "")
        df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["H", "R"])

print("\nDatos limpios:")
print(df.head())

```

![Screenshot 2026-04-17 at 5.48.08 p.m..png](Semana%204%20Consolidada/ef403d1b-6ced-463c-aae4-5767a6bcd3f6.png)

### **Parte 2: Modelado y evaluación**

Continúa con el desarrollo del modelo de regresión lineal simple. Para esto, realiza lo siguiente:

1. **Análisis exploratorio:** Calcula la correlación de Pearson para determinar la relación entre el número de bateos y carreras. Interpreta este coeficiente para entender la fuerza y dirección de la relación.
    
    ```python
    correlacion = df[["H", "R"]].corr().iloc[0,1]
    print("\nCorrelación:", correlacion)
    
    print("\nCorrelación de Pearson:", correlacion)
    
    if abs(correlacion) > 0.7:
        print("Relación fuerte")
    elif abs(correlacion) > 0.4:
        print("Relación moderada")
    else:
        print("Relación débil")
    
    if correlacion > 0:
        print("Relación positiva")
    else:
        print("Relación negativa")
    ```
    
    ![Screenshot 2026-04-17 at 5.52.08 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-17_at_5.52.08_p.m..png)
    
    Esta correlación mide que tan relacionadas están las dos variables H y R 
    
    **‘H’** es el numero de bateas y **‘R’** es el número de carreras
    
    Es una relación positiva  entre más bateos, más carreras. Pero no es una relación muy fuerte
    
2. **Construcción del modelo:** Identifica tu variable dependiente y tu variable independiente. Divide el conjunto de datos en dos grupos: uno para entrenamiento y otro para prueba.
    
    ```python
    #2. construccion de modelo
    X = df[["H"]]
    y = df["R"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("modelo", LinearRegression())
    ])
    ```
    
3. **Entrenamiento y predicción:** Entrena tu modelo de regresión lineal simple con el conjunto de entrenamiento. Luego, utiliza este modelo para realizar predicciones sobre el conjunto de prueba.
    
    ```python
    pipeline.fit(X_train, y_train)
    print("\nModelo entrenado")
    
    pred = pipeline.predict(X_test)
    
    print("Predicciones realizadas:")
    print(pred)
    
    ```
    
    ![Screenshot 2026-04-17 at 6.22.49 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-17_at_6.22.49_p.m..png)
    
    Se puede ver que en modelo tiene una capacidad limitadas para ver diferencias más especificas entre jugadores
    

1. **Evaluación:** Calcula el error de tus predicciones utilizando métricas adecuadas. Analiza estos errores para evaluar la precisión de tu modelo.
    
    ```python
    # 4. evaluacion
    mae = mean_absolute_error(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    
    print("\nMAE:", mae)
    print("RMSE:", rmse)
    
    # resultados
    resultado = X_test.copy()
    resultado["R_real"] = y_test.values
    resultado["R_pred"] = pred
    resultado["Error"] = abs(resultado["R_real"] - resultado["R_pred"])
    
    print("\nResultados:")
    print(resultado)
    
    #top judaroes
    top_jugadores = df.sort_values(by="R", ascending=False)
    
    print("\nTop 10 jugadores:")
    print(top_jugadores[["NOMBRE", "EQUIPO", "H", "R"]].head(10))
    
    ```
    
    ![Screenshot 2026-04-17 at 6.26.14 p.m..png](Semana%204%20Consolidada/Screenshot_2026-04-17_at_6.26.14_p.m..png)
    
    MAE es el error promedio por predicciones y RMSE penaliza los errores grandes, permite la precisión del modelo de una manera más estrictas
    
2. **Conclusión:** Reflexiona sobre los resultados obtenidos, discute la efectividad del modelo y su aplicabilidad en la toma de decisiones estratégicas basadas en el análisis de datos.

> 
> 
> 
> Existe una relación positiva entre los bateos y las carreras, lo que significa que mientras más bateos tiene un jugador, más probable es que genere carreras. El modelo funciona para estimar este comportamiento, aunque no es completamente preciso.
> Con base en los datos, el equipo ideal estaría formado por los jugadores con mayor número de carreras y bateos, ya que son los que más aportan ofensivamente. Sin embargo, hay que considerar que no es un modelo perfecto y que hay otros factores que también influyen en el rendimiento.
>