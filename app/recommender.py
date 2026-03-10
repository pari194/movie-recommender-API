import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Create user-movie matrix
movie_ratings = ratings.pivot_table(
    index="movieId",
    columns="userId",
    values="rating"
).fillna(0)

# Compute similarity between movies
movie_similarity = cosine_similarity(movie_ratings)

similarity_df = pd.DataFrame(
    movie_similarity,
    index=movie_ratings.index,
    columns=movie_ratings.index
)

# Map movieId to title
movie_titles = movies.set_index("movieId")["title"]


def get_recommendations(title, n=5):
    movie_id = movie_titles[movie_titles == title].index[0]

    similar_scores = similarity_df[movie_id]

    similar_movies = similar_scores.sort_values(ascending=False)

    similar_movies = similar_movies.iloc[1:n+1]

    return movie_titles.loc[similar_movies.index]