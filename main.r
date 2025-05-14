
# this is a program used to calculate the data set form the iris data set where certain data is provided within the library 
# the iris data set contain specis of flowers and the length of it   

data("iris")

# str is the function which is used to get the structure of the data set
# variables and data Types are defined 
str(iris)

# Summary is the funaction to summerize tha data set numeric variables and specific distributions
summary(iris)

# from here the visualization of the data set is done 
# histogram is used to plot the data set and the distribution of the data set

# the data set are divided into 4 parts and the histogram is plotted for each of the data
# 2 by 2 matrix is used to plot the data set
par(mfrow = c(2,2))

# hist means histogram and the data are set for spela length and width and petal length and width.
hist(iris$Sepal.Length, main = "Sepal Length Distribution", xlab = "Length (cm)",)
hist(iris$Sepal.Width, main = "Sepal Width Distribution", xlab = "Width (cm)",)
hist(iris$Petal.Length, main = "Petal Length Distribution", xlab = "Length (cm)",)
hist(iris$Petal.Width, main = "Petal Width Distribution", xlab = "Width (cm)",)

# boxes are ploted with the spiral length and petal lenght as they are represented in different color as light blue and pink respectively
# the data is divided into 1 by 1 matrix.
par(mfrow = c(1,1))
boxplot(Sepal.Length ~ Species, data = iris, main ="Sepal Length by Species", col = "lightblue")
boxplot(Petal.Length ~ Species, data = iris, main ="Petal Length by Species", col = "pink")

# to show the relationship between the data set the scatter is ploted.
pairs(iris[, 1:4], col = iris$Species, pch= 19, main = "Pariswise relationships by Species")

# get_mod function is used to set the mode of the given data 
# mod is the most frequently occuring value in the data set
get_mod <- function (v){
  uniqv <- unique(v)
  # tabulate counts the number of times each value occurs in v 
  uniqv[which.max(tabulate(match(v,uniqv)))]
}


# calculation for each of the variables are done here 
# stats_table  stores the data set in frame and tha data is calculated for each vairables.
# initally the data frame is empty
variables <- c( 'Sepal.Length','Sepal.Width','Petal.Length', 'Petal.Width')
stats_table <- data.frame()


#  for loop is used to iterate the data set and calculate the mean, median, mod, variance, standard devitation
# and range of the date set.
# here v is the variable which itterates the dataset 
for ( v in variables){
  data <- iris[[v]]

# calculating statstics for each variable as mean, median, mode, variance, standard deviation and range.
  mean_v <- mean(data)
  median_v <- median(data)
  mode_v <- get_mod(data)
  variance_v <- var(data)
  standardDeviation_v <- sd(data)
  range_val <- paste(min(data), "-", max(data))


# now the data is stored in the table format as the data frame is initally empty and the data is appended to it after the calcuation
  stats_table <- rbind(stats_table, data.frame(
    Varibles = v,
    Mean = round(mean_v,2),
    Median = round(median_v,2),
    Mode = mode_v,
    Variance = round(variance_v,2),
    StandardDeviation = round(standardDeviation_v,2),
    Range = range_val
  ))
}

#  then the tabulated data is printed in the table format 
print ('Descriptive Statistics for Iris Dataset')
print(stats_table)



# the code is well documented maintaing the integrity, readability and the functionality of the code.
# the code full fills the case study that is provided to show case the knowledge of the data set.

