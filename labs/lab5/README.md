# Lab 5: Task Summaries

### Task 1: New Feature
* **Feature:** Created a distance-per-quantity feature (`Delivery_Distance_km` / `Quantity`).
* **Reason:** This helps the model understand the delivery effort relative to the order size, which can be a better predictor of order status than distance alone.

### Task 2: Peak Hour Rule
* **Action:** Changed the time range for peak hours.
* **Result:** Accuracy stayed at 0.8519, showing that the specific hour of the order does not strongly impact the final status in this dataset.

### Task 3: Item Name Reduction
* **Action:** Tested different `top_k` values (10, 30, 50) for the most frequent items.
* **Result:** Increasing the number of items did not improve the score. Numerical data like distance remains more important than the item name.

### Task 4: Feature Selection
* **Action:** Ran the optional selection tool.
* **Result:** Accuracy remained 0.8519.
* **Conclusion:** It was beneficial for making the model faster and simpler, but it did not help predict the minority classes (Cancelled/In Transit).