# Semana 2 Consolidado

---

# Actividad 2

1. **Lee los temas 5, 6, 7 y 8.**
2. **Accede a tu entorno de desarrollo de código.**
3. **Definición del problema y recopilación de datos**
    - Redacta el objetivo del proyecto y las preguntas clave que se buscan responder.
    
    **Descripción del problema**
    
    ---
    
    El objetivo del proyecto es realizar un análisis exploratorio de los datos de ventas de la tienda en línea *“Todo ventas en Línea, S.A. de C.V.”*, con el fin de identificar patrones de compra, productos más vendidos, comportamiento de los clientes y tendencias estacionales. Esto permitirá generar información útil para la toma de decisiones estratégicas, optimizar las ventas y definir acciones comerciales durante el año.
    
    **Preguntas clave**
    
    ---
    
    - ¿Cuáles son los productos más vendidos?
    - ¿Qué categorías generan mayores ingresos?
    - ¿En qué periodos del año se registran más ventas?
    - ¿Qué tipo de clientes compran más (segmentación)?
    - ¿Cuál es el ticket promedio por compra?
    - ¿Existen productos con baja rotación que deban eliminarse o promocionarse?
    - ¿Qué tendencias o patrones se pueden identificar en el comportamiento de compra?
    
4. **Utiliza Python para generar, de manera aleatoria, los conjuntos de datos necesarios** para el ejercicio propuesto. Los conjuntos de datos deben cumplir con los siguientes requisitos:
    - Incluir al menos 10 columnas: cuatro de tipo numérico (entero o decimal), dos de tipo categórico (texto breve que representa una categoría), dos de tipo estructurado (datos con una organización predefinida) y dos de tipo no estructurado (texto libre, etc.).
    - Contener al menos 5,000 registros.
    
    ```python
    import pandas as pd
    import numpy as np
    import random
    import string
    from datetime import datetime, timedelta
    n = 5000
    
    def texto_aleatorio():
        palabras = ["excelente", "malo", "rápido", "lento", "calidad", "precio", "recomendado", "defectuoso"]
        return " ".join(random.choices(palabras, k=random.randint(5, 15)))
    
    def direccion():
        return {
            "calle": random.choice(["Av. Central", "Calle Norte", "Boulevard Sur"]),
            "ciudad": random.choice(["CDMX", "Querétaro", "Monterrey"]),
            "codigo_postal": random.randint(10000, 99999)
        }
    
    def detalles_pedido():
        return {
            "metodo_pago": random.choice(["Tarjeta", "PayPal", "Transferencia"]),
            "envio": random.choice(["Express", "Estándar"])
        }
    
    data = {
        # numéricos
        "precio": np.round(np.random.uniform(50, 2000, n), 2),
        "cantidad": np.random.randint(1, 10, n),
        "descuento": np.round(np.random.uniform(0, 0.3, n), 2),
        "total_venta": np.round(np.random.uniform(100, 5000, n), 2),
    
        # categoriua
        "categoria_producto": np.random.choice(["Electrónica", "Ropa", "Hogar", "Deportes"], n),
        "metodo_envio": np.random.choice(["Estándar", "Express"], n),
    
        # estructurados
        "direccion_cliente": [direccion() for _ in range(n)],
        "detalle_pedido": [detalles_pedido() for _ in range(n)],
    
        # no estructurados
        "comentarios_cliente": [texto_aleatorio() for _ in range(n)],
        "descripcion_producto": [texto_aleatorio() for _ in range(n)]
    }
    
    df = pd.DataFrame(data)
    
    df.to_csv("datos_ventas.csv", index=False)
    
    print("Dataset generado con éxito")
    print(df.head())
    ```
    
