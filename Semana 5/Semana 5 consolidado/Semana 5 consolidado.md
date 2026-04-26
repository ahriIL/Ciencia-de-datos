# Actividad 5

## **Objetivo**

---

Reforzar los conocimientos sobre regresión lineal múltiple y regresión logística binaria para analizar datos y generar predicción

---

## **Instrucciones**

### **Parte 1: Predicción de ventas usando regresión lineal múltiple**

En esta sección de la actividad, crearás y evaluarás un modelo de regresión lineal múltiple para predecir las ventas de los vehículos de acuerdo con el precio de venta establecido y el kilometraje de los mismos.

---

1. **Preparación de los datos:** Guarda la base de datos en una variable. Los datos los obtendrás de la siguiente liga: [https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data/download?datasetVersionNumber=1](https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data/download?datasetVersionNumber=1)
    
    ```python
    import kagglehub
    import pandas as pd
    import os
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    # preparación de los datos
    path = kagglehub.dataset_download("syedanwarafridi/vehicle-sales-data")
    
    archivos = os.listdir(path)
    
    archivoCvs = os.path.join(path, 'car_prices.csv') 
    df = pd.read_csv(archivoCvs)
    
    print(df.head())
    
    #limpiar
    print(df.isnull().sum())
    dfClean = df.dropna()
    
    # Limpiamos, corregimos valores valentes o errôneos y eliminamos columnas innecesarias
    ```
    
2. **Análisis exploratorio:** Realiza una gráfica de dispersión para verificar la relación que existe entre el precio, el kilometraje y las ventas. Para esto, utiliza pairplot de la biblioteca Seaborn, la cual te permitirá visualizar las relaciones entre estas variables.
    
    ```python
    #analisis exploratorio
    #odometer es kilometraje
    
    variableIntereses = ['sellingprice','odometer', 'year']
    
    #grafico
    sns.set_theme(style="whitegrid")
    
    grafico = sns.pairplot(dfClean[variableIntereses], kind='reg', diag_kind='kde', plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.3}})
    
    plt.suptitle("Relación entre Precio, Kilometraje y Valor de Mercado", y=1.02)
    plt.show()
    ```
    
    ![Screenshot 2026-04-21 at 2.26.32 p.m..png](Actividad%205/Screenshot_2026-04-21_at_2.26.32_p.m..png)
    
    ![image.png](Actividad%205/image.png)
    
3. **Identificación de variables:** Determina cuáles son las variables independientes y cuál es la dependiente.
    
    ```python
    # identificacion de variables
    y = dfClean['sellingprice']
    
    X = dfClean[['odometer', 'mmr']]
    
    print("Variable dependiente (Y): sellingprice")
    print("Variables independientes (X):", X.columns.tolist())
    
    ```
    
    ![Screenshot 2026-04-26 at 11.32.58 a.m..png](Actividad%205/Screenshot_2026-04-26_at_11.32.58_a.m..png)
    
4. **División de datos:** Crea los grupos de entrenamiento y de prueba para tus variables. Esta división es esencial para entrenar tu modelo con un conjunto de datos y evaluar su rendimiento con otro, asegurando así que el modelo sea capaz de generalizar a nuevos datos.
    
    ```python
    # division de datos
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )
    
    print(f"Entrenamiento: {X_train.shape[0]} filas")
    print(f"Prueba:        {X_test.shape[0]} filas")
    ```
    
    ![Screenshot 2026-04-26 at 11.33.32 a.m..png](Actividad%205/Screenshot_2026-04-26_at_11.33.32_a.m..png)
    
5. **Modelado:** Aplica el modelo de regresión lineal múltiple.
    
    ```python
    # Modelado
    from sklearn.linear_model import LinearRegression
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    print("Intercepto:", round(modelo.intercept_, 2))
    print("Coeficiente odometer:", round(modelo.coef_[0], 6))
    print("Coeficiente year:",     round(modelo.coef_[1], 2))
    ```
    
    ![Screenshot 2026-04-26 at 11.34.01 a.m..png](Actividad%205/Screenshot_2026-04-26_at_11.34.01_a.m..png)
    
6. **Error cuadrático medio:** Este paso te ayudará a entender la magnitud de los errores cometidos por el modelo en sus predicciones.
7. **Evaluación del modelo:** Puedes utilizar métricas como el R² (coeficiente de determinación) para entender qué tan bien el modelo se ajusta a los datos.
    
    ```python
    #evaluacion del modelo
    from sklearn.metrics import r2_score, mean_squared_error
    
    y_pred = modelo.predict(X_test)
    
    #eror cuadratico medio
    r2  = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    
    print(f"R²:   {r2:.4f}")
    print(f"MSE:  {mse:,.2f}")
    print(f"RMSE: {rmse:,.2f}")
    ```
    
    ![Screenshot 2026-04-26 at 11.34.23 a.m..png](Actividad%205/Screenshot_2026-04-26_at_11.34.23_a.m..png)
    
