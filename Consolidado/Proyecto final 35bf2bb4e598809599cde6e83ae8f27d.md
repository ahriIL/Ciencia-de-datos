# Proyecto final

# Avance del Proyecto final

Código del avance del proyecto final:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = kagglehub.dataset_download("stevezhenghp/airbnb-price-prediction")

print(os.listdir(path))

df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "stevezhenghp/airbnb-price-prediction",
    "train.csv"   
)

sns.set_theme(style='darkgrid')
print(df.head(50))

#Analisis exploratorio
# 1. Información general del dataset (tipos de datos y nulos)
print("--- Información del Dataset ---")
print(df.info())

# 2. Estadísticas descriptivas de variables numéricas
print("\n--- Estadísticas Univariadas ---")
display(df.describe())

#Parte 2: Ánalisis Exploratorio de Datos
import math
from collections import Counter

def analizar_columna(columna):

    datos = [x for x in columna if x == x]
    n = len(datos)

    if n < 2:
        return 0, 0, 0, 0, 0, 0

    #MDTC
    #media
    media = sum(datos) / n

    #mediana
    datos_ordenados = sorted(datos)

    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]

    #moda
    conteo = Counter(datos)
    max_freq = max(conteo.values())
    moda = [k for k, v in conteo.items() if v == max_freq][0]

    # MDispecion

    #rango
    rango = max(datos) - min(datos)

    # varianza
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    varianza = suma_cuadrados / (n - 1)
    #desviación Estándar
    desviacion = math.sqrt(varianza)

    return media, mediana, moda, rango, varianza, desviacion

#precio dolares
df['precio_dolares'] = np.exp(df['log_price'])

columnas = ['log_price', 'precio_dolares',  'accommodates', 'bathrooms', 'bedrooms', 'number_of_reviews', 'review_scores_rating']

print(f"{'Variable':<20} | {'Media':<7} | {'Mediana':<7} | {'Moda':<7} | {'Rango':<7} | {'Varianza':<9} | {'Desv.Est':<7}")
print("-" * 95)

for col in columnas:
    if col in df.columns:
        res = analizar_columna(df[col])
        med, mdn, mod, ran, var, desv = res
        print(f"{col:<20} | {med:<7.2f} | {mdn:<7.1f} | {mod:<7.1f} | {ran:<7.1f} | {var:<9.2f} | {desv:<7.2f}")

#moda de variables
print("\n")

cols = ['city', 'property_type', 'room_type', 'bed_type', 'cancellation_policy', 'cleaning_fee']

print(f"{'Variable':<25} | {'Moda':<25}")
print("-" * 60)
for col in cols:
    if col in df.columns:
        moda_val = df[col].mode()[0]
        print(f"{col:<25} | {moda_val}")

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 5))

#histograma precio
plt.subplot(1, 2, 1)
sns.histplot(df['log_price'], kde=True, color="skyblue")
plt.title('Distribución de log_price')
plt.xlabel('Log Price')

# bocplot precio x habitación
plt.subplot(1, 2, 2)
sns.boxplot(x='room_type', y='log_price', data=df, palette="Set3")
plt.title('Precio por Tipo de Habitación')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

sns.scatterplot(x='accommodates', y='log_price', data=df, alpha=0.3, color="coral")

sns.regplot(x='accommodates', y='log_price', data=df, scatter=False, color="darkred")

plt.title('Relación entre Capacidad y Precio')
plt.show()

plt.figure(figsize=(10, 8))

cols_num = ['log_price', 'accommodates', 'bathrooms', 'bedrooms', 'number_of_reviews', 'review_scores_rating']
corr = df[cols_num].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Mapa de Calor de Correlaciones')
plt.show()

plt.figure(figsize=(12, 6))
# Ordenamos las ciudades por precio promedio
order = df.groupby('city')['log_price'].mean().sort_values(ascending=False).index

