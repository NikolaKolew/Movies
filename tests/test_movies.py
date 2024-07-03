import unittest
import pandas as pd
from movies.etl.movie import MovieDataset

class TestMovieDataset(unittest.TestCase):
    def setUp(self):
        self.movie_dataset = MovieDataset('../movies/cleaned_data/combined_movies_ratings.csv')

    def test_unique_movies_count(self):
        self.assertIsInstance(self.movie_dataset.get_unique_movies_count(), int)

    def test_average_rating(self):
        self.assertIsInstance(self.movie_dataset.get_average_rating(), float)

    def test_top_5_movies(self):
        top_5_movies = self.movie_dataset.get_top_5_movies()
        self.assertEqual(len(top_5_movies), 5)

    def test_movies_per_year(self):
        movies_per_year = self.movie_dataset.get_movies_per_year()
        self.assertTrue(isinstance(movies_per_year, pd.Series))

    def test_movies_per_genre(self):
        movies_per_genre = self.movie_dataset.get_movies_per_genre()
        self.assertTrue(isinstance(movies_per_genre, pd.Series))

if __name__ == '__main__':
    unittest.main()
