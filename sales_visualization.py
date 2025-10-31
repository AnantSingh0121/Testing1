import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
revenue_by_region = df.groupby("region")["revenue"].sum()

plt.figure(figsize=(6, 4))
revenue_by_region.plot(kind="bar")
plt.title("Revenue by Region")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("revenue_by_region.png")

print("Visualization saved to revenue_by_region.png")
