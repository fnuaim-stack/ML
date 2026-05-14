# Credit Card Customer Segmentation
A machine learning project that uses K-Means clustering to segment credit card customers based on their usage behavior.

## Dataset
File: CC_GENERAL.csv
Size: 8,950 customers × 18 features
Key features include: BALANCE, PURCHASES, CASH_ADVANCE, CREDIT_LIMIT, PAYMENTS, and various frequency columns.

## Project Steps

Data Cleaning — Drop CUST_ID, fill missing values with column mean
EDA — Histograms, correlation heatmap, scatter plots
Feature Scaling — StandardScaler to normalize all features
Choosing K — Elbow method + Silhouette score (K=1 to 10)
Final Model — KMeans with K=3 (random_state=42, n_init=10)
Cluster Analysis — Group summary table + customer counts
Visualization — PCA 2D plot of clusters

## Results

| Cluster | Description | Size |
|---------|-------------|------|
| 0 | **Cash Advance Users** — High balance, heavy cash borrowing, low purchases | ~1,596 |
| 1 | **High-Value Purchasers** — High spending, high credit limit, pays reliably | ~1,235 |
| 2 | **Low-Activity Users** — Low balance, occasional purchases, average behavior | ~6,119 |

K=3 was chosen based on the highest silhouette score (≈ 0.25).