5. **Preparación de los datos:**
    - Carga los datos a MongoDB.
    
    ```python
    from pymongo import MongoClient
    import pandas as pd
    
    df = pd.read_csv("datos_ventas.csv")
    
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["actividad2"]
    coleccion = db["ventas"]
    
    datos = df.to_dict(orient="records")
    coleccion.insert_many(datos)
    
    print("Datos insertados correctamente")
    
    datos_mongo = list(coleccion.find())
    df_mongo = pd.DataFrame(datos_mongo)
    
    df_mongo.info()
    df_mongo.head()
    df_mongo.describe()
    ```
    
    - Realiza una exploración inicial de los datos para comprender su estructura y calidad. Esta fase es crucial para identificar posibles problemas de calidad de datos, como valores faltantes o atípicos, y para entender la distribución y relaciones entre las variables.
    
    ```python
    print("=== 1. ESTRUCTURA DE LOS DATOS ===")
    print(df_mongo.info())
    
    print("\n=== 2. CALIDAD DE DATOS: VALORES FALTANTES ===")
    nulos = df_mongo.isnull().sum()
    if nulos.sum() == 0:
        print("Calidad confirmada: No existen valores faltantes en ninguna columna.")
    else:
        print("Alerta de calidad. Valores nulos encontrados:")
        print(nulos[nulos > 0])
    
    print("\n=== 3. CALIDAD DE DATOS: VALORES ATÍPICOS (OUTLIERS) ===")
    cols_num = ['precio', 'cantidad', 'descuento', 'total_venta']
    for col in cols_num:
        Q1 = df_mongo[col].quantile(0.25)
        Q3 = df_mongo[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        
        atipicos = df_mongo[(df_mongo[col] < limite_inferior) | (df_mongo[col] > limite_superior)]
        print(f"- En '{col}' se detectaron {len(atipicos)} valores atípicos.")
    
    print("\n=== 4. DISTRIBUCIÓN DE LAS VARIABLES ===")
    print(df_mongo[cols_num].describe())
    
    print("\n=== 5. RELACIONES ENTRE VARIABLES ===")
    print(df_mongo[cols_num].corr())
    ```
    
    Esto nos da un resultado como el siguiente:
    
    ```
    === 1. ESTRUCTURA DE LOS DATOS ===
    <class 'pandas.DataFrame'>
    RangeIndex: 5000 entries, 0 to 4999
    Data columns (total 11 columns):
     #   Column                Non-Null Count  Dtype  
    ---  ------                --------------  -----  
     0   _id                   5000 non-null   object 
     1   precio                5000 non-null   float64
     2   cantidad              5000 non-null   int64  
     3   descuento             5000 non-null   float64
     4   total_venta           5000 non-null   float64
     5   categoria_producto    5000 non-null   str    
     6   metodo_envio          5000 non-null   str    
     7   direccion_cliente     5000 non-null   str    
     8   detalle_pedido        5000 non-null   str    
     9   comentarios_cliente   5000 non-null   str    
     10  descripcion_producto  5000 non-null   str    
    dtypes: float64(3), int64(1), object(1), str(6)
    memory usage: 429.8+ KB
    None
    
    === 2. CALIDAD DE DATOS: VALORES FALTANTES ===
    Calidad confirmada: No existen valores faltantes en ninguna columna.
    
    === 3. CALIDAD DE DATOS: VALORES ATÍPICOS (OUTLIERS) ===
    ...
    precio       1.000000  0.008693   0.018659     0.024385
    cantidad     0.008693  1.000000  -0.023592     0.007409
    descuento    0.018659 -0.023592   1.000000    -0.021781
    total_venta  0.024385  0.007409  -0.021781     1.000000
    ```
    
