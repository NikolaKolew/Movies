import pandas as pd
from ast import literal_eval

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv("../source/movies_metadata.csv")
#
# print('Dataset Info:')
# print(df.info())
#
# print('First few rows of the dataset:')
# print(df.head())
#
# print('Missing values:')
# print(df.isnull().sum())
#
# print('Data types:')
# print(df.dtypes)

# Clean up the 'popularity' column
df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')

# Convert 'budget' and 'revenue' to numeric, replacing any non-numeric values with NaN
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')

# Convert 'release_date' to datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Convert 'adult' and 'video' to boolean
df['adult'] = df['adult'].map({'True': True, 'False': False})
df['video'] = df['video'].map({'True': True, 'False': False})

# Function to safely parse JSON-like strings
def safe_eval(x):
    if pd.isna(x):
        return []
    try:
        return literal_eval(x)
    except:
        return []

# Parse JSON-like strings
for column in ['genres', 'production_companies', 'production_countries', 'spoken_languages']:
    df[column] = df[column].apply(safe_eval)

# Display updated info
print('Updated Dataset Info:')
print(df.info())

# Display the first few rows of cleaned data
print('First few rows of cleaned dataset:')
print(df.head(23))

df.to_csv('../cleaned_data/movies_metadata_cleaned.csv', encoding='utf-8')
