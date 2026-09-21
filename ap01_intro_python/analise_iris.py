import pandas as pd
df = pd.read_csv("Iris.csv")
print(df.shape)
print(df.head(5))
print(df["Species"].value_counts())
print(df.groupby("Species")["PetalLengthCm"].mean().round(3))
print(df.groupby("Species")["PetalLengthCm"].agg(["min", "max"]))
