# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset =  pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# Splitting the dataset into the Training set and Test set
"""rom sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""



# Fitting the regression model to the dataset 
# Create your regressor here

# Predicting a new result
y_pred = regressor.predict(6.5)

# Visualiazing the Regression Result
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_2.predict(regressor.fit_transform(X)), color='blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Predecting a new result in polynomial regression
lin_reg_2.predict(regressor.fit_transform([[6.5]]))










