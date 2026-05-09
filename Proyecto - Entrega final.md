# Proyecto: Entrega Final — Ciencia de Datos

**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio
**Ponderación:** 35%
**Temas relacionados:** T16, T17, T18 (Regresión logística binaria en Python - Partes 1 y 2, Estrategias de comunicación de datos en Python)

---

## Descripción

En la segunda fase del proyecto, aplicarás técnicas avanzadas de ciencia de datos para desarrollar modelos predictivos basados en los datos explorados anteriormente. Asimismo, utilizarás técnicas de visualización de datos avanzadas para comunicar de forma eficiente los insights obtenidos.

---

## Objetivo

Aplicar técnicas de modelado predictivo para analizar el mercado inmobiliario y comunicar los resultados de manera efectiva.

---

## Requerimientos

- Los datos obtenidos en la fase I (Avance del Proyecto).
- Google Colab o entorno local con Python.

---

## Instrucciones

### Parte 1: Modelo de regresión lineal múltiple

1. **Limpieza de datos:** utiliza Pandas para limpiar tus datos. Incluye la eliminación o imputación de valores faltantes e identificación y corrección de errores (por ejemplo: valores atípicos extremos que claramente son incorrectos).

2. **Identificación de variables:** define cuál es la variable dependiente y cuáles son las variables independientes.

3. **Selección de características:** determina qué variables incluir en el modelo. Esto puede requerir realizar más análisis exploratorio para evaluar la importancia de las distintas características.

4. **Análisis de correlación:** emplea Seaborn para generar un pairplot que muestre las relaciones entre las variables.

5. **Grupos de entrenamiento y prueba:** divide el conjunto de datos en un grupo de entrenamiento y otro de prueba.

6. **Construcción y entrenamiento del modelo:** construye y entrena un modelo de regresión lineal múltiple con las variables seleccionadas. Es importante considerar la multicolinealidad y la relevancia de cada variable en el modelo.

7. **Evaluación del modelo:** evalúa el modelo mediante métricas de regresión, enfocándote en el R² y el ajuste de los datos. Interpreta estos valores para entender la calidad del modelo.

8. **Predicciones:** utiliza el modelo para realizar predicciones sobre el conjunto de prueba y comparar estas predicciones con los valores reales para evaluar la precisión del modelo.

9. **Cálculo del error cuadrático medio (MSE):** calcula el MSE como una medida del error de las predicciones realizadas por el modelo.

### Parte 2: Comunicación de los resultados

1. Crea visualizaciones que comuniquen los resultados del modelo, como gráficos de dispersión de predicciones vs. valores reales o gráficos de importancia de las características.

2. Desarrolla una narrativa que acompañe a las visualizaciones, y explica los resultados del análisis, la precisión del modelo y cómo las características influyen en los precios de las viviendas.

---

## Entregable(s)

> **⚠️ IMPORTANTE: La entrega se realiza a través del repositorio de GitHub**
>
> No se aceptan documentos en Word, PDF o PowerPoint. Todo el trabajo debe estar subido a tu repositorio de GitHub.

### Estructura de entrega en GitHub:

```
Semana7/
├── Consolidado/
│   └── Semana7_Consolidado.md    # Documento consolidado semanal
├── Proyecto/
│   ├── Final/
│   │   ├── Modelo.py              # Código del modelo
│   │   ├── Limpieza.py            # Código de limpieza
│   │   ├── Datos/                 # Datasets utilizados
│   │   └── Visualizaciones/       # Gráficas generadas
│   ├── Presentacion/              # Presentación (en Markdown)
│   └── README.md                  # Documentación del proyecto
└── commits documentados
```

### Componentes de evaluación:

| Componente | Ponderación | Descripción |
|------------|-------------|-------------|
| **Actividad Evaluable** | **70% (24.5%)** | Modelo predictivo y comunicación |
| **Ejercicios Complementarios** | **10% (1.7%)** | Regresión logística, métricas, visualización |
| **Actividades Prácticas Extra** | **10% (1.7%)** | Actividades 7.1 - 7.5 completadas |
| **Documentación Elaborada** | **10% (1.7%)** | Consolidado semanal organizado |

---

## Rúbrica de Evaluación

### 1. Actividad Evaluable (70% - 24.5%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| **Parte 1: Modelo de Regresión** | | |
| Limpieza de datos | Valores faltantes e outliers manejados | 0-3% |
| Identificación de variables | Variables dependientes e independientes definidas | 0-2% |
| Selección de características | Variables relevantes seleccionadas | 0-3% |
| Análisis de correlación | Pairplot generado e interpretado | 0-2% |
| División de datos | Train/test split apropiado | 0-2% |
| Construcción del modelo | Regresión múltiple implementada | 0-3% |
| Manejo de multicolinealidad | VIF calculado o solución aplicada | 0-2.5% |
| Evaluación del modelo | R² y R² ajustado interpretados | 0-2% |
| Predicciones | Predicciones sobre test set | 0-2% |
| MSE | Error calculado e interpretado | 0-3% |
| **Parte 2: Comunicación** | | |
| Visualizaciones | Gráficos de predicciones vs reales | 0-2% |
| Importancia de características | Gráfico de coeficientes | 0-2% |
| Narrativa | Storyline que explica resultados | 0-2% |
| Conclusiones | Recomendaciones basadas en el análisis | 0-2% |

### 2. Ejercicios Complementarios (10% - 1.7%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Regresión Logística - Teoría | Completados | 0-0.4% |
| Odds y Odds Ratio | Completados | 0-0.45% |
| Matriz de Confusión | Completados | 0-0.45% |
| Curva ROC/AUC | Completados | 0-0.4% |

### 3. Actividades Prácticas Extra (10% - 1.7%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Regresión Logística - Intro | Completado | 0-0.35% |
| Implementación | Completado | 0-0.4% |
| Métricas de Evaluación | Completado | 0-0.5% |
| Comunicación de Resultados | Completado | 0-0.45% |

### 4. Documentación Elaborada (10% - 1.7%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Estructura | Sigue la estructura propuesta | 0-0.4% |
| Completitud | Incluye todas las secciones | 0-0.45% |
| Calidad de contenido | Ejercicios bien resueltos | 0-0.45% |
| Reflexión | Reflexiones profundas | 0-0.4% |

---

## Calendario

- **Semana:** 7
- **Fecha de entrega:** Según calendario del curso
- **Fecha límite:** Domingo de la semana indicated

---

## Recursos

- [Tema 16: Regresión logística binaria - parte 1](Tema16.md)
- [Tema 17: Regresión logística binaria - parte 2](Tema17.md)
- [Tema 18: Estrategias de comunicación](Tema18.md)
- [Ejercicios Complementarios Semana 7](Actividad%20Semana%207/Ejercicios%20Complementarios.md)
- [Actividades Prácticas Semana 7](Actividad%20Semana%207/Propuesta%20Actividades.md)
