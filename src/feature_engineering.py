import pandas as pd

df = pd.read_excel("./data/ipo_cleaned.xlsx")

date = df['Date']
df['Year'] = date.dt.year
df['Month'] = date.dt.month
df['Day'] = date.dt.day_of_week

df.to_excel("./data/ipo_cleaned.xlsx")
print("Saved extracted data")

# print(df.head())