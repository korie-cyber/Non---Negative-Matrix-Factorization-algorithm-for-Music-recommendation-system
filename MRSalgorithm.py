# Music Recommendation System Algorithm code
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from scipy.sparse import coo_matrix
from sklearn.decomposition import NMF
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('d:\\datasets\\spotify\\dataset1.csv')

# Preprocess the data
data_agg = data[['track_id', 'artists', 'popularity']]
train_data_agg, test_data_agg = train_test_split(data_agg, test_size=0.2, random_state=42)

# Encode 'track_id' and 'artists' to integer identifiers
label_encoder = LabelEncoder()
train_data_agg['track_id_encoded'] = label_encoder.fit_transform(train_data_agg['track_id'])
train_data_agg['artists_encoded'] = label_encoder.fit_transform(train_data_agg['artists'])

# Convert the train dataset to a sparse matrix with floating-point data type
train_matrix_sparse = coo_matrix((train_data_agg['popularity'], (train_data_agg['track_id_encoded'], train_data_agg['artists_encoded'])), dtype=np.float64)

# Perform NMF
k = 5  # Number of latent factors
nmf_model = NMF(n_components=k)
U = nmf_model.fit_transform(train_matrix_sparse)
Vt = nmf_model.components_

# Reconstruct the original matrix
predicted_ratings = np.dot(U, Vt)

# Convert the predicted ratings matrix to DataFrame
predicted_ratings_df = pd.DataFrame(predicted_ratings, index=train_data_agg['track_id_encoded'].unique())

# # Get test data popularity values
# test_data_agg['track_id_encoded'] = label_encoder.transform(test_data_agg['track_id'])
# test_data_agg['artists_encoded'] = label_encoder.transform(test_data_agg['artists'], handle_unknown='ignore')

# Create a mapping of unique track IDs and artists to integer identifiers
track_id_map = {track_id: idx for idx, track_id in enumerate(train_data_agg['track_id'].unique())}
artists_map = {artist: idx for idx, artist in enumerate(train_data_agg['artists'].unique())}

# Apply the mappings to the test dataset
test_data_agg['track_id_encoded'] = test_data_agg['track_id'].map(track_id_map).fillna(-1).astype(int)
test_data_agg['artists_encoded'] = test_data_agg['artists'].map(artists_map).fillna(-1).astype(int)

# Filter out rows with unknown labels
test_data_agg_filtered = test_data_agg[(test_data_agg['track_id_encoded'] != -1) & (test_data_agg['artists_encoded'] != -1)]

# Convert the test dataset to a sparse matrix with floating-point data type
test_matrix_sparse = coo_matrix((test_data_agg_filtered['popularity'], (test_data_agg_filtered['track_id_encoded'], test_data_agg_filtered['artists_encoded'])), shape=train_matrix_sparse.shape, dtype=np.float64)

# test_matrix_sparse = coo_matrix((test_data_agg['popularity'], (test_data_agg['track_id_encoded'], test_data_agg['artists_encoded'])), shape=train_matrix_sparse.shape, dtype=np.float64)

# Predict ratings for test data
test_predicted_ratings = np.dot(U, Vt)

# Get predicted ratings for test data
test_predicted_ratings_df = pd.DataFrame(test_predicted_ratings, index=train_data_agg['track_id_encoded'].unique())

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(test_matrix_sparse.toarray(), test_predicted_ratings))
print("RMSE:", rmse)


import matplotlib.pyplot as plt

# Extract actual popularity values for the test data
actual_popularity = test_matrix_sparse.toarray()[test_data_agg_filtered['track_id_encoded'], test_data_agg_filtered['artists_encoded']]

# Extract predicted ratings for the test data
predicted_ratings_test = np.dot(U, Vt)[test_data_agg_filtered['track_id_encoded'], test_data_agg_filtered['artists_encoded']]

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot distribution of actual popularity
axs[0].hist(actual_popularity, bins=30, alpha=0.5, color='blue')
axs[0].set_title('Distribution of Actual Popularity')
axs[0].set_xlabel('Popularity')
axs[0].set_ylabel('Frequency')

# Plot distribution of predicted ratings
axs[1].hist(predicted_ratings_test, bins=30, alpha=0.5, color='orange')
axs[1].set_title('Distribution of Predicted Ratings')
axs[1].set_xlabel('Ratings')
axs[1].set_ylabel('Frequency')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()