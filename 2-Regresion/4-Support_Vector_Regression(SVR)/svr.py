# -*- coding: utf-8 -*-
"""
Date: Sat Feb 18 22:00:36 2023

@author: edwin
"""
# =============================================================================
# Support Vectorial Regression
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
# --------------------Escalado de variables--------------------
# =============================================================================

from sklearn.preprocessing import StandardScaler

# Escalador para las variables
sc_X = StandardScaler()
sc_y = StandardScaler()

X= sc_X.fit_transform(X)
y= sc_y.fit_transform(y)
# =============================================================================
# --------------------Ajustar la SVR con el dataset--------------------
# =============================================================================

from sklearn.svm import SVR

svr_regression=SVR(kernel='rbf')
svr_regression.fit(X,y)


# =============================================================================
# --------------Visualizacion de los resultado del modelo--------------
# =============================================================================
plt.scatter(X,y,color='red')
plt.plot(X,svr_regression.predict(X),color='green')
plt.title("Modelo Regresion SVR")
plt.xlabel("Posicion del empleado")
plt.ylabel("Sueldo en $")
plt.show()

# =============================================================================
# -----------------Prediccion de nuestros modelos-----------------
# =============================================================================
y_pred_sc=svr_regression.predict(sc_X.transform([[6.5]]))
y_pred=sc_y.inverse_transform([y_pred_sc])
print(y_pred)
