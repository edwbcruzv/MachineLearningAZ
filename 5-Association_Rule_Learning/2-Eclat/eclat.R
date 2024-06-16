# =============================================================================
# Eclat
# =============================================================================
# =============================================================================
# --------------------Importando dataset--------------------
# =============================================================================

dataset = read.csv('Market_Basket_Optimisation.csv', header = FALSE)

# No se hace ninguna distincion entre variables independientes 
# y variables dependientes en R
# =============================================================================
# --------------------Matriz Dispersa (o Esparcen)--------------------
# =============================================================================
# install.packages('arules')
# library(arules)

dataset = read.transactions("Market_Basket_Optimisation.csv",
                            sep = ',',
                            rm.duplicates = TRUE)

summary(dataset)
# nos muestra una grafica de los items mas frecuentes (N primeros)
itemFrequencyPlot(dataset, topN=50)

# =============================================================================
# --------------------Enternamiendo del arlgoritmo Eclat--------------------
# =============================================================================

# PASO 1: Decidir un soporte y nivel de confianza minimo.

# 3: una media de un producto que se vende 3 veces al dia
# 7: dias de la semana
# 7500: total de los productos
# 3*7/7500 = 0.0028, decidimos redondearlo a 0.003
# para la confianza R recomienda un 0.4

# PASO 2: Elegir todos los subconjuntos de transacciones con soporte superior al minimo elegido.
# PASO 3: Elegir todas las reglas de estos subconjuntos con nivel de confianza superior al minimo elegido.
rules = eclat(dataset,
                parameter = list(support = 0.004, minlen = 2))

 # PASO 4: Ordenar todas las reglas anteriores por lift descendiente.
inspect(sort(rules, by = 'support')[1:10])







