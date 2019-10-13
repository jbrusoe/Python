import pandas as pd
import matplotlib.pyplot as plt
import os

HOUSING_PATH = "C:\\Users\\jbrus\\Documents\\GitHub\\Python\\9DataScience\\GeronBook\\Chapter2\\"

def load_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()
print(housing.head())
print("\nHousing Info")
print(housing.info())
print("\nOcean Proximity Values")
print(housing["ocean_proximity"].value_counts())
print("\nDescribe Method Output")
print(housing.describe())

#Plot data
housing.hist(bins=50, figsize=(20,15))
plt.show()