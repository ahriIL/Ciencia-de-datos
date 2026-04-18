import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


url = "https://www.espn.com.mx/beisbol/mlb/estadisticas/jugador"
tablas = pd.read_html(url)

df = pd.concat([tablas[0], tablas[1]], axis=1)

print("Datos originales:")
print(df.head())

df.columns = df.columns.str.upper()
df = df.loc[:, ~df.columns.duplicated()]


df[["NOMBRE", "EQUIPO"]] = df["NOMBRE"].str.extract(r'(.+?)([A-Z]{2,3})$')


for col in df.columns:
    if col not in ["NOMBRE", "EQUIPO"]:
        df[col] = df[col].astype(str)
        df[col] = df[col].str.replace(",", "")
        df[col] = df[col].str.replace("%", "")
        df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["H", "R"])

print("\nDatos limpios:")
print(df.head())



# P1 Modelo y evaluación. 
# 1. Analisis exploratorio
correlacion = df[["H", "R"]].corr().iloc[0,1]
print("\nCorrelación:", correlacion)

print("\nCorrelación de Pearson:", correlacion)

if abs(correlacion) > 0.7:
    print("Relación fuerte")
elif abs(correlacion) > 0.4:
    print("Relación moderada")
else:
    print("Relación débil")

if correlacion > 0:
    print("Relación positiva")
else:
    print("Relación negativa")

#2. construccion de modelo
X = df[["H"]]
y = df["R"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("modelo", LinearRegression())
])

# 5. entrenamiento y prediccion
pipeline.fit(X_train, y_train)
print("\nModelo entrenado")


pred = pipeline.predict(X_test)

print("Predicciones realizadas:")
print(pred)


# 4. evaluacion
mae = mean_absolute_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))

print("\nMAE:", mae)
print("RMSE:", rmse)



# resultados
resultado = X_test.copy()
resultado["R_real"] = y_test.values
resultado["R_pred"] = pred
resultado["Error"] = abs(resultado["R_real"] - resultado["R_pred"])

print("\nResultados:")
print(resultado)

#top judaroes
top_jugadores = df.sort_values(by="R", ascending=False)

print("\nTop 10 jugadores:")
print(top_jugadores[["NOMBRE", "EQUIPO", "H", "R"]].head(10))


# -------------------------------
# 8. Conclusión
# -------------------------------
print("""
Conclusión:
Existe una relación positiva entre los bateos y las carreras.
El modelo permite estimar el rendimiento ofensivo de los jugadores,
aunque no es completamente preciso.
""")