import pandas as pd


df = pd.read_csv('../source/ratings.csv')

print('First few rows of the original dataset:')
print(df.head())

print('Dataset information:')
print(df.info())

print('Summary statistics:')
print(df.describe())

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

df.drop_duplicates(inplace=True)

print('Missing values:')
print(df.isnull().sum())

print('First few rows of the cleaned dataset:')
print(df.head())

print('Cleaned dataset information:')
print(df.info())

print('Cleaned dataset summary statistics:')
print(df.describe())

df.to_csv('../cleaned_data/ratings.csv', encoding='utf-8')
