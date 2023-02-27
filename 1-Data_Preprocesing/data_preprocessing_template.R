# =============================================================================
# --------------------Plantilla de Pre-procesado--------------------
# =============================================================================

# =============================================================================
# --------------------Importando dataset--------------------
# =============================================================================
# Estructura de los datos: {explicar eldataset y el objetivo}.
# Filas :{numero de filas}
# Columnas:
#           |{col1}|{col2}|{...} (vars independiente)
#           |{columna de var indep.}| (var_dependiente)
dataset = read.csv('dataset.csv')

# No se hace ninguna distincion entre variables independientes 
# y variables dependientes en R

# =============================================================================
# --------------------Tratamiendo de NAs--------------------
# =============================================================================

# Los valores desconocidos de los valores independientes son los NA´s
# ifelse("Condicion",Sentencia si es verdadera,sentencia si es falso)
dataset$Age = ifelse(is.na(dataset$Age),
                     # El valor que se va a sustituir que sera la media
                     ave(dataset$Age,FUN= function(x) mean(x,na.rm=TRUE)),
                     # se deja el valor como esta por defecto
                     dataset$Age)


dataset$Salary = ifelse(is.na(dataset$Salary),
                     # El valor que se va a sustituir que sera la media
                     ave(dataset$Salary,FUN= function(y) mean(y,na.rm=TRUE)),
                     # se deja el valor como esta por defecto
                     dataset$Salary)

# =============================================================================
# --------------------Codificar datos categoricos--------------------
# =============================================================================

# se convierte una columna en factores
dataset$Country = factor(dataset$Country,
                     # dandole un valos a cada etiqueta dentro de la columna
                     levels = c("France","Spain", "Germany"),
                     # etiquetas
                     labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                     # dandole un valos a cada etiqueta dentro de la columna
                     levels = c("No","Yes"),
                     # etiquetas
                     labels = c(0,1))

# =============================================================================
# --------------------Dividiendo dataset en conjuntos--------------------
# --------------------de entrenamiento y conjunto de testings------------
# =============================================================================

# install.packages("caTools") # solo se necesita ejecutar una vez
# library(caTools)

# configurando semilla aleatoria para la division de datos
set.seed(10)
# se elige el porcentaje de los datos para el training en %
split = sample.split(dataset$Purchased,SplitRatio = 0.8)

# Dividiendo el conjunto , False para el test
training_set = subset(dataset,split == FALSE)
# Dividiendo el conjunto , True para el training
testing_set = subset(dataset,split == TRUE)

# =============================================================================
# --------------------Escalado de variables--------------------
# =============================================================================

# Scale() necesitaremos especificar las filas y columnas
# para especificar cuales son variables numericas.
# Ya que factor() no sobreescribe el dataset
training_set[,2:3] = scale(training_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3])

