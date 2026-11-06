import argparse
import random
from pathlib import Path

import numpy as np

from src.data_loader import load_movielens_data

# Reproducibility
SEED = 42


def set_random_seed():
    random.seed(SEED)
    np.random.seed(SEED)

def load_data(data_dir):
    """Load MovieLens 1M dataset."""
    print("Loading MovieLens 1M dataset...")

    data_dir = Path(data_dir)

    required_files = [
        "ratings.dat",
        "movies.dat",
        "users.dat"
    ]

    for filename in required_files:
        if not (data_dir / filename).exists():
            raise FileNotFoundError(
                f"Missing dataset file: {filename}"
            )

    print("Dataset files found!")
    
    # TODO: Parse ratings.dat, movies.dat and users.dat

    ratings, movies, users = load_movielens_data(data_dir)

    print(f"Loaded {len(ratings)} ratings")
    print(f"Loaded {len(movies)} movies")
    print(f"Loaded {len(users)} users")

    print("\nRatings:")
    print(ratings.head())

    print("\nMovies:")
    print(movies.head())

    print("\nUsers:")
    print(users.head())

    print("\nData types:")
    print(ratings.dtypes)

    return ratings, movies, users


def run_pipeline(data_dir):
    """Run the complete recommendation project."""

    set_random_seed()

    print("Starting MovieLens recommendation project...")

    # 1. Load and parse data
    ratings, movies, users = load_data(data_dir)

    # 2. Analyze data
    # TODO: Implement data analysis

    # 3. Preprocess data and create temporal split
    # TODO: Implement temporal split

    # 4. Train recommendation models
    # TODO: Implement popularity baselines
    # TODO: Implement item-based kNN

    # 5. Evaluate models
    # TODO: Implement evaluation

    # 6. Save results and figures
    # TODO: Export results

    print("Project pipeline completed!")


def main():
    parser = argparse.ArgumentParser(
        description="Run MovieLens recommendation project"
    )

    parser.add_argument(
        "--data-dir",
        type=str,
        required=True,
        help="Path to MovieLens 1M dataset"
    )

    args = parser.parse_args()

    run_pipeline(args.data_dir)


if __name__ == "__main__":
    main()