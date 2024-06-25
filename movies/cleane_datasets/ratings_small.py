import pandas as pd

df = pd.read_csv('../source/ratings_small.csv')

print('First few rows of the original dataset:')
print(df.head())

print('Dataset information:')
print(df.info())

print('Summary statistics:')
print(df.describe())

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

duplicates = df.duplicated().sum()
df.drop_duplicates(inplace=True)

missing_values = df.isnull().sum()

print('First few rows of the cleaned dataset:')
print(df.head())

print('Cleaned dataset information:')
print(df.info())

print('Cleaned dataset summary statistics:')
print(df.describe())

print(f'Number of duplicates removed: {duplicates}')
print('Missing values:')
print(missing_values)

df.to_csv('../cleaned_data/ratings_small.csv', encoding='utf-8')

