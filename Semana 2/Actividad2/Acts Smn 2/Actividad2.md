# Actividad 2 — Ciencia de Datos

**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio
**Ponderación:** 6%
**Temas relacionados:** T3, T4, T5 (Arquitecturas de almacenamiento, Bases de datos NoSQL, CRUD con MongoDB)

---

## Descripción

Imagina que eres el responsable de un proyecto de reciente creación, cuyo objetivo es examinar un conjunto de datos que contiene información sobre ventas de productos de una tienda en línea llamada "Todo ventas en Línea, S.A. de C.V." durante un período de tiempo. Se te pide realizar un análisis exploratorio de los datos para comprender de manera más profunda el rendimiento de las ventas y extraer información valiosa que contribuya a la toma de decisiones comerciales para el presente año. De la información que obtengas dependerán todas las estrategias comerciales de la organización para determinar qué producto vender más, a qué nicho de mercado dirigirse y en qué época del año reforzar las promociones.

---

## Objetivo

Reforzar el análisis exploratorio de datos utilizando Python y MongoDB para comprender mejor el rendimiento de las ventas en una tienda en línea. Este proceso incluirá la importación de datos desde MongoDB, la exploración de los mismos utilizando Pandas y NumPy y la visualización de la información a través de herramientas como Matplotlib y Seaborn.

---

## Instrucciones

Lee detenidamente las siguientes indicaciones para poder realizar la actividad:

1. **Lee los temas 5, 6, 7 y 8.**
2. **Accede a tu entorno de desarrollo de código.**
3. **Definición del problema y recopilación de datos**
   - Redacta el objetivo del proyecto y las preguntas clave que se buscan responder.
4. **Utiliza Python para generar, de manera aleatoria, los conjuntos de datos necesarios** para el ejercicio propuesto. Los conjuntos de datos deben cumplir con los siguientes requisitos:
   - Incluir al menos 10 columnas: cuatro de tipo numérico (entero o decimal), dos de tipo categórico (texto breve que representa una categoría), dos de tipo estructurado (datos con una organización predefinida) y dos de tipo no estructurado (texto libre, etc.).
   - Contener al menos 5,000 registros.
5. **Preparación de los datos:**
   - Carga los datos a MongoDB.
   - Realiza una exploración inicial de los datos para comprender su estructura y calidad. Esta fase es crucial para identificar posibles problemas de calidad de datos, como valores faltantes o atípicos, y para entender la distribución y relaciones entre las variables.
6. **Análisis exploratorio de datos:**
   - Utiliza Pandas y NumPy para realizar análisis numérico y manipulación de datos.
   - Explora la distribución de datos numéricos y categóricos mediante el uso de estadísticas descriptivas como media, mediana, moda, solamente.
   - Crea un resumen estadístico utilizando un DataFrame de Python y sus librerías requeridas, como lo son NumPy y Pandas.
   - Realiza la interpretación del análisis exploratorio.
7. **Creación de gráficas para visualización de datos:**
   - Genera una visualización a través de un diagrama de cajas utilizando Python y las bibliotecas adecuadas.
   - Crea una gráfica de dispersión para representar la relación entre variables.
   - Crea un histograma para mostrar la distribución de datos.
   - Realiza la interpretación de las gráficas creadas.

---

## Entregable(s)

> **⚠️ IMPORTANTE: La entrega se realiza a través del repositorio de GitHub**
>
> No se aceptan documentos en Word o PDF. Todo el trabajo debe estar subido a tu repositorio de GitHub.

### Estructura de entrega en GitHub:

```
Semana2/
├── Consolidado/
│   └── Semana2_Consolidado.md    # Documento consolidado semanal
├── Actividad2/
│   ├── Analisis.py                # Código Python del análisis
│   ├── datos_ventas.csv          # Dataset generado
│   └── Visualizaciones/           # Gráficas generadas
└── commits documentados
```

### Componentes de evaluación:

| Componente | Ponderación | Descripción |
|------------|-------------|-------------|
| **Actividad Evaluable** | **70% (4.2%)** | Análisis exploratorio completo con visualizaciones |
| **Ejercicios Complementarios** | **10% (0.6%)** | Ejercicios de SQL, JSON, MongoDB |
| **Actividades Prácticas Extra** | **10% (0.6%)** | Actividades 2.1 - 2.4 completadas |
| **Documentación Elaborada** | **10% (0.6%)** | Consolidado semanal organizado |

---

## Rúbrica de Evaluación

### 1. Actividad Evaluable (70% - 4.2%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| **Definición del problema** | Objetivo claro y preguntas de investigación bien definidas | 0-0.6% |
| **Generación de datos** | Dataset con 10+ columnas y 5000+ registros | 0-0.6% |
| **Conexión a MongoDB** | Datos cargados correctamente en MongoDB | 0-0.6% |
| **Análisis con Pandas/NumPy** | Estadísticas descriptivas completas | 0-0.6% |
| **Visualizaciones** | Boxplot, scatter plot e histograma | 0-0.6% |
| **Interpretación** | Análisis claro de resultados | 0-0.6% |
| **Código bien documentado** | Comentarios y estructura clara | 0-0.6% |

### 2. Ejercicios Complementarios (10% - 0.6%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Ejercicios de SQL | Resueltos correctamente | 0-0.2% |
| Ejercicios de JSON | Resueltos correctamente | 0-0.2% |
| Ejercicios de MongoDB CRUD | Resueltos correctamente | 0-0.2% |

### 3. Actividades Prácticas Extra (10% - 0.6%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Arquitecturas de Datos | Completado | 0-0.15% |
| Introducción a MongoDB | Completado | 0-0.15% |
| Operaciones CRUD | Completado | 0-0.15% |
| Modelado NoSQL | Completado | 0-0.15% |

### 4. Documentación Elaborada (10% - 0.6%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Estructura | Sigue la estructura propuesta | 0-0.15% |
| Completitud | Incluye todas las secciones | 0-0.15% |
| Calidad de contenido | Ejercicios bien resueltos | 0-0.15% |
| Reflexión | Reflexiones profundas | 0-0.15% |

---

## Calendario

- **Semana:** 2
- **Fecha de entrega:** Según calendario del curso
- **Fecha límite:** Domingo de la semana indicada

---

## Recursos

- [Tema 3: Arquitecturas de almacenamiento](Tema3.md)
- [Tema 4: Bases de datos NoSQL](Tema4.md)
- [Tema 5: CRUD con MongoDB](Tema5.md)
- [Ejercicios Complementarios Semana 2](Actividad%20Semana%202/Ejercicios%20Complementarios.md)
- [Actividades Prácticas Semana 2](Actividad%20Semana%202/Propuesta%20Actividades.md)
