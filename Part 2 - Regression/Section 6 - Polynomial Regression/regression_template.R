# Regression Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]


# Fitting Regression Model to the dataset
# Create your Regression here


# Predicting a new result
predict(regressor, newdata = data.frame(Level = 6.5))

# Visualizing the Regression Model results (for higher resolution and smoother curve)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), 
             colour = 'red') + 
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))), 
            colour = 'blue') + 
  ggtitle('Truth or Bluff (Regression Model)') + 
  xlab('Level') +
  ylab('Salary')











