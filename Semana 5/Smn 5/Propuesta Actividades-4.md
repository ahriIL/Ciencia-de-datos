# Actividades Prácticas - Semana 5

## Preparación para: Actividad 4

**Temas cubiertos:** Análisis preliminar de los datos en Python, Regresión lineal simple en Python

---

## IMPORTANTE: Ejercicios Complementarios

Antes de comenzar con las actividades prácticas, es **fundamental** completar los ejercicios del archivo [`Ejercicios Complementarios.md`](Ejercicios%20Complementarios.md).

### ¿Por qué realizar estos ejercicios?

Los ejercicios complementarios te proporcionan la base de estadística y matemáticas necesaria para:

1. **Calcular correlaciones** e interpretar coeficientes
2. **Comprender la regresión lineal** desde sus fundamentos
3. **Evaluar modelos** usando R², residuos e intervalos de confianza
4. **Realizar pruebas de hipótesis** para validar resultados

> **Justificación:** Estos conocimientos son prerrequisitos básicos que facilitan la comprensión del análisis de correlación y regresión lineal simple. Sin esta base, será más difícil completar las actividades prácticas de manera efectiva.

**Tiempo estimado:** 1-2 horas

---

## Objetivo

Estas actividades prácticas te prepararán para completar la Actividad 4, enfocándose en análisis de correlación y regresión lineal simple.

---

## GIT: Recordatorio de Comandos

```bash
# Ver estado
git status

# Agregar cambios
git add .

# Crear commit
git commit -m "Mensaje descriptivo"

# Subir al repositorio
git push origin main

# Actualizar repositorio local
git pull origin main
```

---

## Actividades Propuestas

### Actividad 5.1: Análisis de Correlación

**Descripción:** Aprende a calcular e interpretar correlaciones.

**Instrucciones:**
1. Carga un dataset con variables numéricas
2. Calcula la matriz de correlación
3. Crea un mapa de calor (heatmap)
4. Identifica las variables más correlacionadas
5. Interpreta los coeficientes de correlación
6. Discute la diferencia entre correlación y causalidad

**Carpeta de entrega:** `Semana5/Actividades/Actividad5.1/`

**Git:**
```bash
git add Semana5/Actividades/Actividad5.1/
git commit -m "Semana5: Actividad 5.1 - Análisis de correlación"
git push
```

---

### Actividad 5.2: Regresión Lineal Simple - Teoría

**Descripción:** Refuerza los conceptos teóricos de regresión lineal simple.

**Instrucciones:**
1. Investiga los supuestos de la regresión lineal:
   - Linealidad
   - Independencia
   - Homocedasticidad
   - Normalidad
2. Explica cada supuesto con tus propias palabras
3. Da un ejemplo de cómo verificar cada uno

**Carpeta de entrega:** `Semana5/Actividades/Actividad5.2/`

**Git:**
```bash
git add Semana5/Actividades/Actividad5.2/
git commit -m "Semana5: Actividad 5.2 - Teoría de regresión"
git push
```

---

### Actividad 5.3: Regresión Lineal Simple - Práctica

**Descripción:** Implementa una regresión lineal simple en Python.

**Instrucciones:**
1. Usa un dataset apropiado (ej: datos de precios de casas)
2. Selecciona una variable independiente y una dependiente
3. Divide los datos en entrenamiento y prueba
4. Implementa el modelo de regresión lineal
5. Evalúa el modelo usando R² y error cuadrático medio
6. Interpreta los coeficientes

**Carpeta de entrega:** `Semana5/Actividades/Actividad5.3/`

**Git:**
```bash
git add Semana5/Actividades/Actividad5.3/
git commit -m "Semana5: Actividad 5.3 - Regresión lineal simple"
git push
```

---

### Actividad 5.4: Diagnóstico del Modelo

**Descripción:** Verifica los supuestos de la regresión.

**Instrucciones:**
1. Continúa con el modelo de la actividad anterior
2. Crea gráficas para verificar:
   - Residuos vs valores ajustados
   - Q-Q plot de residuos
   - Histograma de residuos
