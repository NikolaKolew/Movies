import pandas as pd
import json
from movies.logger.logger import setup_logger


class MovieDataset:
    def __init__(self, csv_file_path):

        self.logger = setup_logger(__name__)
        try:
            self.df = pd.read_csv(csv_file_path)
            self.logger.info("Dataset loaded successfully.")
        except Exception as e:
            self.logger.error(f"Error loading dataset: {e}")
            raise

    def get_unique_movies_count(self):
        return self.df['title'].nunique()

    def get_average_rating(self):
        return self.df['rating'].mean()

    def get_top_5_movies(self):
        return self.df.sort_values(by='rating', ascending=False).head(5)

    def get_movies_per_year(self):
        return self.df['release_date'].value_counts().sort_index()

    def get_movies_per_genre(self):
        genres = self.df['genres'].str.split(',').explode().value_counts()
        return genres

    def print_results(self):
        self.results = {}

        # Number of unique movies
        self.results['unique_movies_count'] = self.get_unique_movies_count()

        # Average rating of all movies
        self.results['average_rating'] = round(self.get_average_rating(), 2)

        # Top 5 highest rated movies
        top_5_movies = self.get_top_5_movies()
        self.results['top_5_movies'] = []
        for index, row in top_5_movies.iterrows():
            movie_info = {
                'title': row['title'],
                'year': row['release_date'][:4],
                'rating': row['rating']
            }
            self.results['top_5_movies'].append(movie_info)

        # Number of movies released each year
        movies_per_year = self.get_movies_per_year()
        self.results['movies_per_year'] = {str(year): count for year, count in movies_per_year.items()}

        # Number of movies in each genre
        movies_per_genre = self.get_movies_per_genre()
        self.results['movies_per_genre'] = {genre.strip(): count for genre, count in movies_per_genre.items()}

        # Print results to console
        self._print_results_to_console()

    def _print_results_to_console(self):
        print(f"Number of unique movies: {self.results['unique_movies_count']}")
        print(f"Average rating of all movies: {self.results['average_rating']:.2f}")

        print("Top 5 highest rated movies:")
        for movie in self.results['top_5_movies']:
            print(f"{movie['title']} ({movie['year']}) - Rating: {movie['rating']}")

        print("Number of movies released each year:")
        for year, count in self.results['movies_per_year'].items():
            print(f"{year}: {count}")

        print("Number of movies in each genre:")
        for genre, count in self.results['movies_per_genre'].items():
            print(f"{genre}: {count}")

    def save_to_json(self, json_file_path):
        try:
            with open(json_file_path, 'w') as f:
                json.dump(self.results, f, indent=4)
            self.logger.info(f"Analysis results saved to {json_file_path}")
        except Exception as e:
            self.logger.error(f"Error saving analysis results to JSON: {e}")
            raise

