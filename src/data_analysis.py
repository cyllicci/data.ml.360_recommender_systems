import matplotlib.pyplot as plt
from pathlib import Path

def analyze_dataset(ratings, movies, users):
    """Calculate basic MovieLens dataset statistics."""

    n_users = ratings["user_id"].nunique()
    n_movies = ratings["movie_id"].nunique()
    n_ratings = len(ratings)

    density = n_ratings / (n_users * n_movies)
    sparsity = 1 - density

    print("\n=== Dataset Statistics ===")
    print(f"Users: {n_users:,}")
    print(f"Movies rated: {n_movies:,}")
    print(f"Movies in movie catalog: {len(movies):,}")
    print(f"Ratings: {n_ratings:,}")
    print(f"Density: {density:.6f} ({density * 100:.4f}%)")
    print(f"Sparsity: {sparsity:.6f} ({sparsity * 100:.4f}%)")

    return {
        "n_users": n_users,
        "n_movies": n_movies,
        "n_ratings": n_ratings,
        "density": density,
        "sparsity": sparsity,
    }


def analyze_interaction_distributions(ratings):
    """Analyze rating and interaction distributions."""

    figures_dir = Path("figures")
    figures_dir.mkdir(exist_ok=True)

    # 1. Rating distribution
    rating_counts = ratings["rating"].value_counts().sort_index()

    print("\n=== Rating Distribution ===")
    print(rating_counts)

    plt.figure(figsize=(8, 5))
    rating_counts.plot(kind="bar")
    plt.title("Distribution of Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Number of ratings")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(figures_dir / "rating_distribution.png")
    plt.close()

    # 2. Number of interactions per user
    user_interactions = ratings.groupby("user_id").size()

    print("\n=== Interactions per User ===")
    print(user_interactions.describe())

    plt.figure(figsize=(8, 5))
    plt.hist(user_interactions, bins=50)
    plt.title("Distribution of Interactions per User")
    plt.xlabel("Number of ratings per user")
    plt.ylabel("Number of users")
    plt.tight_layout()
    plt.savefig(figures_dir / "user_interactions.png")
    plt.close()

    # 3. Number of interactions per movie
    movie_interactions = ratings.groupby("movie_id").size()

    print("\n=== Interactions per Movie ===")
    print(movie_interactions.describe())

    plt.figure(figsize=(8, 5))
    plt.hist(movie_interactions, bins=50)
    plt.title("Distribution of Interactions per Movie")
    plt.xlabel("Number of ratings per movie")
    plt.ylabel("Number of movies")
    plt.tight_layout()
    plt.savefig(figures_dir / "movie_interactions.png")
    plt.close()

    print("\nDistribution analysis completed!")
    print("Figures saved in the figures/ directory.")