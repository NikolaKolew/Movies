import pandas as pd
import json
from ast import literal_eval
from collections import ChainMap
pd.set_option('display.max_columns', None)



df = pd.read_csv("../source/credits.csv")

# print('Dataset info:')
# print(df.info())
#
# print('First few rows of the dataset:')
# print(df.head())
#
# print('Summary statistics:')
# print(df.describe())
#
# print('Missing values:')
# print(df.isnull().sum())
#
# print('Number of duplicate rows:', df.duplicated().sum())
#

df = df.drop_duplicates().reset_index(drop=True)
print(df.head(3))
def safe_eval(x):
    if pd.isna(x):
        return []
    try:
        return literal_eval(x)
    except:
        return []

# Parse JSON in 'cast' and 'crew' columns
df1 = df['cast'] = df['cast'].apply(safe_eval).apply(lambda x: dict(ChainMap(*x)))
df2 = df['crew'] = df['crew'].apply(safe_eval).apply(lambda x: dict(ChainMap(*x)))
df1 = pd.concat([df['cast'].apply(pd.Series), df['id']], axis=1)
df2 = pd.concat([df['crew'].apply(pd.Series), df['id']], axis=1)

#
# print('Cleaned dataset info:')
# print(df1.head(3))
# print(df1.info())
# print(df2.head(3))
# print(df2.info())

result = pd.concat([df1, df2], axis=1, join="inner")

print(result.head(3))
print(result.info())
df.fillna(value=0)


result.to_csv('../cleaned_data/credits.csv', encoding='utf-8')