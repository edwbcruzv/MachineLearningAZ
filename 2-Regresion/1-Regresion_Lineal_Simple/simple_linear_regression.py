# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:43:24 2022

@author: Muerto
"""
# Regresion lineal simple

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importando dataset

dataset = pd.read_csv('Salary_Data.csv')

X = dataset.iloc[:,:-1].values # tomamos todas las columnas, menos la ultima
Y = dataset.iloc[:,1].values# tomamos la ultima columna

# Dividir el dataset en conjunto de entrenamiento y conjunto de testing

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)

# Crear modelo de Regresion Lineal Simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()

regression.fit(X_train ,Y_train)
# Predecir el cunjunto de test
Y_pred = regression.predict(X_test)

# Visualizar los resultados de entrenamiento
plt.scatter(X_train,Y_train, color="red")
plt.plot(X_train,regression.predict(X_train),color="blue")
plt.title("sueldo vs Años de experiencia")
plt.ylabel("Sueldo ($)")
plt.xlabel("Anos de experiencia")
plt.show()

# Visualizar los resultados de test
plt.scatter(X_test,Y_test, color="red")
plt.plot(X_train,regression.predict(X_train),color="blue")
plt.title("sueldo vs Años de experiencia")
plt.ylabel("Sueldo ($)")
plt.xlabel("Anos de experiencia")
plt.show()

