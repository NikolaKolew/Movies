import pandas as pd

df = pd.read_csv('../source/links.csv')

print('Dataset info:')
print(df.info())

print('First few rows of the dataset:')
print(df.head())

print('Missing values:')
print(df.isnull().sum())

print('Number of duplicate rows:')
print(df.duplicated().sum())

print('Basic statistics of numeric columns:')
print(df.describe())

df['movieId'] = df['movieId'].astype(int)
df['imdbId'] = df['imdbId'].astype(int)

# Fill missing values in tmdbId with -1 and convert to integer type
df['tmdbId'] = df['tmdbId'].fillna(-1).astype(int)

df = df[(df['movieId'] > 0) & (df['imdbId'] > 0) & ((df['tmdbId'] > 0) | (df['tmdbId'] == -1))]

print('Cleaned dataset info:')
print(df.info())

print('First few rows of the cleaned dataset:')
print(df.head())

print('Missing values:')
print(df.isnull().sum())

print('Basic statistics of numeric columns:')
print(df.describe())

df.to_csv('../cleaned_data/links.csv', encoding='utf-8')

