from pathlib import Path

import pandas as pd


def load_movielens_data(data_dir):
    """Load and parse the MovieLens 1M dataset."""

    data_dir = Path(data_dir)

    ratings = pd.read_csv(
        data_dir / "ratings.dat",
        sep="::",
        engine="python",
        encoding="latin-1",
        names=["user_id", "movie_id", "rating", "timestamp"],
    )

    movies = pd.read_csv(
        data_dir / "movies.dat",
        sep="::",
        engine="python",
        encoding="latin-1",
        names=["movie_id", "title", "genres"],
    )

    users = pd.read_csv(
        data_dir / "users.dat",
        sep="::",
        engine="python",
        encoding="latin-1",
        names=["user_id", "gender", "age", "occupation", "zip_code"],
    )

    return ratings, movies, users