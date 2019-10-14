import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

import os

HOUSING_PATH = "C:\\Users\\jbrus\\Documents\\GitHub\\Python\\9DataScience\\GeronBook\\Chapter2\\"

def load_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

#Main program
housing = load_housing_data()
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

print("\nTraining Set")
print(train_set)

print("\nTesting Set")
print(test_set)

print("\n\nCreating Stratified Data")
housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

print( housing["income_cat"].value_counts() / len(housing))