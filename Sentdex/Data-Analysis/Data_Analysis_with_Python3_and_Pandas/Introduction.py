import pandas as pd 

df = pd.read_csv("datasets/avocado.csv")

#print(df.head()) # default 5 row
#print(df.head(3))
#print(df.tail()) # default 5 row
#print(df.tail(3))

#print(df['AveragePrice'].head())
#print(df.AveragePrice.head())

#albany_df = df[df['region']=="Albany"]
albany_df = df[df.region=="Albany"]

#print(albany_df.head())
#print(albany_df.index)
#print(albany_df.set_index("Date"))

albany_df = albany_df.set_index("Date")
#print(albany_df.head())

albany_df['AveragePrice'].plot()