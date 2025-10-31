import pandas as pd

df = pd.read_csv("sales_data.csv")

summary = df.groupby("region").agg(
    total_revenue=("revenue", "sum"),
    total_quantity=("quantity", "sum")
).reset_index()

print("=== Sales Summary by Region ===")
print(summary)

summary.to_csv("sales_summary_output.csv", index=False)
print("\nSaved results to sales_summary_output.csv")
