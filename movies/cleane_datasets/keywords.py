import pandas as pd
import json

df = pd.read_csv('../source/keywords.csv')

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


df_cleaned = df.drop_duplicates().reset_index(drop=True)

def parse_json(json_str):
    try:
        return json.loads(json_str.replace("'", '"'))
    except:
        return []


df['keywords'] = df['keywords'].apply(parse_json)

df_cleaned['id'] = df_cleaned['id'].astype(int)

print('Cleaned dataset info:')
print(df_cleaned.info())

# Show the first few rows of the cleaned dataset
print('First few rows of the cleaned dataset:')
print(df_cleaned.head().to_string())

# Verify no missing values
print('Missing values:')
print(df_cleaned.isnull().sum())

df.to_csv('../cleaned_data/keywords.csv', encoding='utf-8')
