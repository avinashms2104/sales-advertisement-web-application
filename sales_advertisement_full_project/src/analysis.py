import pandas as pd

df = pd.read_csv("data/campaign_dataset.csv")

df["conversion_rate"] = df["conversions"] / df["clicks"]
df["ctr"] = df["clicks"] / df["impressions"]

summary = df.groupby("campaign")[["clicks","conversions","cost_usd"]].sum()

print("Campaign Summary")
print(summary)

best = summary["conversions"].idxmax()
print("\nBest Performing Campaign:", best)