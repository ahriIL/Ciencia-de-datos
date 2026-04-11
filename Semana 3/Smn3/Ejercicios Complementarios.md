# Ejercicios Complementarios - Semana 3

## Temas Cubiertos
- **T6**: Python para ciencia de datos
- **T7**: El proceso de ciencia de datos
- **T8**: Análisis exploratorio de datos en Python

## Prerrequisitos Recomendados
- **Programación**: Python básico (variables, funciones, loops)
- **Estadística**: Medidas de tendencia central, distribuciones, percentiles
- **Librerías**: NumPy, Pandas, Matplotlib

---

## Ejercicios de Python Básico

### Ejercicio 1: Variables y Tipos de Datos
```python
# Ejercicios:
# 1. Crear variables de diferentes tipos: int, float, str, bool, list, dict
# 2. Convertir tipos: str a int, float a int, int a float
# 3. Usar f-strings para formatear: "El usuario tiene X años"
```

### Ejercicio 2: Control de Flujo
```python
# Ejercicios:
# 1. Crear un programa que determine si un número es positivo, negativo o cero
# 2. Crear un menú con if-elif-else
# 3. Usar un loop for para iterar sobre una lista
# 4. Usar while para calcular factorial
```

### Ejercicio 3: Funciones
```python
# Crear funciones para:
# 1. Calcular el área de un círculo
# 2. Convertir Celsius a Fahrenheit
# 3. Calcular el promedio de una lista
# 4. Encontrar el valor máximo y mínimo
```

---

## Ejercicios de NumPy

### Ejercicio 4: Operaciones con Arrays
```python
import numpy as np

# Crear arrays y realizar operaciones:
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# Ejercicios:
# 1. Sumar los arrays elemento a elemento
# 2. Multiplicar por un escalar
# 3. Calcular la media, mediana y desviación estándar
# 4. Encontrar valores únicos
# 5. Reshape de un array 1D a 2D
```

### Ejercicio 5: Álgebra con NumPy
```python
# Dados los vectores v1 = [1, 2, 3] y v2 = [4, 5, 6]
# Calcular:
# 1. Producto punto
# 2. Producto cruz
# 3. Magnitud de cada vector
# 4. Normalización de vectores
```

---

## Ejercicios de Pandas

### Ejercicio 6: DataFrames Básico
```python
import pandas as pd

# Crear un DataFrame con datos de estudiantes
data = {
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Sofia'],
    'edad': [20, 22, 19, 21, 23],
    'carrera': ['Ing', 'Ing', 'Lic', 'Ing', 'Lic'],
    'promedio': [8.5, 9.0, 7.8, 8.2, 9.5]
}

df = pd.DataFrame(data)

# Ejercicios:
# 1. Seleccionar columna 'nombre'
# 2. Filtrar estudiantes con promedio > 8.5
# 3. Ordenar por edad
# 4. Agregar columna 'aprobado' (promedio >= 7)
# 5. Group by carrera y promediar
```

### Ejercicio 7: Manipulación de Datos
```python
# Dado el DataFrame anterior:
# 1. Manejar valores faltantes (agregar NaN y llenarlos)
# 2. Eliminar duplicados
# 3. Aplicar funciones con apply()
# 4. Usar loc e iloc para slicing
# 5. Concatenar dos DataFrames
```

---

## Ejercicios de Visualización

### Ejercicio 8: Matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crear visualizaciones:
# 1. Gráfico de línea básico
# 2. Gráfico de dispersión
# 3. Histograma
# 4. Gráfico de barras
# 5. Personalizar: títulos, etiquetas, leyenda, colores
```

### Ejercicio 9: Análisis Exploratorio
```python
# Usando un dataset (puede ser 'iris' o cualquier otro)
import pandas as pd
import seaborn as sns

# Ejercicios:
# 1. Cargar dataset y mostrar info básica
# 2. Calcular estadísticas descriptivas
# 3. Crear histogramas de todas las columnas numéricas
# 4. Crear matriz de correlación
# 5. Crear boxplots por categoría
# 6. Identificar outliers
```

---

## Ejercicios de Estadística

### Ejercicio 10: Medidas de Tendencia Central
Calcular manualmente (sin funciones built-in):

| Datos       | Media | Mediana | Moda   |
| ----------- | ----- | ------- | ------ |
| [5, 3, 8, 3, 7] |       |         |        |
| [10, 20, 30, 40]|       |         |        |
| [1, 2, 2, 3, 3, 3, 4]|   |         |        |

### Ejercicio 11: Dispersion
Calcular:

| Datos       | Rango | Varianza | Desviación Estándar |
| ----------- | ----- | -------- | ------------------- |
| [2, 4, 4, 4, 5, 5, 7, 9] |       |          |                     |
| [1, 3, 5, 7, 9]     |       |          |                     |

---

## Ejercicios de Investigación

### Ejercicio 12: El Proceso de Data Science
Investigar y explicar:
1. ¿Qué es el ciclo CRISP-DM?
2. ¿Cuáles son las fases del proceso de ciencia de datos?
3. ¿Qué es el MVP (Minimum Viable Product) en ciencia de datos?

### Ejercicio 13: Caso de Estudio
Investigar un caso real de análisis exploratorio de datos:
- ¿Qué preguntas buscaban responder?
- ¿Qué técnicas usaron?
- ¿Qué insights encontraron?

---

## Recursos Adicionales

### Práctica Interactiva
- Python.org - Tutorial oficial
- Pandas Exercises en GitHub
- Kaggle - Titanic dataset practice

### Videos
- Corey Schafer - Python Tutorials
- Keith Galli - Pandas & NumPy tutorials

---

## Próxima Semana
En la Semana 4 cubriremos:
- **T9**: Preparación de los datos en Python
- **T10**: Procesamiento de datos en Python

**Prerrequisitos para próxima semana:**
- Normalización y estandarización
- Valores atípicos (outliers)
- Manipulación de DataFrames
- Transformaciones de variables
