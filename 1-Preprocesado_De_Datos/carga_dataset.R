# importando datasets

dataset = read.csv('Data.csv')

# tratamiento de valores NAs

dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age,FUN= function(x) mean(x,na.rm=TRUE)),
                     dataset$Age)


dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary,FUN= function(y) mean(y,na.rm=TRUE)),
                        dataset$Salary)

# Codificar datos categoricos

dataset$Country = factor(dataset$Country,
                         levels = c("France","Spain", "Germany"),
                         labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No","Yes"),
                           labels = c(0,1))

# Dividir los datos en conjunto de entrenamiento y conjunto de test

# install.packages("caTools") # solo se necesita ejecutar una vez
library(caTools)
set.seed(10) # aleatorio
split = sample.split(dataset$Purchased,SplitRatio = 0.8)

training_set = subset(dataset,split == FALSE)
testing_set = subset(dataset,split == TRUE)

# Escalado de valores

training_set[,2:3] = scale(training_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3])