sns.barplot(x='city', y='log_price', data=df, order=order, palette="viridis")
plt.title('Precio Promedio (Log) por Ciudad')
plt.show()
```

![Screenshot 2026-05-08 at 6.16.41 p.m..png](Proyecto%20final/Screenshot_2026-05-08_at_6.16.41_p.m..png)

![Screenshot 2026-05-08 at 6.16.51 p.m..png](Proyecto%20final/Screenshot_2026-05-08_at_6.16.51_p.m..png)

![Screenshot 2026-05-08 at 6.17.12 p.m..png](Proyecto%20final/Screenshot_2026-05-08_at_6.17.12_p.m..png)

# Proyecto final

---

```python
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm

```

## Parte 1: Modelo de regresión lineal múltiple

### 1. Limpieza de datos

```python
df['precio_dolares'] = np.exp(df['log_price'])

print("Valores faltantes por columna:")
print(df.isnull().sum()[df.isnull().sum() > 0])

cols_modelo = ['log_price', 'accommodates', 'bathrooms', 'bedrooms', 'number_of_reviews', 'review_scores_rating']

for col in cols_modelo:
    if df[col].isnull().sum() > 0:
        mediana = df[col].median()
        df[col].fillna(mediana, inplace=True)
        print(f"  '{col}': imputado con mediana = {mediana:.2f}")

media_lp = df['log_price'].mean()
std_lp = df['log_price'].std()
antes = len(df)
df = df[(df['log_price'] >= media_lp - 3*std_lp) & (df['log_price'] <= media_lp + 3*std_lp)]
print(f"\nFilas eliminadas por outliers en log_price: {antes - len(df)}")
print(f"Filas restantes: {len(df)}")

```

![Screenshot 2026-05-08 at 6.19.02 p.m..png](Proyecto%20final/Screenshot_2026-05-08_at_6.19.02_p.m..png)

### 2. Selección de características

```markdown
['accommodates', 'bathrooms', 'bedrooms',
 'number_of_reviews', 'review_scores_rating']

 Se seleccionaron variables relacionadas con capacidad, calidad y popularidad del alojamiento debido a su posible influencia en el precio.
```

### 3. Identificación de variables

```markdown
- **Variable dependiente (Y):** log_price — el precio del alojamiento en escala logarítmica.
- **Variables independientes (X):** accommodates, bathrooms, bedrooms, number_of_reviews, review_scores_rating.
```

### 4. Análisis de correlación

```python
cols_num = ['log_price', 'accommodates', 'bathrooms', 'bedrooms', 'number_of_reviews', 'review_scores_rating']

sns.pairplot(df[cols_num].dropna(), diag_kind='kde', plot_kws={'alpha': 0.3})
plt.suptitle('Pairplot de Variables del Modelo', y=1.02)
plt.show()
```

![image.png](Proyecto%20final/image.png)

Las variables físicas de la propiedad (capacidad, habitaciones, baños) son las que más influyen en el precio, meintras que las métricas de reseñas aportan poco al modelo

### 5. Grupos de entrenamiento y prueba

```python
X = df[['accommodates', 'bathrooms', 'bedrooms', 'number_of_reviews', 'review_scores_rating']].dropna()
y = df.loc[X.index, 'log_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Entrenamiento: {X_train.shape[0]} filas")
print(f"Prueba: {X_test.shape[0]} filas")
```

![Screenshot 2026-05-08 at 6.21.14 p.m..png](Proyecto%20final/Screenshot_2026-05-08_at_6.21.14_p.m..png)

### 6. Construcción y entrenamiento del modelo

```python
modelo = LinearRegression()
modelo.fit(X_train, y_train)

print("Modelo entrenado.")
print("\nCoeficientes:")
for nombre, coef in zip(X.columns, modelo.coef_):
    print(f"  {nombre}: {coef:.4f}")
print(f"  Intercepto: {modelo.intercept_:.4f}")
```

![Screenshot 2026-05-08 at 6.21.43 p.m..png](Proyecto%20final/Screenshot_2026-05-08_at_6.21.43_p.m..png)

### 7. Evaluación del modelo

```python
y_pred_train = modelo.predict(X_train)
y_pred_test = modelo.predict(X_test)

r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)

n = X_test.shape[0]
k = X_test.shape[1]
r2_ajustado = 1 - (1 - r2_test) * (n - 1) / (n - k - 1)

