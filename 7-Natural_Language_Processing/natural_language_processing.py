#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 22:50:38 2024

@author: cruz
"""

# =============================================================================
# Natural Language Precessing
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# =============================================================================
# importacion del dataset
# =============================================================================

dataset = pd.read_csv("Restaurant_Reviews.tsv",
                      sep='\t',
                      quoting= 3) # ignora las " en el texto

# =============================================================================
# Limpieza de texto 
# =============================================================================

import re 
import nltk
nltk.download ('stopwords') # palabras inutiles que no nos sirven en un analisis (irrelevantes)
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer # funcion para stemizars las palabras

# frases limpias
corpus = []

for i in range(0,1000):
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i]) # letras deseadas
    review = review.lower() # convierte a minusculas
    review = review.split() # divide la palabra en una lista de caracteres
    
    # Hasta este momento tenemos palabras conjugada, ahora se debe buscar el
    # infinitivo para evitar redundancias
    ps = PorterStemmer()
    # se dejara la palabra que no este en stopwords
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    # juntamos las palabras con espacio
    review = ' '.join(review)
    corpus.append(review)


# =============================================================================
# Crear el Bag of Words
# =============================================================================
















