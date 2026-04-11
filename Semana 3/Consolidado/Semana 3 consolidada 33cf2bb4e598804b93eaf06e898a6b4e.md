# Semana 3 consolidada

# **Ejercicios Complementarios - Semana 3**

## **Ejercicios de Python Básico**

---

### **Ejercicio 1: Variables y Tipos de Datos**

```python
# Ejercicios:
# 1. Crear variables de diferentes tipos: int, float, str, bool, list, dict
# 2. Convertir tipos: str a int, float a int, int a float
# 3. Usar f-strings para formatear: "El usuario tiene X años"

# 1. Crear variables
# int
numero = 2

# float
numero2 = 2.3

# str
nombre = "Arantza"

# bool
valido = True

#list
lista = {"perro",  "gato", "jirafa"}

#dict
mi_diccionario = {           
    "id": 1, 
    "curso": "Programación"
}
```

### Ejercicio 2: Control de flujo

```python
# Ejercicios:
# 1. Crear un programa que determine si un número es positivo, negativo o cero
# 2. Crear un menú con if-elif-else
# 3. Usar un loop for para iterar sobre una lista
# 4. Usar while para calcular factorial

#1. Programa que determina si el número es positivo, negativo o cero

numero = -2

if numero < 0:
    print ("El número es negativo")
elif numero == 0:
    print ("El número es cero")
else:
    print ("El número es positivo")

#2. Menú

inventario = {"pescado", "harina", "catsup"}
empleados = {"Juan", "Sofia", "Pedro"}
distribuidores = {"Mariscos Felices", "Tienda de todo"}

print("¿Qué desea realizar?") 
print("1. Ver inventario\n2.Ver Empleados\n3.Ver distribuidores")

usuario = input("Ingrese el número")
usuario_int = int(usuario)

if usuario_int == 1:
    print (inventario)
elif usuario_int == 2:
    print (empleados)
elif usuario_int == 3:
    print (distribuidores)
else:
    print("El número que ingreso es incorrecto")

#3. Usar loop

frutas = ["Manzana", "Plátano", "Cereza"]

for fruta in frutas:
    print(f"Lista de frutas: {fruta}")

#4. Calcula un factorial

resultado = 1
factorial = 4

for i in range(1, factorial + 1):

    resultado = resultado * i

print(resultado)   

```

### Ejercicio 3: Funciones

```python
# Crear funciones para:
# 1. Calcular el área de un círculo
# 2. Convertir Celsius a Fahrenheit
# 3. Calcular el promedio de una lista
# 4. Encontrar el valor máximo y mínimo

# 1. Área de un circulo
radio = 5
area = 3.14159265 * (radio**2)
print(area)

# 2. Celsuis a Fahrenheit
celsuis = 0
fahrenheit = (celsuis * 1.8) + 32
print(fahrenheit)

# 3 Calcular promedio de lista
numeros = [10, 20, 30, 40]
total = sum(numeros)
cantDeNumeros = len(numeros)
promedio = total/cantDeNumeros

print(f"El promedio es: {promedio}")

#4. Valor máximo y minimo
maxmin = [15, 25, 5, 40, 12]

valmax = max(maxmin)
valmin = min(maxmin)

print(f"Máximo: {valmax}")
print(f"Minimo: {valmin}")

```

---

## Ejercicios de NumPy

---

### Ejercicio 4: Operaciones con Arrays

```python
import numpy as np

# Crear arrays y realizar operaciones:
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# Ejercicios:
# 1. Sumar los arrays elemento a elemento
sumar = arr1 + arr2
print(f"Suma de elemento a elemento de los arrays: {sumar}")

# 2. Multiplicar por un escalar
multiplicar1 = arr1 * 2
print(f"Array 1 * 2 = {multiplicar1}")

multiplicar2 = arr2 * 3
print(f"Array 1 * 3 = {multiplicar2}")

# 3. Calcular la media, mediana y desviación estándar
print(f"Media Array1: {np.mean(arr1)}")
print(f"Mediana: {np.median(arr1)}")
print(f"Desviación estándar: {np.std(arr1):.2f}")

# 4. Encontrar valores únicos
arr3 = np.array([1, 1, 3, 4, 5])
unicos = np.unique(arr2)
print(f"Valores únicos en {arr2} y : {unicos}")

# 5. Reshape de un array 1D a 2D
array_1d = np.array([10, 20, 30, 40, 50, 60])
array_2d = array_1d.reshape(2, 3)
print(array_2d)

```

### Ejercicio 5: Álgebra con NumPy

