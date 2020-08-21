# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range (0, 20)])
    
# Training Apriori on the dataset
results = []
from fim import eclat
rules = eclat(tracts = transactions, zmin = 1)
rules.sort(key = lambda x: x[1], reverse = True)


# Visualizing  the results
results = list(rules)   