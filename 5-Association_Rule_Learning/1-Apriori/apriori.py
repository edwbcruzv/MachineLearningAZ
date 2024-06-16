#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:35:06 2023

@author: cruz
"""

# =============================================================================
# Apriori
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# =============================================================================
# --------------------Importando dataset--------------------
# =============================================================================

# Cada una de las filas es lo que un usuario compro en un supermercado en francia.
# Objetivo: ver que reglas de asociacion existen para brindarselas al gerente
# de un supermercado para que realice el acomododo en el supermecado y asi
# la gente al comprar un producto lleve el otro y a la vez incrementar las ventas.
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header= None)

# No se hace ninguna distincion entre variables independientes 
# y variables dependientes en R
# =============================================================================
# --------------------Lista de listas--------------------
# =============================================================================

transactions = []  
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

# =============================================================================
# --------------------Enternamiendo del arlgoritmo Apriori--------------------
# =============================================================================
# Utilizaremos una libreria externa, ya que no hay para instalar
from Apriori_Python.Apyori import apriori

# PASO 1: Decidir un soporte y nivel de confianza minimo.

# 3: una media de un producto que se vende 3 veces al dia
# 7: dias de la semana
# 7500: total de los productos
# 3*7/7500 = 0.0028, decidimos redondearlo a 0.003
# para la confianza R recomienda un 0.4
rules = apriori(transactions, min_support = 0.003, min_confidense = 0.2, nim_lift = 3, max_length = 2 )
# =============================================================================
# --------------------Visualizacion--------------------
# ============================================================================= 
result = list(rules)
result[1]
 # PASO 2: Elegir todos los subconjuntos de transacciones con soporte superior al minimo elegido.
# PASO 3: Elegir todas las reglas de estos subconjuntos con nivel de confianza superior al minimo elegido.


# PASO 4: Ordenar todas las reglas anteriores por lift descendiente.