print(f"R² (entrenamiento): {r2_train:.4f}")
print(f"R² (prueba):        {r2_test:.4f}")
print(f"R² ajustado:        {r2_ajustado:.4f}")

#VIF 

print("- - VIF - -")
X_vif = sm.add_constant(X)

vif_data = pd.DataFrame()
vif_data["Variable"] = X_vif.columns
vif_data["VIF"] = [
    variance_inflation_factor(X_vif.values, i)
    for i in range(X_vif.shape[1])
]

print(vif_data)
```

![Screenshot 2026-05-10 at 8.15.22 a.m..png](Proyecto%20final/Screenshot_2026-05-10_at_8.15.22_a.m..png)

### 8. Predicciones

### 9. Cálclo de error cuadrático de medio

```python
mse = mean_squared_error(y_test, y_pred_test)
rmse = np.sqrt(mse)

print(f"MSE:  {mse:.4f}")
print(f"RMSE: {rmse:.4f}")

comparacion = pd.DataFrame({
    'Real': y_test.values[:10],
    'Predicción': y_pred_test[:10],
    'Error': y_test.values[:10] - y_pred_test[:10]
})
print("\nPrimeras 10 predicciones vs valores reales:")
print(comparacion.to_string(index=False))
```

![Screenshot 2026-05-10 at 8.15.57 a.m..png](Proyecto%20final/Screenshot_2026-05-10_at_8.15.57_a.m..png)

---

## Parte 2. Comunicación de resultados

1. Gráfico Predicciones vs Valores Reales
    
    ```python
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred_test, alpha=0.3, color='steelblue', edgecolors='none')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=2, label='Predicción perfecta')
    plt.xlabel('Valores Reales (log_price)')
    plt.ylabel('Predicciones (log_price)')
    plt.title('Predicciones vs Valores Reales')
    plt.legend()
    plt.tight_layout()
    plt.show()
    ```
    
    ![image.png](Proyecto%20final/image%201.png)
    
    El modelo predice bien los precios intermedios, pero osbreestima los alojamientos baratos y subestima los más caros. Esto idnica que el modelo es funcional pero limitado en los extremos de precio
    
2. Gráfico Importancias de caracteristicas del modelo
    
    ```python
    coeficientes = pd.DataFrame({
        'Variable': X.columns,
        'Coeficiente': modelo.coef_
    }).sort_values('Coeficiente', ascending=True)
    
    colores = ['tomato' if c < 0 else 'steelblue' for c in coeficientes['Coeficiente']]
    
    plt.figure(figsize=(8, 5))
    plt.barh(coeficientes['Variable'], coeficientes['Coeficiente'], color=colores)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.xlabel('Coeficiente')
    plt.title('Importancia de Características del Modelo')
    plt.tight_layout()
    plt.show()
    ```
    
    ![image.png](Proyecto%20final/image%202.png)
    
    La capacidad de húespedes (accomodates) y el número de habitaciones son los factores que se determinan el precio. Las reseñas y calificaciones no tienen impacto relevante, por lo que podrían eliminarse del modelo sin afectar los resultados
    

---

# Conclusión

En este proyecto se trabajó con datos de Airbnb para analizar qué características influyen más en el precio de los alojamientos. Primero se limpiaron los datos para evitar errores en el análisis y después se seleccionaron las variables más relevantes para crear el modelo.

Con el análisis realizado se pudo observar que variables como la cantidad de personas que puede alojar una propiedad, el número de habitaciones y las calificaciones de los usuarios sí tienen relación con el precio. También se revisó la multicolinealidad entre variables para comprobar que el modelo funcionara correctamente.

El modelo de regresión lineal múltiple logró obtener resultados aceptables, ya que las predicciones fueron relativamente cercanas a los valores reales. Además, las gráficas ayudaron a visualizar mejor el comportamiento de los datos y el desempeño del modelo.

En general, este proyecto ayudó a entender mejor cómo aplicar técnicas de ciencia de datos y modelos predictivos en Python para analizar información real y obtener conclusiones a partir de ella.