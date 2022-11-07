# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 18:48:48 2022

@author: Muerto
"""

# Plantilla de Pro-procesado - Datos Faltantes o NAs

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