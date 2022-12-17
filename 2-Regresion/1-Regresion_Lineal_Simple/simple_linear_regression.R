# Regresion Lineal Simple

# ----------------importando dataset----------------

dataset = read.csv('Salary_Data.csv')

# ----------------Dividiendo dataset en conjuntos----------------
# ----------------de entrenamiento y conjunto de testings----------------

# install.packages("caTools") # solo se necesita ejecutar una vez
# library(caTools)

# configurando semilla aleatoria para la division de datos
set.seed(0)
# se elige el porcentaje de los datos para el training en %
# se selecciona la columna de la variable dependiente o a predecir
split = sample.split(dataset$Salary,SplitRatio = 2/3)
print(split)
# Dividiendo el conjunto , True para el training
training_set = subset(dataset,split == TRUE)
# Dividiendo el conjunto , False para el test
testing_set = subset(dataset,split == FALSE)

# --------------------Crear modelo de Regresion Lineal--------------------
# --------------------Simple con el conjunto de entrenamiento--------------------
# visualisar documentacion de lm()
regressor=lm(formula=Salary ~ YearsExperience,data=training_set)
summary(regressor)

# --------------------Predecir el conjunto de test--------------------
# (modelo de prediccion,datos de testing)
y_pred=predict(regressor,newdata=testing_set)
print(y_pred)

# --------------------Visualizar los resultados de entrenamiento--------------------
# Para mostrar la grafica de datos de entrenamiento y la recta del modelo lineal

# Agregando componentes a mostrar
ggplot()+
  # Dobujando los puntos de entrenamiento
  geom_point(aes(x=training_set$YearsExperience,y=training_set$Salary),
             colour="red")+
  # Dobujando la linea de la prediccion, en base al entrenamiento
  geom_line(aes(x=training_set$YearsExperience,y=predict(regressor,newdata=training_set)),
            colour="blue")+
  ggtitle("Sueldo vs Años de experiencia(Entrenamiento)")+
  xlab("Sueldo ($)")+
  ylab("Anos de experiencia")

# --------------------Visualizar los resultados de test--------------------
# Para mostrar la grafica de datos de testing y la recta del modelo lineal


# Agregando componentes a mostrar
ggplot()+
  # Dobujando los puntos de testing
  geom_point(aes(x=testing_set$YearsExperience,y=testing_set$Salary),
             colour="red")+
  # Dobujando la linea de la prediccion, en base al testing
  geom_line(aes(x=testing_set$YearsExperience,y=y_pred),
            colour="blue")+
  ggtitle("Sueldo vs Años de experiencia(testing)")+
  xlab("Sueldo ($)")+
  ylab("Anos de experiencia")



