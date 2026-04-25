###KNN Classification Project

Classifying data points using the K-Nearest Neighbors algorithm.


Overview
Builds a KNN classifier on artificial data to predict a binary target class. The main focus is on finding the optimal K value using the elbow method.

What I Did
1. EDA
Used a Seaborn pairplot to visualize feature relationships, colored by target class.
2. Preprocessing
Scaled all features with StandardScaler and split the data 70/30 for training and testing.
3. Modeling
Started with n_neighbors=1 as a baseline, then looped through K values 1–39 and plotted error rate vs. K to find the sweet spot.
4. Final Model
Retrained with K=30, evaluated using a confusion matrix and classification report.

Results
The tuned model with K=30 outperformed the baseline K=1 model across precision, recall, and overall accuracy.

Built With
Python · Pandas · Seaborn · Scikit-learn · Matplotlib