6. **Análisis exploratorio de datos:**
    - Utiliza Pandas y NumPy para realizar análisis numérico y manipulación de datos.
    - Explora la distribución de datos numéricos y categóricos mediante el uso de estadísticas descriptivas como media, mediana, moda, solamente.
    - Crea un resumen estadístico utilizando un DataFrame de Python y sus librerías requeridas, como lo son NumPy y Pandas.
    - Realiza la interpretación del análisis exploratorio.
        
        ```python
        import pandas as pd
        import numpy as np
        
        cols_numericas = ['precio', 'cantidad', 'descuento', 'total_venta']
        
        resumen_dict = {
            "Métrica": ["Media", "Mediana", "Moda"]
        }
        
        for col in cols_numericas:
            media = np.mean(df_mongo[col])
            mediana = np.median(df_mongo[col])
            moda = df_mongo[col].mode()[0] 
            
            resumen_dict[col] = [media, mediana, moda]
        
        df_resumen = pd.DataFrame(resumen_dict)
        
        print("=== RESUMEN ESTADÍSTICO DE VARIABLES NUMÉRICAS ===")
        print(df_resumen)
        
        print("\n=== DISTRIBUCIÓN DE VARIABLES CATEGÓRICAS ===")
        for col in ['categoria_producto', 'metodo_envio']:
            print(f"\nConteo para {col}:")
            print(df_mongo[col].value_counts())
            print(f"Moda (Categoría más frecuente): {df_mongo[col].mode()[0]}")
        ```
        
        Nos da un resultado como el siguiente:
        
        ```
        === RESUMEN ESTADÍSTICO DE VARIABLES NUMÉRICAS ===
           Métrica      precio  cantidad  descuento  total_venta
        0    Media  1019.39514    5.0676   0.150624   2532.80442
        1  Mediana  1029.29000    5.0000   0.150000   2510.63000
        2     Moda  1558.07000    7.0000   0.070000    131.75000
        
        === DISTRIBUCIÓN DE VARIABLES CATEGÓRICAS ===
        
        Conteo para categoria_producto:
        categoria_producto
        Hogar          1327
        Electrónica    1256
        Ropa           1226
        Deportes       1191
        Name: count, dtype: int64
        Moda (Categoría más frecuente): Hogar
        
        Conteo para metodo_envio:
        metodo_envio
        Estándar    2510
        Express     2490
        Name: count, dtype: int64
        Moda (Categoría más frecuente): Estándar
        ```
        
7. **Creación de gráficas para visualización de datos:**
    - Genera una visualización a través de un diagrama de cajas utilizando Python y las bibliotecas adecuadas.
    - Crea una gráfica de dispersión para representar la relación entre variables.
    - Crea un histograma para mostrar la distribución de datos.
    - Realiza la interpretación de las gráficas creadas.
    
    ```python
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    # estilo
    sns.set_theme(style="whitegrid")
    paleta = sns.color_palette("viridis")
    
    # cajas
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='categoria_producto', y='precio', data=df_mongo, palette="Set3")
    plt.title('Distribución de Precios por Categoría de Producto', fontsize=14)
    plt.xlabel('Categoría de Producto', fontsize=12)
    plt.ylabel('Precio ($)', fontsize=12)
    plt.xticks(rotation=45) 
    plt.show()
    
    # dipsecion 
    plt.figure(figsize=(10, 6))
    
    sns.scatterplot(x='cantidad', y='total_venta', data=df_mongo, color=paleta[2], alpha=0.5)
    plt.title('Relación entre Cantidad Comprada y Total de Venta', fontsize=14)
    plt.xlabel('Cantidad de Artículos', fontsize=12)
    plt.ylabel('Total de Venta ($)', fontsize=12)
    plt.show()
    
    # histograma
    plt.figure(figsize=(10, 6))
    
    sns.histplot(df_mongo['total_venta'], kde=True, color=paleta[0], bins=30)
    plt.title('Distribución de Frecuencia del Total de Ventas', fontsize=14)
    plt.xlabel('Total de Venta ($)', fontsize=12)
    plt.ylabel('Frecuencia (Número de Registros)', fontsize=12)
    plt.show()
    ```
    
    ![image.png](Semana%202%20Consolidado/image.png)
    
    ![image.png](Semana%202%20Consolidado/image%201.png)
    
    ![image.png](Semana%202%20Consolidado/image%202.png)
    

---

# Ejercicios Complementarios - Semana 2

## **Ejercicio 1: Consultas Básicas**

Dada la siguiente tabla `empleados`:

| id | nombre | departamento | salario |
| --- | --- | --- | --- |
| 1 | Juan | IT | 50000 |
| 2 | María | HR | 45000 |
| 3 | Carlos | IT | 55000 |
| 4 | Ana | Finanzas | 48000 |
| 5 | Pedro | Marketing | 42000 |

Escribir consultas SQL para:

1. Seleccionar todos los empleados
    
    ```sql
    SELECT * FROM empleados;
    ```
    
2. Seleccionar nombres y salarios de empleados de IT
    
    ```sql
    SELECT nombre, salario FROM empleados WHERE departamento = 'IT';
    ```
    
3. Encontrar el empleado con mayor salario
    
    ```sql
    SELECT * FROM empleados ORDER BY salario DESC LIMIT 1;
    ```
    
4. Contar empleados por departamento
    
    ```sql
    SELECT departamento, COUNT(*) FROM empleados GROUP BY departamento;
    ```
    
