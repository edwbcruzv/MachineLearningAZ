# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 18:47:04 2022

@author: Muerto
"""
# Plantilla de Pro-procesado - Datos Categoricos

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importando dataset

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:,:-1].values # tomamos todas las columnas, menos la ultima
Y = dataset.iloc[:,3].values# tomamos la ultima columna

# Dividir el dataset en conjunto de entrenamiento y conjunto de testing

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=10)

# Escalado de variables

from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)