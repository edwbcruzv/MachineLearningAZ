# -*- coding: utf-8 -*-
"""
Date: Wed Feb 22 00:08:15 2023

@author: edwin
"""
# =============================================================================
# Random Forest Regression
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


dataset = pd.read_csv('Position_Salaries.csv') # {buscar el dataset}

# Variable independiente:Mayuscula por ser una matriz.
#   tomamos [Todas las filas ,Solo la columna 1 (Leavel)]
X = dataset.iloc[:,1:2].values # {se pueden modificar segun se necesite}

# Variable dependiente:minuscula por ser un vector.
#   tomamos [Todas las filas: Solo la ultima columna]
y = dataset.iloc[:,2:3].values # {se pueden modificar segun se necesite}

# =============================================================================
# Ajustar la regresion con arboles aleatorios de decision con el dataset
# =============================================================================

from sklearn.ensemble import RandomForestRegressor 
rf_regression=RandomForestRegressor(n_estimators=100,random_state=0)
rf_regression.fit(X,y)

# ===== ========================================================================
# Prediccion de nuestros modelos (Resultados)
# =============================================================================
y_pred=rf_regression.predict([[6.5]])

# =============================================================================
# Visualizacion de los resultado: Random Forest
# =============================================================================

X_grid =np.arange(min(X),max(X),0.1)
X_grid=X_grid.reshape(len(X_grid),1)

plt.scatter(X,y,color='red')
plt.plot(X_grid,rf_regression.predict(X_grid),color='green')
# plt.plot(X,rf_regression.predict(X),color='green')
plt.title("Modelo Regresion por arboles aleatorios de decision")
plt.xlabel("Posicion del empleado")
plt.ylabel("Sueldo en $")
plt.show()
