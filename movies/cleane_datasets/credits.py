import pandas as pd
import json


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

def parse_json(json_str):
    try:
        return json.loads(json_str.replace("'", '"'))
    except:
        return []

# Parse JSON in 'cast' and 'crew' columns
df['cast'] = df['cast'].apply(parse_json)
df['crew'] = df['crew'].apply(parse_json)


print('Cleaned dataset info:')
print(df.info())

df.to_csv('../cleaned_data/credits.csv', encoding='utf-8')