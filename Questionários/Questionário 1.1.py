import pandas as pd
import numpy as np

data = pd.read_csv('C:/Users/Arthur OS/PycharmProjects/icd/Dados/iris-with-errors.csv', header=(0))
print(data.head(25))
data = data.drop_duplicates()
data = data.replace("?", np.nan)
data = data.dropna()
data = data.drop(data.columns[[-1, -2]], axis=1)
print(data.head(25))
