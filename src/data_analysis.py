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