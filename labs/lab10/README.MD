# SVM Assignment – Iris Dataset
 
A machine learning project that uses a **Support Vector Machine (SVM)** to classify iris flowers into three species based on their physical measurements.
 
---
 
## Dataset
 
The **Iris dataset** contains 150 flower samples from 3 species — Setosa, Versicolor, and Virginica — each described by 4 features: sepal length, sepal width, petal length, and petal width. The goal is to predict the species from these measurements.
 
---
 
## What the Notebook Covers
 
**1. Exploratory Data Analysis**
- A **pairplot** visualizes how well the three species separate across all features. Setosa is clearly the most separable species.
- A **KDE plot** shows the density of Setosa's sepal length vs. sepal width.
**2. Train/Test Split**
The data is split 70/30 into training and test sets so the model is evaluated on data it hasn't seen before.
 
**3. Training the SVM**
A `SVC()` classifier is trained on the training data. It learns the boundaries between the three species.
 
**4. Model Evaluation**
Predictions are made on the test set and evaluated using a **confusion matrix** and a **classification report** (precision, recall, F1-score).
 
**5. Hyperparameter Tuning with GridSearchCV**
`GridSearchCV` tests different combinations of the `C` and `gamma` parameters to find the best-performing version of the model using cross-validation.
 
---
 
## Results
 
Both the default and tuned SVM achieve around **98% accuracy**. The dataset is small and clean, so the default settings already work very well. GridSearchCV is more impactful on larger, noisier datasets.
 
