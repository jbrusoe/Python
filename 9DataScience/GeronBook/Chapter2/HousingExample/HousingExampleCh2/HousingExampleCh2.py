import pandas as pd
import os

HOUSING_PATH = "C:\\Users\\jbrus\\Documents\\GitHub\\Python\\9DataScience\\GeronBook\\Chapter2\\"

def load_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()
print(housing.head())
