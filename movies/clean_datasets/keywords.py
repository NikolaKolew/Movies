import pandas as pd
from ast import literal_eval
from collections import ChainMap
pd.set_option('display.max_columns', None)

df = pd.read_csv('../source/keywords.csv')

print('First few rows of the dataset:')
print(df.head(3))

print('Missing values:')
print(df.isnull().sum())

print('Number of duplicate rows:')
print(df.duplicated().sum())

df = df.drop_duplicates().reset_index(drop=True)

df['id'] = df['id'].astype(int)

def safe_eval(x):
    if pd.isna(x):
        return []
    try:
        return literal_eval(x)
    except:
        return []

df['keywords'] = df['keywords'].apply(safe_eval).apply(lambda x: dict(ChainMap(*x)))
df = pd.concat([df['keywords'].apply(pd.Series), df['id']], axis=1)

print('Cleaned dataset info:')
print(df.info())

# Show the first few rows of the cleaned dataset
print('First few rows of the cleaned dataset:')
print(df.head(3))

# Verify no missing values
print('Missing values:')
print(df.isnull().sum())
df.fillna(value=0)

#df.to_csv('../cleaned_data/keywords.csv', encoding='utf-8')
