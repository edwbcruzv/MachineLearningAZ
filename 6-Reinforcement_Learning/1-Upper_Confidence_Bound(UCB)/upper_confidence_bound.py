#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:34:20 2024

@author: cruz
"""

# =============================================================================
# Upper Confidence Bound (UCB)
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# =============================================================================
# cargando el dataset
# =============================================================================

# Descripcion: tenemos 10 versiones de un mismo anuncio de publicidad y no se 
# deciden por cual es el mejor, tenemos el testeo junto el numero de 
# clicks que le dio el publico.
# Objetivo: buscamos cual es el mejor anuncio.

dataset = pd.read_csv("Ads_CTR_Optimisation.csv")