8. **Predicción:** Con el modelo ya entrenado y evaluado, procede a realizar las predicciones.
    
    ```python
    #prediccion
    
    plt.figure(figsize=(8, 5))
    plt.scatter(y_test[:3000], y_pred[:3000], alpha=0.3, s=8)
    plt.plot([0, 80000], [0, 80000], 'r--', label='predicción perfecta')
    plt.xlabel('Precio real')
    plt.ylabel('Precio predicho')
    plt.title('Real vs Predicho')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    nuevoDato = pd.DataFrame({'odometer': [60000], 'mmr': [15000]})
    precioPredicho = modelo.predict(nuevoDato)
    print(f"Precio estimado: ${precioPredicho[0]:,.2f}")
    
    ```
    
    ![Screenshot 2026-04-26 at 11.34.49 a.m..png](Actividad%205/e73c740e-3fa9-4295-9fd7-21311cc09a75.png)
    
9. **Conclusión:** Finalmente, elabora una conclusión con base en los resultados obtenidos. Reflexiona sobre la eficacia del modelo de regresión lineal múltiple para predecir las ventas de vehículos. Considera posibles mejoras o ajustes para futuros modelos.
    
    Hallazgo 1: El kilometraje tiene una relación negativa con el precio.
    Por cada kilómetro adicional el precio baja aproximadamente $0.06,
    lo que indica que los autos con menos uso mantienen mejor su valor.
    
    Hallazgo 2: El valor estimado de mercado (mmr) es el predictor más
    fuerte 1, lo que significa que el precio de venta sigue muy de 
    cerca al valor estimado del mercado. Esto puede
    ayudar a los vendedores a fijar precios competitivos.
    

---