```python
import numpy as np

# Dados los vectores v1 = [1, 2, 3] y v2 = [4, 5, 6]
v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

# Calcular:
# 1. Producto punto
punto = np.dot(v1, v2)
print(f"Punto {v1} y {v2}: {punto}")

# 2. Producto cruz
cruz = np.cross(v1, v2)
print(f"Cruz{v1} y {v2}: {cruz}")

# 3. Magnitud de cada vector
v1magn = np.linalg.norm(v1)
v2magn = np.linalg.norm(v2)
print(f"v1 = {v1magn:.2f}")
print(f"v2 = {v2magn:.2f}")

# 4. Normalización de vectores
v1Nor = v1 / np.linalg.norm(v1)
v2Nor = v2 / np.linalg.norm(v2)
print(f"v1 normalizado: {v1Nor}")
print(f"v2 normalizado: {v2Nor}")

```

---

## **Ejercicios de Visualización**

---

### **Ejercicio 8: Matplotlib**

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(12, 8))

# Crear visualizaciones:
# 1. Gráfico de línea básico
plt.subplot(2, 2, 1)
plt.plot(x,y, color="#FF5E99", linewidth=4)
plt.title('Gráfica Linea', color='#701705',fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('sin(x), fontsize=12')
plt.grid(True)
plt.show

# 2. Gráfico de dispersión
plt.subplot(2, 2, 2)
xdisp = np.random.randn(50)
ydisp = np.random.randn(50)
plt.scatter(xdisp, ydisp, alpha=0.6, color='#FFC45E')
plt.title('Gráfico de Dispersión', color='#003E47')
plt.xlabel('X')
plt.ylabel('Y')

# 3. Histograma
plt.subplot(2, 2, 3)
datos_hist = np.random.randn(1000)
plt.hist(datos_hist, bins=30, color='#FFDEEA', edgecolor='#FF5E99')
plt.title('Histograma', color='#754A00')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# 4. Gráfico de barras
plt.subplot(2, 2, 4)
categorias = ['Ing', 'Lic', 'Doc', 'Arq']
valores = [45, 30, 15, 10]
plt.bar(categorias, valores, color=['#5E99FF', '#FF5E99', '#5EEAFF', '#5EFFC4'])
plt.title('Gráfico de Barras', color='#00472D')
plt.xlabel('Carrera')
plt.ylabel('Cantidad')

# 5. Personalizar: títulos, etiquetas, leyenda, colores

plt.tight_layout()
plt.show()
```

![image.png](Semana%203%20consolidada/image.png)

### Ejercicio 9: Análisis Exploratorio

```python
# Usando un dataset (puede ser 'iris' o cualquier otro)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
df = sns.load_dataset('iris')

# Ejercicios:
# 1. Cargar dataset y mostrar info básica

print("     - - PRIMERAS 10 FILAS IRIS - -\n".center(30))
df.head(10)

print("Información del dataset:")
df.info()

# 2. Calcular estadísticas descriptivas
print("Estadísticas descriptivas:")
df.describe()

# 3. Crear histogramas de todas las columnas numéricas

df.select_dtypes(include=['number']).hist(bins=20, figsize=(12, 8), color='#CFFFEE', edgecolor='black')

plt.suptitle('Distribución de Variables Numéricas - Iris', fontsize=16, color="#8AB5FF")

plt.tight_layout() 
plt.show()

# 4. Crear matriz de correlación
plt.figure(figsize=(8, 6))
numericas = df.select_dtypes(include=['float64'])
sns.heatmap(numericas.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación')
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='species', y='petal_length', palette='Reds')
plt.title('Comparación de Largo de Pétalo por Especie', fontsize=14, color="#5B012F")
plt.xlabel('Especie de Flor')
plt.ylabel('Largo del Pétalo (cm)')

plt.show()

# 6. Identificar outliers
Q1 = df['sepal_width'].quantile(0.25)
Q3 = df['sepal_width'].quantile(0.75)

IQR = Q3 - Q1
limiteinf = Q1 - 1.5 * IQR
limitesup = Q3 + 1.5 * IQR
outliers = df[(df['sepal_width'] < limiteinf) | (df['sepal_width'] > limitesup)]

print(f"--- DETECCIÓN DE OUTLIERS EN ANCHO DEL SÉPALO ---")
print(f"Límite inferior: {limiteinf:.2f}")
print(f"Límite superior: {limitesup:.2f}")
print(f"\nSe encontraron {len(outliers)} flores que son outliers:")

```

![Screenshot 2026-04-09 at 11.52.28 a.m..png](Semana%203%20consolidada/Screenshot_2026-04-09_at_11.52.28_a.m..png)

![image.png](Semana%203%20consolidada/image%201.png)

![image.png](Semana%203%20consolidada/image%202.png)

![image.png](Semana%203%20consolidada/image%203.png)

![Screenshot 2026-04-09 at 11.56.29 a.m..png](Semana%203%20consolidada/Screenshot_2026-04-09_at_11.56.29_a.m..png)

## **Ejercicios de Estadística**

---

### **Ejercicio 10: Medidas de Tendencia Central**

| **Datos** |  |  | rr |
| --- | --- | --- | --- |
| [5, 3, 8, 3, 7] | 5.2 | 5 | 3 |
| [10, 20, 30, 40] | 25 | 25 | - |
| [1, 2, 2, 3, 3, 3, 4] | 2.57 | 3 | 3 |

### Ejercicio 11: Dispersión

| **Datos** | **Rango** | **Varianza** | **Desviación Estándar** |
| --- | --- | --- | --- |
| [2, 4, 4, 5, 5, 7, 9] | 7 | 4.0 | 2.0 |
| [1, 3, 3, 5, 9] | 8 | 8.0 | 2.83 |

## **Ejercicios de Investigación**

---

### **Ejercicio 12: El Proceso de Data Science**

1. ¿Qué es el ciclo CRISP-DM?
    
    El CRISP-DM es una metodología que organiza el proceso de un análisis de datos en pasos claros para resolver un problema de forma estructurada
    
2. ¿Cuáles son las fases del proceso de ciencia de datos?
    
    Comprensión del negocio, comprensión de los datos, preparación de los datos, modelado, evaluación y despliegue
    
3. ¿Qué es el MVP (Minimum Viable Product) en ciencia de datos?
    
    Es una versión básica del proyecto que ya funciona con el que ya funciona con lo mínimo necesario, y sirve para validar si la solución es útil antes de mejorarla
    

---

### **Ejercicio 13: Caso de Estudio**

Investigar un caso real de análisis exploratorio de datos:

- ¿Qué preguntas buscaban responder?
    
    en el caso de Iris dataset, buscaban identificar si se podían diferencias las especies de flores según sus características
    
- ¿Qué técnicas usaron?
    
    Análisis Exploratorio (EDA), visualización de datos y estadísticas descriptivas
    
- ¿Qué insights encontraron?
    
    Que algunas especies, como la setosa, se pueden diferencias fácilmente, mientras que algunas especies, como la setosa, se pueden diferencias fácilmente, mientras que otras requieren más análisis porque sus características son más similares.
    

---

# Avance del proyecto final

## Parte 1: Base de datos

```python
#Importamos el dataset del airbnb prediction
import kagglehub

# Download latest version
path = kagglehub.dataset_download("stevezhenghp/airbnb-price-prediction")

print("Path to dataset files:", path)

#Cargamos el dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='darkgrid')

try:
    df = pd.read_csv('train.csv')
    print("Dataset cargado.")
except FileNotFoundError:
    print("Error: No se encontró el archivo .csv.")

df.head()

#Para analisis exploratorio para saber los tipos de datos

print("--- Información del Dataset ---")
print(df.info())

print("\n--- Estadísticas Univariadas ---")
display(df.describe())
```

![Screenshot 2026-04-10 at 4.56.47 p.m..png](Semana%203%20consolidada/Screenshot_2026-04-10_at_4.56.47_p.m..png)

![Screenshot 2026-04-10 at 4.56.57 p.m..png](Semana%203%20consolidada/Screenshot_2026-04-10_at_4.56.57_p.m..png)

## Parte 2: Análisis Exploratorio de Datos (EDA)

### Calcular medidas de tendencia central (moda, media, mediana, rango, varianza y desviación estándar)

```python
import math
from collections import Counter

def analizar_columna(columna):
    
    
    datos = [x for x in columna]
    
    
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

    columnas = ['log_price', 'accommodates', 'bathrooms', 'bedrooms', 'number_of_reviews', 'review_scores_rating']

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

```

![Screenshot 2026-04-10 at 4.52.50 p.m..png](Semana%203%20consolidada/5345e82d-1cad-4bb4-85d1-928e79364c33.png)

---

### Visualización de datos

```python
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

![image.png](Semana%203%20consolidada/image%204.png)

![image.png](Semana%203%20consolidada/image%205.png)

![image.png](Semana%203%20consolidada/image%206.png)

![image.png](Semana%203%20consolidada/image%207.png)