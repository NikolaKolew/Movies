import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


ratings_normal = pd.read_csv('../cleaned_data/ratings.csv', encoding='utf-8')
ratings_small = pd.read_csv('../cleaned_data/ratings_small.csv', encoding='utf-8')
ratings_normal = ratings_normal[['movieId', 'rating']]
ratings_small = ratings_small[['movieId', 'rating']]


frames = [ratings_normal, ratings_small]
merged_ratings = pd.concat(frames)

average_ratings = merged_ratings.groupby('movieId')['rating'].mean().reset_index()

movies = pd.read_csv('../cleaned_data/movies_metadata_cleaned.csv')
ratings = average_ratings

movies = movies.dropna(subset=['id'])
ratings = ratings.dropna(subset=['movieId'])

movies['id'] = movies['id'].astype(int)
ratings['movieId'] = ratings['movieId'].astype(int)

ratings.drop_duplicates()
movies.drop_duplicates()


combined_df = pd.merge(movies, ratings, left_on='id', right_on='movieId')

movies_ids = len(set(movies['id']))
ratings_ids = len(set(ratings['movieId']))

print(movies_ids)
print(ratings_ids)


combined_df.drop_duplicates()
print(combined_df.info())
print(combined_df.head(23))
combined_df.to_csv('../cleaned_data/combined_movies_ratings.csv', encoding='utf-8', index=False)

