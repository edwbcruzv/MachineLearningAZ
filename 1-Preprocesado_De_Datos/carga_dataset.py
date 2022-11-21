# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:13:26 2022

@author: Muerto
"""

# Plantilla de Pro-procesado

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importando dataset

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:,:-1].values # tomamos todas las columnas, menos la ultima
Y = dataset.iloc[:,3].values# tomamos la ultima columna

# Tratamiendo de NAs

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X[:,1:3]) # aplicarlo a las columnas 1 y 2 
X[:,1:3] = imputer.transform(X[:,1:3])


# Codificar datos categoricos

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

le_X =LabelEncoder()
X[:,0]=le_X.fit_transform(X[:,0])

ct = ColumnTransformer(
    [('one_hot_encoder',OneHotEncoder(categories='auto'),[0])],
    remainder='passthrough')
# se creara una columna por cada pais (categorizando)
# y con un booleano se sabra el pais correspondiente (onehotencoder)
X = np.array(ct.fit_transform(X),dtype=float)

# columna de si o no usando booleanos
le_Y=LabelEncoder()
Y=le_Y.fit_transform(Y)

# Dividir el dataset en conjunto de entrenamiento y conjunto de testing

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=10)

# Escalado de variables

from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)



