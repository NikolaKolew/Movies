import pandas as pd
import ast

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv("../source/movies_metadata.csv")

print('Dataset Info:')
print(df.info())

print('First few rows of the dataset:')
print(df.head(3))

print('Missing values:')
print(df.isnull().sum())

print('Data types:')
print(df.dtypes)


df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')

# Convert 'budget' and 'revenue' to numeric, replacing any non-numeric values with NaN
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df['id'] = pd.to_numeric(df['id'], errors='coerce')
# Convert 'release_date' to datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Convert 'adult' and 'video' to boolean
df['adult'] = df['adult'].map({'True': True, 'False': False})
df['video'] = df['video'].map({'True': True, 'False': False})

def clean_column(column, key):
    def process_value(x):
        try:
            # Convert the string representation of list of dictionaries to actual list of dictionaries
            data = ast.literal_eval(x)
            # Check if data is a list (to handle cases where literal_eval returns a single dictionary or other unexpected types)
            if isinstance(data, list):
                # Join the values corresponding to the key
                return ', '.join([d[key] for d in data])
            elif isinstance(data, dict):
                # Handle case where literal_eval returns a single dictionary
                return data.get(key, '')
            else:
                # Handle unexpected cases gracefully
                return ''
        except (SyntaxError, ValueError):
            # Return empty string if the literal_eval fails (e.g., NaN values)
            return ''
    return column.apply(process_value)

columns_to_clean = {
    'genres': 'name',
    'production_companies': 'name',
    'production_countries': 'name',
    'spoken_languages': 'name'
}

# Apply the cleaning function to each column
for column, key in columns_to_clean.items():
    df[column] = clean_column(df[column], key)


print('Updated Dataset Info:')
print(df.info())

print('First few rows of cleaned dataset:')
print(df.head(23))

df.to_csv('../cleaned_data/movies_metadata_cleaned.csv', encoding='utf-8', index=False)
