import numpy as np
import pandas as pd

df = pd.read_excel("./data/ipo.xlsx")

#reading the data
def readingData():
    print(df.head(5))
    print(df.shape)
    print(df.info())
    print(df.isnull().sum())
    print(df.duplicated().sum())

#reading the missing columns
def missingValues():
    missingRows = df[df.isnull().any(axis=1)]
    print(missingRows)

#dropping unwanted columns
def dropUnwanted():
    global df
    columns_to_drop = ["IPO_Name",  "CMP(BSE)","CMP(NSE)", "Current Gains"]
    df = df.drop(columns = columns_to_drop)

    print(df.shape)

#handling missing values
def handleMissing():
    global df
    cols = ["QIB", "HNI", "RII", "Total"]
    df[cols] = df[cols].fillna(df[cols].median())
    df = df.dropna(subset=["List Price", "Listing Gain"])

# readingData()
dropUnwanted()
# missingValues()
handleMissing()
# missingValues()

df.to_excel("./data/ipo_cleaned.xlsx", index=False)
print("Saved Cleaned file")

