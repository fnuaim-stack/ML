LendingClub Loan Prediction
Predicts loan repayment using historical LendingClub data (2007–2010).
Dataset
loan_data.csv with 9,578 entries. Key features: FICO score, loan purpose, interest rate, and a binary repayment label (paid vs. defaulted).
What I Did
Kicked off with EDA to understand how FICO scores, interest rates, and credit policy relate to defaults. Then encoded the purpose column, did a 70/30 split, and trained two models.
Results
Random Forest (600 trees) hit ~85% accuracy and is solid for spotting reliable borrowers. Decision Tree trades some accuracy for better recall on defaults — more useful if catching risky loans is the priority.
