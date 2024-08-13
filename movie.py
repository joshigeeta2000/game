import pandas as pd
import seaborn as sns
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt

# Load the datasets
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Merge the datasets on 'movieId'
data = pd.merge(ratings, movies, on='movieId')

# Create a new DataFrame for movie statistics
movie_stats = data.groupby('title').agg({'rating': ['mean', 'count']})
movie_stats.columns = ['average_rating', 'rating_count']

# Set a threshold for the number of ratings to consider popular movies
threshold = 50
popular_movies = movie_stats[movie_stats['rating_count'] >= threshold]

# Merge popular movies with the original data
data_popular = pd.merge(data, popular_movies, on='title')

# Create a pivot table with users as rows and movies as columns
movie_user_matrix = data_popular.pivot_table(index='userId', columns='title', values='rating').fillna(0)

# Convert the pivot table to a sparse matrix
movie_user_matrix_sparse = csr_matrix(movie_user_matrix.values)

# Create and fit the kNN model
model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=5, n_jobs=-1)
model_knn.fit(movie_user_matrix_sparse)

# Function to get movie recommendations
def get_movie_recommendations(movie_title):
    movie_index = movie_user_matrix.columns.get_loc(movie_title)
    distances, indices = model_knn.kneighbors(movie_user_matrix.iloc[:, movie_index].values.reshape(1, -1), n_neighbors=6)
    recommendations = movie_user_matrix.columns[indices.flatten()]
    return recommendations[1:]

# Example: Get recommendations for a specific movie
recommended_movies = get_movie_recommendations('Toy Story (1995)')
print("Recommended movies similar to 'Toy Story (1995)':")
for movie in recommended_movies:
    print(movie)
