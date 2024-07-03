from movies.etl.movie import MovieDataset


def main():
    csv_file_path = '../cleaned_data/combined_movies_ratings.csv'
    json_file_path = '../result/movies.json'

    movie_dataset = MovieDataset(csv_file_path)

    movie_dataset.print_results()

    movie_dataset.save_to_json(json_file_path)


if __name__ == "__main__":
    main()
