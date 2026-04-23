# LendingClub Loan Prediction Project

## Overview
This project predicts whether a borrower will fully repay their loan based on historical data from LendingClub.com (2007–2010). The goal is to assist investors in identifying high-probability repayment profiles using machine learning classification models.

## Dataset
The `loan_data.csv` contains 9,578 entries with features such as:
* **FICO Score**: Creditworthiness indicator.
* **Purpose**: Reason for the loan (e.g., debt consolidation, small business).
* **Interest Rate**: Cost of the loan.
* **Not Fully Paid**: Target variable (0 = Paid, 1 = Default).

## Workflow
1.  **Exploratory Data Analysis (EDA)**: Visualized relationships between FICO scores, credit policies, and interest rates using Seaborn histograms, countplots, and jointplots.
2.  **Data Preprocessing**: Converted the categorical `purpose` feature into dummy variables and split data into training (70%) and testing (30%) sets.
3.  **Modeling**:
    * **Decision Tree**: Trained a single classifier to establish a baseline.
    * **Random Forest**: Utilized an ensemble of 600 trees to improve predictive performance.

## Key Results
* **Random Forest**: Superior overall accuracy (~85%). It is excellent for predicting borrowers who will pay in full.
* **Decision Tree**: Lower overall accuracy but higher **Recall** for defaults. It is more effective at flagging risky borrowers that the Random Forest might miss.
