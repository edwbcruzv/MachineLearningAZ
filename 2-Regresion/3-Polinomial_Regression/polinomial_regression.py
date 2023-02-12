# =============================================================================
# Regresion Lineal Polinomica
# =============================================================================
# =============================================================================
# --------------------Importando librerias--------------------
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# =============================================================================
# --------------------Importando dataset--------------------
# =============================================================================

# Estructura de los datos:tipos de empleados y el nivel 
# de cada tipo de empleado y el salario correspondiente.
# Objetivo: asignar un salario correspondientes a un nivel y su posicion dada.
# Filas :10
# Columnas:
#           |Position|Level| (vars independiente)
#           |salary| (var_dependiente)

dataset = pd.read_csv('Position_Salaries.csv')

# Variable independiente:Mayuscula por ser una matriz.
#   tomamos [Todas las filas ,Solo la columna 1 (Leavel)]
X = dataset.iloc[:,1:2].values

# Variable dependiente:minuscula por ser un vector.
#   tomamos [Todas las filas: Solo la ultima columna]
y = dataset.iloc[:,2:3].values

# =============================================================================
# --------------------Dividiendo dataset en conjuntos--------------------
# --------------------de entrenamiento y conjunto de testings-------------
# =============================================================================

# No es recomendable dividir los datos, al ser pocos a simple vista necesita
# toda la informacion.

# =============================================================================
# Ajustar la regresion lineal con el dataset
# =============================================================================
from sklearn.linear_model import LinearRegression
linear_regression = LinearRegression()
linear_regression.fit(X,y)

# =============================================================================
# Ajustar la regresion polinomica con el dataset
# =============================================================================

from sklearn.preprocessing import PolynomialFeatures
poly_regression=PolynomialFeatures(degree=4) # se puede jugar con el grado
X_poly=poly_regression.fit_transform(X)

linear_regression_2=LinearRegression()
linear_regression_2.fit(X_poly,y)

# =============================================================================
# Visualizacion de los resultado: Modelo Lineal
# =============================================================================
plt.scatter(X,y,color='red')
plt.plot(X,linear_regression.predict(X),color='blue')
plt.title("Modelo Regresion Lineal")
plt.xlabel("Posicion del empleado")
plt.ylabel("Sueldo en $")
plt.show()
# =============================================================================
# Visualizacion de los resultado: Modelo Polinomico
# =============================================================================
plt.scatter(X,y,color='red')
plt.plot(X,linear_regression_2.predict(X_poly),color='green')
plt.title("Modelo Regresion Polinomica")
plt.xlabel("Posicion del empleado")
plt.ylabel("Sueldo en $")
plt.show()
# =============================================================================
# Prediccion de nuestros modelos (Resultados)
# =============================================================================

linear_regression.predict([[6.5]])
linear_regression_2.predict(poly_regression.fit_transform([[6.5]]))















