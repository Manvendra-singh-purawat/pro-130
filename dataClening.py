import csv
import pandas as pd

df=pd.read_csv("bright_stars.csv")

print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df.to_csv("bright_stars.csv")