5. Actualizar el salario de María a 50000
    
    ```sql
    UPDATE empleados SET salario = 50000 WHERE nombre = 'María';
    ```
    

## Ejercicio 2: Joins

Dadas las tablas:

**empleados**

| id | nombre | id_departamento |
| --- | --- | --- |
| 1 | Juan | 1 |
| 2 | María | 2 |
| 3 | Carlos | 1 |

**departamentos**

| id | nombre |
| --- | --- |
| 1 | IT |
| 2 | HR |
| 3 | Finanzas |

Escribir consultas para:

1. INNER JOIN entre empleados y departamentos
    
    ```sql
    SELECT e.nombre, d.nombre AS departamento
    FROM empleados e
    INNER JOIN departamentos d
    ON e.id_departamento = d.id;
    ```
    
2. LEFT JOIN mostrando todos los empleados
    
    ```sql
    SELECT e.nombre, d.nombre AS departamento
    FROM empleados e
    LEFT JOIN departamentos d
    ON e.id_departamento = d.id;
    ```
    
3. Contar empleados por departamento
    
    ```sql
    SELECT d.nombre AS departamento, COUNT(e.id) AS total_empleados
    FROM departamentos d
    LEFT JOIN empleados e
    ON e.id_departamento = d.id
    GROUP BY d.nombre;
    ```
    

## **Ejercicios de JSON y Estructuras de Datos**

---

### **Ejercicio 3: Manipulación de JSON**

Dado el siguiente JSON:

```json
{
  "empleados": [
    {"id": 1, "nombre": "Juan", "habilidades": ["Python", "SQL"]},
    {"id": 2, "nombre": "María", "habilidades": ["Java", "MongoDB"]},
    {"id": 3, "nombre": "Carlos", "habilidades": ["Python", "R"]}
  ]
}
```

![Screenshot 2026-04-03 at 3.52.41 p.m..png](Semana%202%20Consolidado/Screenshot_2026-04-03_at_3.52.41_p.m..png)

1. Extraer los nombres de todos los empleados
    
    ```bash
    db.ejercicioSmn2.find({}, { "empleados.nombre": 1, _id: 0 })
    ```
    
    ![Screenshot 2026-04-03 at 3.53.23 p.m..png](Semana%202%20Consolidado/Screenshot_2026-04-03_at_3.53.23_p.m..png)
    
2. Agregar una nueva habilidad a Juan
    
    ```bash
    db.ejercicioSmn2.updateOne(
      { "empleados.nombre": "Juan" },
      { $push: { "empleados.$.habilidades": "C++" } }
    )
    ```
    
    ![Screenshot 2026-04-03 at 3.54.08 p.m..png](Semana%202%20Consolidado/Screenshot_2026-04-03_at_3.54.08_p.m..png)
    
3. Crear un nuevo empleado con id: 4
    
    ```bash
    db.ejercicioSmn2.updateOne(
      {},
      {
        $push: {
          empleados: {
            id: 4,
            nombre: "Ana",
            habilidades: ["JavaScript"]
          }
        }
      }
    )
    ```
    
    ![Screenshot 2026-04-03 at 3.54.32 p.m..png](Semana%202%20Consolidado/Screenshot_2026-04-03_at_3.54.32_p.m..png)
    
4. Eliminar las habilidades de María
    
    ```bash
    db.ejercicioSmn2.updateOne(
      { "empleados.nombre": "María" },
      { $set: { "empleados.$.habilidades": [] } }
    )
    ```
    
    ![Screenshot 2026-04-03 at 3.54.52 p.m..png](Semana%202%20Consolidado/Screenshot_2026-04-03_at_3.54.52_p.m..png)
    

### **Ejercicio 4: Estructuras de Datos en Python**

Implementar las siguientes estructuras:

```python
# Lista de diccionarios (simulando una tabla)
empleados = [
    {"id": 1, "nombre": "Juan", "salario": 50000},
    {"id": 2, "nombre": "María", "salario": 45000},
    {"id": 3, "nombre": "Carlos", "salario": 55000}
]

# Ejercicios:
# 1. Agregar un nuevo empleado
# 2. Buscar empleado por id
# 3. Calcular promedio de salarios
# 4. Filtrar empleados con salario > 50000
# 5. Actualizar el nombre del empleado con id=2
```

Mi cdigo

