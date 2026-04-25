LendingClub Loan Prediction

Can we predict if a borrower will pay back their loan? This project finds out.


Overview
Using historical LendingClub data from 2007–2010, this project builds classification models to predict loan repayment. Useful for investors trying to spot reliable borrowers before committing capital.

Dataset
loan_data.csv — 9,578 entries
Key features:

FICO Score — creditworthiness of the borrower
Loan Purpose — debt consolidation, small business, etc.
Interest Rate — cost of the loan
Not Fully Paid — target variable (0 = repaid, 1 = defaulted)


What I Did
1. Exploratory Data Analysis
Dug into relationships between FICO scores, interest rates, and credit policy using Seaborn histograms, countplots, and jointplots.
2. Preprocessing
Encoded the purpose column into dummy variables and split the data 70/30 for training and testing.
3. Modeling
Trained two classifiers and compared their strengths:

* Decision Tree — baseline model
** Random Forest — ensemble of 600 trees


Results
*** Random Forest hit ~85% accuracy — the go-to for identifying borrowers likely to repay in full.
*** Decision Tree trades overall accuracy for higher recall on defaults — better at flagging risky loans the Random Forest might let slip through.

Built With
Python · Pandas · Seaborn · Scikit-learn
