#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 22:14:49 2024

@author: cruz
"""

# =============================================================================
# Random Selection
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
# =============================================================================
# cargando el dataset
# =============================================================================

# Descripcion: tenemos 10 versiones de un mismo anuncio de publicidad y no se 
# deciden por cual es el mejor, tenemos el testeo junto el numero de 
# clicks que le dio el publico.
# Objetivo: buscamos cual es el mejor anuncio.

dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

# =============================================================================
# Implementacion del random selection
# =============================================================================

N = 10000
d = 10

ads_selected = []
total_reward = 0

for n in range(0,N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    total_reward = total_reward+reward
    
plt.hist(ads_selected)
plt.title("histograma de anuncios")
plt.xlabel("Anuncio")
plt.ylabel("Numero de veces que se a visualizado")
plt.show()
    