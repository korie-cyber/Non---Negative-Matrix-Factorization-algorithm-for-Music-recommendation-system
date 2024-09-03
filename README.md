# 🎧 Music Recommendation System Using Collaborative Filtering Techniques

## Project Overview

This repository contains the code and documentation for my final year project at Landmark University, titled **"Music Recommendation System Using Collaborative Filtering Techniques"**. The project aims to enhance user experiences on music streaming platforms by providing personalized music recommendations based on user behavior and song attributes.

## Introduction

With the explosion of digital music content, users often find it challenging to discover music that aligns with their unique tastes. This project addresses this issue by developing a music recommendation system that utilizes **Non-negative Matrix Factorization (NMF)**, a collaborative filtering technique. The NMF model is trained on a dataset of Spotify tracks, enabling it to uncover latent features that link user preferences with song characteristics.

## Problem Statement

In the current digital era, users are overwhelmed with the vast amount of available music content, making it difficult to find and interact with music that suits their tastes. Traditional recommendation algorithms often fail to fully capture users' nuanced preferences, limiting their ability to provide tailored recommendations. This project aims to overcome these challenges by developing a more accurate and personalized music recommendation system.

## Project Objectives

The primary objectives of this project are:
1. **Design a Music Recommendation Model**: Develop a model using collaborative filtering techniques that can effectively recommend songs based on user behavior.
2. **Implement the Model**: Build and train the model using the NMF algorithm, leveraging a dataset of Spotify tracks.
3. **Evaluate the Model**: Assess the model's performance using metrics such as Root Mean Squared Error (RMSE) and compare it with traditional approaches like Singular Value Decomposition (SVD).

## Dataset

The dataset used in this project was sourced from Kaggle and contains Spotify tracks across 125 unique genres. It includes various audio features such as popularity, duration, danceability, energy, key, loudness, and more. The data is stored in a CSV file, making it easy to manipulate and analyze.

## Methodology

### 1. **Data Preprocessing**
   - Load the dataset into a Pandas DataFrame.
   - Remove duplicates and handle missing values to ensure data quality.
   - Normalize ratings and prepare the data for model training.

### 2. **Model Development**
   - Construct a user-item interaction matrix where each row represents a user and each column represents a music item.
   - Apply the NMF algorithm to decompose this matrix into two lower-dimensional matrices, representing user and item features.
   - Train the NMF model to learn latent factors that capture the underlying patterns in the data.

### 3. **Model Evaluation**
   - Evaluate the model's performance using the RMSE metric.
   - Compare the NMF model's accuracy with the SVD baseline model.
   - Visualize the distribution of actual and predicted ratings using histograms.

## Results

The NMF model demonstrated superior accuracy in predicting user preferences, with a significantly lower RMSE compared to the SVD model. This indicates that NMF is more effective in capturing the diversity and complexity of user preferences, leading to more accurate and personalized music recommendations.

### Key Findings:
- **NMF outperforms SVD**: The NMF model provided more accurate predictions, making it a better choice for music recommendation tasks.
- **Model Interpretation**: The latent factors identified by the NMF model can be interpreted to understand the underlying preferences of users and characteristics of songs.
- **Visualization Insights**: The histograms revealed that while the model accurately predicted common ratings, there is room for improvement in capturing the full distribution of popularity ratings.

## Future Work

While the NMF model shows promising results, there are several areas for future exploration:
- **Incorporate Additional Features**: Including user demographics, social network data, and contextual information like listening time could further enhance the model's accuracy.
- **Explore Hybrid Models**: Combining collaborative filtering with content-based approaches may provide more comprehensive recommendations.
- **Model Optimization**: Further tuning of model parameters and the introduction of additional data sources can improve performance.

## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/music-recommendation-system.git
   cd music-recommendation-system
   ```
2. **Install Dependencies: Ensure you have Python installed, then install the required packages:**

  ```bash
  Copy code
  pip install -r requirements.txt
  ```

3. **Run the Model: Execute the Python script to preprocess the data, train the model, and evaluate the results:**

  ```bash
  Copy code
  python main.py
  ```

4. **Explore the Results: The script will output the RMSE values and generate visualizations of the predicted ratings:**

## Contributing
Contributions are welcome! If you have any ideas for improving the model or adding new features, feel free to fork the repository and submit a pull request.

## Contact
For any questions or feedback, please reach out to me at your.email@example.com.


