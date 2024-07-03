import pandas as pd

df = pd.read_csv("../source/links_small.csv")

df['tmdbId'] = df['tmdbId'].fillna(-1).astype(int)

print(df.head())

print(df.info())

print(df.describe())

df.to_csv('../cleaned_data/links_small.csv', encoding='utf-8')