```bash
empleados = [
    {"id": 1, "nombre": "Juan", "salario": 50000},
    {"id": 2, "nombre": "María", "salario": 45000},
    {"id": 3, "nombre": "Carlos", "salario": 55000}
]

# 1. Agregar un nuevo empleado
nuevo_empleado = {"id": 4, "nombre": "Ana", "salario": 60000}
empleados.append(nuevo_empleado)

# 2. Buscar empleado por id
def buscar_empleado(id_buscar):
    for emp in empleados:
        if emp["id"] == id_buscar:
            return emp
    return None

print("Empleado con id=2:", buscar_empleado(2))

# 3. Calcular promedio de salarios
total = sum(emp["salario"] for emp in empleados)
promedio = total / len(empleados)
print("Promedio de salarios:", promedio)

# 4. Filtrar empleados con salario > 50000
filtrados = [emp for emp in empleados if emp["salario"] > 50000]
print("Empleados con salario > 50000:", filtrados)

# 5. Actualizar el nombre del empleado con id=2
for emp in empleados:
    if emp["id"] == 2:
        emp["nombre"] = "Maria Actualizada"

print("Lista final:", empleados)
```

## **Ejercicios de MongoDB**

### **Ejercicio 5: Operaciones CRUD**

Utilizando la colección `productos`:

```jsx
// Insertar documentos
db.productos.insertMany([
    {"nombre": "Laptop", "precio": 999, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 29, "categoria": "Electrónica"},
    {"nombre": "Escritorio", "precio": 299, "categoria": "Muebles"}
])

// Realizar las siguientes operaciones:
# 1. Read: Encontrar todos los productos de Electrónica
# 2. Read: Encontrar productos con precio < 100
# 3. Update: Aumentar precio de Laptop en 10%
# 4. Delete: Eliminar productos con precio < 50
# 5. Create: Agregar un nuevo producto
```

![Screenshot 2026-04-03 at 3.50.20 p.m..png](Semana%202%20Consolidado/Screenshot_2026-04-03_at_3.50.20_p.m..png)

1. Read: Encontrar todos los productos de Electrónica
    
    ```bash
    db.productos.find({ "categoria": "Electrónica" })
    ```
    
    ![Screenshot 2026-04-03 at 3.51.25 p.m..png](Semana%202%20Consolidado/Screenshot_2026-04-03_at_3.51.25_p.m..png)
    
2. Read: Encontrar productos con precio < 100
    
    ```bash
    db.productos.find({"precio": {$lt: 100} })
    ```
    
    ![Screenshot 2026-04-03 at 3.56.59 p.m..png](Semana%202%20Consolidado/Screenshot_2026-04-03_at_3.56.59_p.m..png)
    
3. Update: Aumentar precio de Laptop en 10%
    
    ```bash
    db.productos.updateOne(
        { "nombre": "Laptop" },
        { $mul: { "precio": 1.1 } }
    )
    ```
    
    ![Screenshot 2026-04-03 at 3.59.55 p.m..png](Semana%202%20Consolidado/Screenshot_2026-04-03_at_3.59.55_p.m..png)
    
4. Delete: Eliminar productos con precio < 50
    
    ```bash
    db.productos.deleteMany({ "precio": { $lt: 50 } })
    ```
    
    ![Screenshot 2026-04-03 at 4.03.53 p.m..png](Semana%202%20Consolidado/Screenshot_2026-04-03_at_4.03.53_p.m..png)
    
5. Create: Agregar un nuevo producto
    
    ```bash
    db.productos.insertOne({
        "nombre": "Silla Gamer",
        "precio": 150,
        "categoria": "Muebles"
    })
    ```
    
    ![Screenshot 2026-04-03 at 4.06.16 p.m..png](Semana%202%20Consolidado/Screenshot_2026-04-03_at_4.06.16_p.m..png)
    

### **Ejercicio 6: Consultas Avanzadas en MongoDB**

```jsx
// Colección: estudiantes
{"nombre": "Ana", "materias": ["Math", "Physics"], "edad": 20}
{"nombre": "Luis", "materias": ["Math", "Chemistry"], "edad": 22}
{"nombre": "Sofia", "materias": ["Biology"], "edad": 19}

# Consultas:
# 1. Encontrar estudiantes que cursan Math
# 2. Encontrar estudiantes mayores de 20
# 3. Contar estudiantes por edad
# 4. Proyectar solo nombres
```

