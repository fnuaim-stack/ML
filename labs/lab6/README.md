# Ecommerce Customer Analytics: Linear Regression

### Project Overview
A machine learning project focused on predicting **Yearly Amount Spent** for an Ecommerce company. The goal is to determine whether the company should focus its efforts on their **Mobile App** or **Website** based on customer usage patterns.

### Dataset
The project utilizes the `Ecommerce Customers.csv` dataset, which contains:
* **Avg. Session Length**: In-store style advice sessions.
* **Time on App**: Average time spent on the app in minutes.
* **Time on Website**: Average time spent on the website in minutes.
* **Length of Membership**: Years the customer has been with the company.

### Workflow
1.  **Data Exploration**: Analyzing correlations and distributions using `Seaborn`.
2.  **Model Training**: Using `Scikit-Learn` to split data (70/30) and train a **Linear Regression** model.
3.  **Prediction**: Testing the model against unseen data.
4.  **Evaluation**: Calculating error metrics (**MAE**, **MSE**, **RMSE**).

### Technical Requirements
* **Language**: Python 3.x
* **Key Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `sklearn`

### Usage
Run the `ARTI308 Lab6.ipynb` notebook to see the data analysis and the resulting model coefficients.