1. **Preparación de los datos:** Guarda la base de datos en una variable. Los datos los obtendrás de la siguiente liga: [https://www.openml.org/data/get_csv/16826755/phpMYEkMl](https://www.openml.org/data/get_csv/16826755/phpMYEkMl).
    
    ```python
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report, confusion_matrix
    from scipy import stats
    
    # prepariacion de datos
    url = 'https://www.openml.org/data/get_csv/16826755/phpMYEkMl'
    df = pd.read_csv(url)
    
    print(df.head())
    print("\nColumnas disponibles:", df.columns.tolist())
    print("\nForma del dataset:", df.shape)
    ```
    
    ![Screenshot 2026-04-26 at 11.52.06 a.m..png](Actividad%205/Screenshot_2026-04-26_at_11.52.06_a.m..png)
    
2. **Limpieza de datos:** Examina las columnas disponibles en tu conjunto de datos y decide cuáles no son necesarias para tu análisis, elimina las que no consideres necesarias. Además, identifica los datos nulos que tengas y elimínalos.
3. **Conversión de variables a su formato correcto:** Dependiendo de las variables en tu conjunto de datos, es posible que necesites convertir algunas de ellas a un tipo de dato más apropiado, como convertir variables categóricas a tipo 'category' o ajustar las fechas a un formato de fecha y hora.
    
    ```python
    #limpieza de datos
    columnasEliminar = ['name', 'ticket', 'cabin', 'boat', 'body', 'home.dest']
    dfCleanTitanic = dfTitanic.drop(columns=columnasEliminar)
    
    print("Valores nulos:")
    print(dfCleanTitanic.isnull().sum())
    
    #conversion de variables
    dfCleanTitanic['sex'] = dfCleanTitanic['sex'].map({'female': 1, 'male': 0})
    dfCleanTitanic['age'] = pd.to_numeric(dfCleanTitanic['age'], errors='coerce')
    dfCleanTitanic['fare'] = pd.to_numeric(dfCleanTitanic['fare'], errors='coerce')
    
    dfCleanTitanic = dfCleanTitanic.dropna()
    print(f"\nFilas restantes después de limpiar: {len(dfCleanTitanic)}")
    
    dfCleanTitanic = dfCleanTitanic.dropna(subset=['survived', 'sex', 'age', 'fare', 'embarked', 'pclass'])
    
    dfCleanTitanic['age'] = dfCleanTitanic['age'].astype(float)
    print("Filas después de limpiar:", len(dfCleanTitanic))
    ```
    
    ![Screenshot 2026-04-26 at 12.50.56 p.m..png](Actividad%205/Screenshot_2026-04-26_at_12.50.56_p.m..png)
    
4. **Visualización de datos:** Analiza los datos de forma gráfica para verificar que existe una relación entre la variable dependiente y la independiente.
    
    ```python
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 3, figsize=(14, 10))
    
    # sex vs survived
    tasaSexo = dfCleanTitanic.groupby('sex')['survived'].mean()
    axes[0,0].bar(tasaSexo.index, tasaSexo.values, color=['#3498db', '#e74c3c'])
    axes[0,0].set_title('Sexo vs Sobrevivencia')
    axes[0,0].set_xticks([0, 1])
    axes[0,0].set_xticklabels(['Male (0)', 'Female (1)'])
    axes[0,0].set_ylabel('Tasa de sobrevivencia')
    
    # age vs survived
    sns.kdeplot(data=dfCleanTitanic[dfCleanTitanic['survived']==1], x='age',
                ax=axes[0,1], label='Sobrevivió', color='#27ae60', fill=True, alpha=0.3)
    sns.kdeplot(data=dfCleanTitanic[dfCleanTitanic['survived']==0], x='age',
                ax=axes[0,1], label='No sobrevivió', color='#e74c3c', fill=True, alpha=0.3)
    axes[0,1].set_title('Edad vs Sobrevivencia')
    axes[0,1].set_xlabel('Edad')
    axes[0,1].legend()
    
    # fare vs survived
    sns.boxplot(data=dfCleanTitanic, x='survived', y='fare', ax=axes[0,2],
                palette=['#e74c3c', '#27ae60'])
    axes[0,2].set_title('Tarifa vs Sobrevivencia')
    axes[0,2].set_xticklabels(['No sobrevivió', 'Sobrevivió'])
    
    # sibsp vs survived
    tasaSibsp = dfCleanTitanic.groupby('sibsp')['survived'].mean()
    axes[1,0].bar(tasaSibsp.index, tasaSibsp.values, color='#3498db')
    axes[1,0].set_title('Hermanos/Cónyuge vs Sobrevivencia')
    axes[1,0].set_xlabel('sibsp')
    axes[1,0].set_ylabel('Tasa de sobrevivencia')
    
    # parch vs survived
    tasaParch = dfCleanTitanic.groupby('parch')['survived'].mean()
    axes[1,1].bar(tasaParch.index, tasaParch.values, color='#9b59b6')
    axes[1,1].set_title('Padres/Hijos vs Sobrevivencia')
    axes[1,1].set_xlabel('parch')
    axes[1,1].set_ylabel('Tasa de sobrevivencia')
    
    # clase vs survived
    tasaClase = dfCleanTitanic.groupby('pclass')['survived'].mean()
    axes[1,2].bar(tasaClase.index, tasaClase.values, color=['#27ae60', '#f39c12', '#e74c3c'])
    axes[1,2].set_title('Clase vs Sobrevivencia')
    axes[1,2].set_xticks([1, 2, 3])
    axes[1,2].set_xticklabels(['1ra clase', '2da clase', '3ra clase'])
    axes[1,2].set_ylabel('Tasa de sobrevivencia')
    
    plt.tight_layout()
    plt.show()
    ```
    
    ![image.png](Actividad%205/image%201.png)
    
5. **Prueba t-test:** Esta puede ayudarte a entender si las diferencias en las medias de dos grupos son estadísticamente significativas.
    
    ```python
    # Prueba t-test 
    edadSobrevivio   = dfCleanTitanic[dfCleanTitanic['survived']==1]['age']
    edadNoSobrevivio = dfCleanTitanic[dfCleanTitanic['survived']==0]['age']
    
    tStat, pValue = stats.ttest_ind(edadSobrevivio, edadNoSobrevivio)
    
    print("T-Test — Edad:")
    print(f"  Media sobrevivió:    {edadSobrevivio.mean():.2f} años")
    print(f"  Media no sobrevivió: {edadNoSobrevivio.mean():.2f} años")
    print(f"  p-value: {pValue:.4f}")
    
    if pValue < 0.05:
        print("  p < 0.05 → la edad SÍ es relevante para predecir sobrevivencia")
    else:
        print("  p >= 0.05 → la edad NO es significativa")
    
    tarifaSobrevivio   = dfCleanTitanic[dfCleanTitanic['survived']==1]['fare']
    tarifaNoSobrevivio = dfCleanTitanic[dfCleanTitanic['survived']==0]['fare']
    
    tStat2, pValue2 = stats.ttest_ind(tarifaSobrevivio, tarifaNoSobrevivio)
    
    print("\nT-Test — Tarifa:")
    print(f"  Media sobrevivió:    {tarifaSobrevivio.mean():.2f}")
    print(f"  Media no sobrevivió: {tarifaNoSobrevivio.mean():.2f}")
    print(f"  p-value: {pValue2:.4f}")
    
    if pValue2 < 0.05:
        print("  p < 0.05 → la tarifa SÍ es relevante para predecir sobrevivencia")
    else:
        print("  p >= 0.05 → la tarifa NO es significativa")
    ```
    
    ![Screenshot 2026-04-26 at 12.52.49 p.m..png](Actividad%205/Screenshot_2026-04-26_at_12.52.49_p.m..png)
    
6. **División de datos:** Divide los datos en variables de prueba y de entrenamiento. Esto es crucial para entrenar el modelo y luego evaluar su capacidad para generalizar a nuevos datos.
    
    ```python
    # Division de datos
    
    #variable dependiente
    y = dfCleanTitanic['survived']
    
    # variables independientes
    X = dfCleanTitanic[['sex', 'age', 'fare', 'sibsp', 'parch']]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Entrenamiento: {X_train.shape[0]} pasajeros")
    print(f"Prueba:        {X_test.shape[0]} pasajeros")
    print(f"\nVariable dependiente: survived")
    print(f"Variables independientes: {X.columns.tolist()}")
    ```
    
    ![Screenshot 2026-04-26 at 12.54.59 p.m..png](Actividad%205/Screenshot_2026-04-26_at_12.54.59_p.m..png)
    
7. **Creación del modelo:** Utiliza las clases vistas en la explicación de los temas para que puedas crear tu modelo.
    
    ```python
    # creacion del modelo
    modelo = LogisticRegression(max_iter=1000, random_state=42)
    modelo.fit(X_train, y_train)
    
    y_pred = modelo.predict(X_test)
    
    print("Reporte de clasificación:")
    print(classification_report(y_test, y_pred,
          target_names=['No sobrevivió', 'Sobrevivió']))
    
    cm = confusion_matrix(y_test, y_pred)
    print("Matriz de confusión:")
    print(cm)
    ```
    
    ![Screenshot 2026-04-26 at 12.57.56 p.m..png](Actividad%205/Screenshot_2026-04-26_at_12.57.56_p.m..png)
    
8. **Estimación de los coeficientes y los odds ratio:** Una vez que entrenaste el modelo, el siguiente paso es interpretar los resultados. Esto se hace mediante la estimación de los coeficientes, los cuales te indicarán la fuerza y dirección de la relación entre cada variable independiente y la variable dependiente.
    
    ```python
    # ceficientes y los odds ratio
    coeficientes = pd.DataFrame({
        'variable':    X.columns,
        'coeficiente': modelo.coef_[0],
        'odds_ratio':  np.exp(modelo.coef_[0])
    }).sort_values('odds_ratio', ascending=False).reset_index(drop=True)
    
    print(coeficientes.to_string(index=False))
    
    print("\nInterpretación:")
    for _, row in coeficientes.iterrows():
        OR  = row['odds_ratio']
        var = row['variable']
        if OR > 1:
            print(f"  {var}: OR={OR:.3f} → aumenta probabilidad de sobrevivir")
        else:
            print(f"  {var}: OR={OR:.3f} → disminuye probabilidad de sobrevivir")
    ```
    
    Métricas del modelo logístico:
    
    - Precisión (accuracy): 80%, el modelo acierta 8 de cada 10 casos.
    - Odds Ratio de sex: ~4, ser mujer multiplica por 4 la probabilidad
    de sobrevivir respecto a un hombre.
    
    ![Screenshot 2026-04-26 at 12.59.07 p.m..png](Actividad%205/Screenshot_2026-04-26_at_12.59.07_p.m..png)
    
9. **Conclusión de tus resultados:** Formula una conclusión sobre tus hallazgos. Considera cuáles variables tienen mayor impacto en la probabilidad de sobrevivencia en el Titanic y la efectividad general de tu modelo para predecir la sobrevivencia. Reflexiona sobre posibles mejoras o ajustes para el modelo.
    
    El modelo de regresión logística presentó una precisión cercana al 80%, lo cual indica un buen desempeño para predecir la supervivencia de los pasajeros del Titanic. A partir de los resultados, se observa que la variable más influyente es el sexo, ya que las mujeres tenían una probabilidad significativamente mayor de sobrevivir. Asimismo, el fare también tiene un impacto importante, lo que sugiere que los pasajeros de clases más altas contaban con mayores ventajas. En cuanto a la edad, se identifica una ligera tendencia donde los pasajeros más jóvenes, especialmente niños, tenían mayor probabilidad de sobrevivir.
    

### Conclusión final

El modelo de regresión lineal obtuvo un R² de 0.58, lo que significa que logra explicar más o menos la mitad de la variación en el precio de los vehículos. No totalmente preciso, ya que hay otros factores que influyen en el precio y no se están considerando.
Por otro lado, el modelo de regresión logística alcanzó una precisión del 80% al predecir la sobrevivencia, lo cual indica un mejor desempeño en comparación con el modelo lineal.
En general, el modelo logístico resultó más efectivo en su tarea, mientras que el modelo lineal funciona, pero podría mejorar si se incluyen más variables.