1. Encontrar estudiante que cursan Math
    
    ```bash
    db.estudiantes.find({ "materias": "Math" })
    ```
    
2. Encontrar estudiantes mayores de 20
    
    ```bash
    db.estudiantes.find({ "edad": { $gt: 20 } })
    ```
    
3. Contar estudiantes por edad
    
    ```bash
    db.estudiantes.aggregate([
        {
            $group: {
                _id: "$edad",
                totalEstudiantes: { $sum: 1 }
            }
        }
    ])
    ```
    
4. Proyectar solo nombres
    
    ```bash
    db.estudiantes.find({}, { "nombre": 1, "_id": 0 })
    ```
    

---

## **Ejercicios de Investigación**

### **Ejercicio 7: Tipos de Bases de Datos NoSQL**

Investigar y explicar:

1. **Documentales**: MongoDB, CouchDB
    
    **¿Qué son?**
    
    Guardan datos en documentos tipo JSON (flexibles, sin esquema rígido).
    
    **¿Cuándo usar?**
    
    - Cuando los datos cambian mucho (apps modernas, perfiles, catálogos)
    - APIs, apps web, sistemas con datos semi-estructurados
    
    **Ventajas**
    
    - Flexibilidad (no necesitas esquema fijo)
    - Fácil de escalar
    - Muy usadas → buena documentación
    
    **Desventajas**
    
    - Menos eficientes para relaciones complejas
    - Puede volverse desordenado si no diseñas bien
2. **Key-Value**: Redis, DynamoDB
    
    **¿Qué son?**
    
    Almacenan datos como dato valor
    
    **¿Cuándo usar?**
    
    - Caché
    - Sesiones de usuario
    - Datos simples y rápidos
    
    **Ventajas**
    
    - Extremadamente rápidas
    - Simples
    - Escalan fácil
    
    **Desventajas**
    
    - No sirven para consultas complejas
    - Estructura muy limitada
3. **Columnar**: Cassandra, HBase
    
    **¿Qué son?**
    
    Guardan datos por columnas en lugar de filas.
    
    **¿Cuándo usar?**
    
    - Big Data
    - Análisis de grandes volúmenes
    - Sistemas distribuidos
    
    **Ventajas**
    
    - Muy eficientes para grandes datos
    - Escalabilidad horizontal
    - Alto rendimiento en lecturas específicas
    
    **Desventajas**
    
    - Complejas de usar
    - No son intuitivas
    - No ideales para aplicaciones simples
4. **Graph**: Neo4j
    
    **¿Qué son?**
    
    Trabajan con nodos y relaciones.
    
    **¿Cuándo usar?**
    
    - Redes sociales
    - Recomendaciones (tipo Netflix)
    - Relaciones complejas
    
    **Ventajas**
    
    - Perfectas para relaciones
    - Consultas rápidas en conexiones
    
    **Desventajas**
    
    - No sirven para datos tabulares simples
    - Curva de aprendizaje

**Investigar:**

- ¿Cuándo usar cada tipo?
- ¿Cuáles son sus ventajas y desventajas?

---

### **Ejercicio 8: Arquitecturas de Almacenamiento**

Investigar:

1. ¿Qué es Data Lake?
    
    Es un sistema que almacena datos en bruto, sin procesar y en cualquier formato (como JSON, CSV, imágenes, etc.). Sirve para guardar grandes volúmenes de información que después pueden analizarse.
    
2. ¿Qué es Data Warehouse?
    
    Es una base de datos que almacena información ya procesada y organizada. Está diseñada para hacer análisis y generar reportes de forma eficiente.
    
3. Diferencias entre OLAP y OLTP
    - **OLTP**: Se usa para operaciones diarias en tiempo real (como compras o registros). Maneja muchas transacciones pequeñas.
    - **OLAP**: Se usa para análisis de datos históricos. Realiza consultas complejas para obtener insights.
4. ¿Qué es ETL?
    
    Es un proceso que permite mover y preparar datos:
    
    - **Extract (Extraer)**: Obtener datos de diferentes fuentes
    - **Transform (Transformar)**: Limpiar y organizar los datos
    - **Load (Cargar)**: Guardarlos en un sistema como un Data Warehouse

---