3. Calcula estadísticas de diagnóstico
4. Concluye si el modelo cumple los supuestos

**Carpeta de entrega:** `Semana5/Actividades/Actividad5.4/`

**Git:**
```bash
git add Semana5/Actividades/Actividad5.4/
git commit -m "Semana5: Actividad 5.4 - Diagnóstico del modelo"
git push
```

---

## Actualizar Documentación Semanal

Crea/actualiza el archivo `Documentacion/Semana5.md`:

```markdown
# Semana 5: Análisis de Correlación y Regresión Simple

## Fecha: [DD/MM/AAAA]

## Actividades Completadas
- [ ] Actividad 5.1: Análisis de Correlación
- [ ] Actividad 5.2: Teoría de Regresión
- [ ] Actividad 5.3: Regresión Lineal Simple
- [ ] Actividad 5.4: Diagnóstico del Modelo

## Resultados del Modelo
- [Documenta los resultados de tu modelo]

## Dudas o Bloqueos
- [Si tienes alguna duda]

## Commits Realizados
- Listar los commits de esta semana
```

**Git:**
```bash
git add Documentacion/Semana5.md
git commit -m "Semana5: Documentación actualizada"
git push
```

---

## Actualizar README

```bash
git add README.md
git commit -m "Update README: Semana 5 completada"
git push
```

---

## Recursos Adicionales

- Scikit-learn Linear Regression: https://scikit-learn.org/stable/modules/linear_model.html
- Statsmodels: https://www.statsmodels.org/stable/index.html

---

## Recordatorio

La Actividad 4 tiene una ponderación del 6% y cubre los Temas 11 y 12 del temario.

---

## 📋 Consolidado Semanal: Semana 5

Al finalizar todas las actividades de esta semana, debes crear un archivo consolidado llamado `Semana5_Consolidado.md` que contenga:

### Estructura del consolidado:

```markdown
# Semana 5: Análisis de Correlación y Regresión Lineal Simple

## 1. Ejercicios Complementarios

### Ejercicio 1: [Nombre]
**Solución:**
[Tu respuesta/solución]

### Ejercicio 2: [Nombre]
**Solución:**
[Tu respuesta/solución]

## 2. Actividades Prácticas

### Actividad 5.1: [Nombre]
**Entregable:** [Descripción]

### Actividad 5.3: [Nombre]
**Entregable:** [Descripción]

## 3. Resultados del Modelo

- R²: [Valor]
- RMSE: [Valor]
- Coeficientes: [Valores]

## 4. Resumen de Aprendizaje

- [Aprendizaje 1]
- [Aprendizaje 2]
- [Aprendizaje 3]

## 5. Dudas o Preguntas

- [Pregunta 1]
- [Pregunta 2]

## 6. Referencias

- [Referencia 1]
- [Referencia 2]
```

### Instrucciones de entrega:
1. Completa todos los ejercicios y actividades
2. Organiza todo en el archivo consolidado
3. Guarda en `Semana5/Semana5_Consolidado.md`
4. Realiza el commit correspondiente:
   ```bash
   git add Semana5/
   git commit -m "Semana5: Consolidado completo"
   git push
   ```

---

## ✅ Actividad Evaluable: Actividad 4

**Fecha de entrega:** [Según calendario del curso]

**Ponderación:** 6%

**Temas evaluados:** T11 y T12

**Instrucciones:**
1. Completa todos los ejercicios complementarios
2. Completa todas las actividades prácticas
3. Construye y evalúa tu modelo de regresión
4. Verifica tu consolidado semanal
5. Entrega según las indicaciones del profesor

**Criterios de evaluación:**
- [ ] Completó los ejercicios complementarios
- [ ] Completó todas las actividades prácticas
- [ ] Modelo de regresión correctamente implementado
- [ ] Diagnóstico de supuestos realizado
- [ ] El consolidado está organizado y completo
- [ ] Commits realizados correctamente en Git
