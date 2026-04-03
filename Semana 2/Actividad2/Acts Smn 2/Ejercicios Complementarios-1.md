# Ejercicios Complementarios - Semana 2

## Temas Cubiertos
- **T3**: Arquitecturas de almacenamiento de datos
- **T4**: Bases de datos NoSQL
- **T5**: Operaciones CRUD con MongoDB

## Prerrequisitos Recomendados
- **Bases de datos**: Fundamentos de SQL, conceptos de tablas, filas y columnas
- **Programación**: Python básico, diccionarios y listas
- **Formatos**: Conceptos de JSON y estructuras de datos

---

## Ejercicios de Bases de Datos SQL

### Ejercicio 1: Consultas Básicas
Dada la siguiente tabla `empleados`:

| id | nombre     | departamento | salario |
| -- | ---------- | ------------ | ------- |
| 1  | Juan       | IT           | 50000   |
| 2  | María      | HR           | 45000   |
| 3  | Carlos     | IT           | 55000   |
| 4  | Ana        | Finanzas     | 48000   |
| 5  | Pedro      | Marketing    | 42000   |

Escribir consultas SQL para:
1. Seleccionar todos los empleados
2. Seleccionar nombres y salarios de empleados de IT
3. Encontrar el empleado con mayor salario
4. Contar empleados por departamento
5. Actualizar el salario de María a 50000

### Ejercicio 2: Joins
Dadas las tablas:

**empleados**
| id | nombre   | id_departamento |
| -- | -------- | ---------------- |
| 1  | Juan     | 1                |
| 2  | María    | 2                |
| 3  | Carlos   | 1                |

**departamentos**
| id | nombre      |
| -- | ----------- |
| 1  | IT          |
| 2  | HR          |
| 3  | Finanzas    |

Escribir consultas para:
1. INNER JOIN entre empleados y departamentos
2. LEFT JOIN mostrando todos los empleados
3. Contar empleados por departamento

---

## Ejercicios de JSON y Estructuras de Datos

### Ejercicio 3: Manipulación de JSON
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

1. Extraer los nombres de todos los empleados
2. Agregar una nueva habilidad a Juan
3. Crear un nuevo empleado con id: 4
4. Eliminar las habilidades de María

### Ejercicio 4: Estructuras de Datos en Python
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

---

## Ejercicios de MongoDB

### Ejercicio 5: Operaciones CRUD
Utilizando la colección `productos`:

```javascript
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

### Ejercicio 6: Consultas Avanzadas en MongoDB
```javascript
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

---

## Ejercicios de Investigación

### Ejercicio 7: Tipos de Bases de Datos NoSQL
Investigar y explicar:
1. **Documentales**: MongoDB, CouchDB
2. **Key-Value**: Redis, DynamoDB
3. **Columnar**: Cassandra, HBase
4. **Graph**: Neo4j

**Investigar:**
- ¿Cuándo usar cada tipo?
- ¿Cuáles son sus ventajas y desventajas?

### Ejercicio 8: Arquitecturas de Almacenamiento
Investigar:
1. ¿Qué es Data Lake?
2. ¿Qué es Data Warehouse?
3. Diferencias entre OLAP y OLTP
4. ¿Qué es ETL?

---

## Recursos Adicionales

### Tutoriales
- MongoDB University (cursos gratuitos)
- SQLZoo - Ejercicios interactivos de SQL
- W3Schools - Tutorial de JSON

### Práctica Recomendada
- Completar los ejercicios de SQL en Hackerrank
- Practicar MongoDB en MongoDB Atlas playground

---

## Próxima Semana
En la Semana 3 cubriremos:
- **T6**: Python para ciencia de datos
- **T7**: El proceso de ciencia de datos
- **T8**: Análisis exploratorio de datos en Python

**Prerrequisitos para próxima semana:**
- Python básico (variables, funciones, loops)
- NumPy, Pandas, Matplotlib
- Medidas de tendencia central
