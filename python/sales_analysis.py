import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create mock sales data
np.random.seed(42)
dates = pd.date_range(start="2022-01-01", periods=200, freq='D')
data = {
    "Order Date": dates,
    "Sales": np.random.randint(100, 1000, size=200),
    "Profit": np.random.randint(-100, 300, size=200),
    "Category": np.random.choice(["Furniture", "Technology", "Office Supplies"], size=200)
}
df = pd.DataFrame(data)

# Step 2: Preprocess the data
df["Order Date"] = pd.to_datetime(df["Order Date"])
df['Month'] = df["Order Date"].dt.to_period("M")

# Step 3: Aggregate monthly sales
monthly_sales = df.groupby("Month")[["Sales", "Profit"]].sum().reset_index()
monthly_sales["Month"] = monthly_sales["Month"].astype(str)

# Step 4: Visualizations
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x="Month", y="Sales", marker="o")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=50)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="Category", y="Profit", estimator=np.sum)
plt.title("Total Profit by Category")
plt.tight_layout()
plt.show()
