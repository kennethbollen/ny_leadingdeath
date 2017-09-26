import pandas as pd

#import the data via NYC Open Data API
df = pd.read_csv("https://data.cityofnewyork.us/resource/uvxr-2jwn.csv")

#data exploration

print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

#clean the data: the variables Deaths, Death Rate and Age Adjusted Death Rate are stored as objects and need to be transformed into numerical values

df["Deaths"] = pd.to_numeric(df["Deaths"], errors="coerce")
df["Death Rate"] = pd.to_numeric(df["Death Rate"], errors="coerce")
df["Age Adjusted Death Rate"] = pd.to_numeric(df["Age Adjusted Death Rate"], errors="coerce")

#transform the Year variable into a cateogry

df.Year = df.Year.astype("category")

#clean the null values as a result of the datatype transformation using their averages

death_avg = df["Deaths"].mean()
death_rate_avg = df["Death Rate"].mean()
adj_death_rate_avg = df["Age Adjusted Death Rate"].mean()

df["Deaths"] = df["Deaths"].fillna(values=death_avg)
df["Death Rate"] = df["Death Rate"].fillna(values=death_rate_avg)
df["Age Adjusted Death Rate"] = df["Age Adjusted Death Rate"].fillna(values=adj_death_rate_avg)

