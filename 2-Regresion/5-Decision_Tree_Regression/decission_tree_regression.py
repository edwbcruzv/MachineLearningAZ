# -*- coding: utf-8 -*-
"""
Date: Tue Feb 21 17:46:38 2023

@author: edwin
"""

# =============================================================================
# Decission Tree Regression
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
# Ajustar la regresion con arboles de decision con el dataset
# =============================================================================

from sklearn.tree import DecisionTreeRegressor
tree_regression=DecisionTreeRegressor(random_state=0)
tree_regression.fit(X,y)

# ===== ========================================================================
# Prediccion de nuestros modelos (Resultados)
# =============================================================================
y_pred=tree_regression.predict([[6.5]])

# =============================================================================
# Visualizacion de los resultado: arboles de decision
# =============================================================================

X_grid =np.arange(min(X),max(X),0.1)
X_grid=X_grid.reshape(len(X_grid),1)

plt.scatter(X,y,color='red')
# plt.plot(X_grid,tree_regression.predict(X_grid),color='green')
plt.plot(X,tree_regression.predict(X),color='green')
plt.title("Modelo Regresion por arboles de decision")
plt.xlabel("Posicion del empleado")
plt.ylabel("Sueldo en $")
plt.show()