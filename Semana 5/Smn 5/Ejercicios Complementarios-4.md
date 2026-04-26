# Ejercicios Complementarios - Semana 5

## Temas Cubiertos
- **T11**: Análisis preliminar de los datos en Python
- **T12**: Regresión lineal simple en Python

## Prerrequisitos Recomendados
- **Matemáticas**: Correlación, covarianza, funciones lineales, pendientes, intersecciones
- **Estadística**: Coeficiente de Pearson, prueba t, p-valores, intervalos de confianza, R², residuos
- **Programación**: Implementación de fórmulas básicas

---

## Ejercicios de Correlación y Covarianza

### Ejercicio 1: Calcular Covarianza Manualmente
Dados los datos:
- X = [1, 2, 3, 4, 5]
- Y = [2, 4, 5, 4, 5]

Calcular:
1. Media de X y Y
2. Covarianza usando la fórmula:
   ```
   Cov(X,Y) = Σ(xi - x̄)(yi - ȳ) / (n-1)
   ```

### Ejercicio 2: Correlación de Pearson
La fórmula del coeficiente de correlación de Pearson:

```
r = Cov(X,Y) / (σX * σY)
```

Para los mismos datos del ejercicio anterior:
1. Calcular desviaciones estándar de X y Y
2. Calcular r
3. Interpretar el resultado (-1 a 1)

### Ejercicio 3: Correlación en Python
```python
import pandas as pd
import numpy as np
from scipy import stats

# Crear datos de ejemplo
df = pd.DataFrame({
    'horas_estudio': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'calificacion': [35, 45, 50, 55, 65, 70, 75, 85, 90, 95]
})

# Ejercicios:
# 1. Calcular correlación con .corr()
# 2. Calcular p-value con scipy.stats
# 3. Crear scatter plot
# 4. Calcular covarianza
```

---

## Ejercicios de Intervalos de Confianza

### Ejercicio 4: Intervalo de Confianza para la Media
Dados los datos de muestra:
- n = 25
- x̄ = 100
- s = 15
- Nivel de confianza = 95%

**Fórmula:**
```
IC = x̄ ± t * (s / √n)
```
Dónde t es el valor t deStudent para 24 grados de libertad

1. Buscar t para 95% y 24 gl
2. Calcular el intervalo
3. Interpretar

### Ejercicio 5: Cálculo de p-valor
Para una prueba de hipótesis:
- H0: μ = 50
- Ha: μ ≠ 50
- n = 30
- x̄ = 55
- s = 10

1. Calcular estadístico t
2. Encontrar p-valor (usar tabla o Python)
3. Decidir si rechazar H0 (α = 0.05)

---

## Ejercicios de Regresión Lineal Simple

### Ejercicio 6: Fórmula de Regresión Lineal
La ecuación de regresión lineal simple:

```
ŷ = β0 + β1*x
```

Dónde:
- β1 = Cov(X,Y) / Var(X)
- β0 = ȳ - β1 * x̄

Para los datos:
- X = [1, 2, 3, 4, 5]
- Y = [2, 4, 5, 4, 5]

1. Calcular β1 (pendiente)
2. Calcular β0 (intercepto)
3. Escribir la ecuación
4. Predecir Y para X = 6

### Ejercicio 7: Implementación en Python
```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([2, 4, 5, 4, 5, 6, 7, 8, 9, 11])

# Crear y entrenar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Obtener parámetros
print(f"Intercepto: {modelo.intercept_}")
print(f"Pendiente: {modelo.coef_[0]}")

# Predecir
prediccion = modelo.predict([[11]])
print(f"Predicción para X=11: {prediccion}")
```

---

## Ejercicios de Evaluación de Modelos

### Ejercicio 8: Coeficiente de Determinación (R²)
```python
from sklearn.metrics import r2_score

# Valores reales y predichos
y_real = [1, 2, 3, 4, 5]
y_predicho = [1.1, 2.2, 2.9, 4.1, 4.9]

# Calcular R² manualmente
SS_res = sum((y - pred)**2 for y, pred in zip(y_real, y_predicho))
SS_tot = sum((y - sum(y_real)/len(y_real))**2 for y in y_real)

r2 = 1 - (SS_res / SS_tot)
print(f"R²: {r2}")

# Verificar con sklearn
print(f"R² sklearn: {r2_score(y_real, y_predicho)}")
```

### Ejercicio 9: Error Estándar de la Estimación
```python
# Calcular RMSE y MAE
from sklearn.metrics import mean_squared_error, mean_absolute_error

y_real = [10, 20, 30, 40, 50]
y_predicho = [12, 18, 32, 38, 52]

rmse = np.sqrt(mean_squared_error(y_real, y_predicho))
mae = mean_absolute_error(y_real, y_predicho)

print(f"RMSE: {rmse}")
print(f"MAE: {mae}")
```

---

## Ejercicios de Diagnóstico

### Ejercicio 10: Análisis de Residuos
```python
import matplotlib.pyplot as plt

# Datos de ejemplo
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_real = np.array([2.1, 4.2, 5.8, 4.3, 5.5, 6.8, 7.5, 8.2, 9.1, 10.5])
y_predicho = [2.3, 4.1, 5.9, 4.2, 5.6, 6.5, 7.4, 8.3, 9.0, 10.4]

residuos = np.array(y_real) - np.array(y_predicho)

# Gráficos de diagnóstico:
# 1. Residuos vs Predichos (heterocedasticidad)
# 2. Histograma de residuos (normalidad)
# 3. Q-Q plot (normalidad)
# 4. Residuos vs Orden (autocorrelación)
```

### Ejercicio 11: Supuestos de Regresión
Investigar y explicar:
1. **Linealidad**: ¿Cómo verificarla?
2. **Independencia**: ¿Qué es la autocorrelación?
3. **Homocedasticidad**: ¿Qué es y cómo detectarla?
4. **Normalidad**: ¿Qué es Q-Q plot?

---

## Ejercicios de Prueba de Hipótesis

### Ejercicio 12: Prueba t para Correlación
```python
from scipy import stats

# Datos
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 4, 5, 6, 7, 8, 9, 11]

# Calcular correlación y p-valor
r, p_value = stats.pearsonr(x, y)

print(f"r: {r}")
print(f"p-value: {p_value}")

# Decisión para α = 0.05
if p_value < 0.05:
    print("Rechazar H0: La correlación es significativa")
else:
    print("No rechazar H0: La correlación no es significativa")
```

---

## Ejercicios de Investigación

### Ejercicio 13: Aplicaciones de Regresión Lineal
Investigar:
1. ¿Qué es la regresión a la media?
2. Ejemplos de uso en negocios
3. Diferencia entre correlación y causalidad

### Ejercicio 14: Limitaciones
Investigar:
1. ¿Por qué la regresión lineal simple no captura relaciones no lineales?
2. ¿Qué es la extrapolación y por qué es riesgosa?
3. ¿Qué es el problema de la variable omitida?

---

## Recursos Adicionales

### Videos
- StatQuest - Linear Regression
- Khan Academy - Statistics

### Práctica
- Khan Academy - Correlation and regression
- SPSS Tutorials - Linear regression

---

## Próxima Semana
En la Semana 6 cubriremos:
- **T13**: Regresión lineal múltiple - parte 1
- **T14**: Regresión lineal múltiple - parte 2
- **T15**: Regresión lineal múltiple - parte 3

**Prerrequisitos para próxima semana:**
- Álgebra matricial
- Multicolinealidad
- Diagnóstico de residuos
- Regularización (Ridge, Lasso, Elastic Net)
- Validación cruzada
