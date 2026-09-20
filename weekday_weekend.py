import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV and use dates as the index.
daily = pd.read_csv("daily_summary.csv", index_col="date", parse_dates=True)

# Keep dates from August 1, 2025, onward.
current = daily[daily.index >= "2025-08-01"]

# Select the step-count column.
steps = current["HKQuantityTypeIdentifierStepCount"]

# Saturday = 5 and Sunday = 6.
is_weekend = steps.index.dayofweek >= 5

# Calculate averages. Missing values are ignored.
avg_weekday = steps[~is_weekend].mean()
avg_weekend = steps[is_weekend].mean()

print(f"Average weekday steps: {avg_weekday:.0f}")
print(f"Average weekend steps: {avg_weekend:.0f}")

# Create a bar chart comparing the averages.
plt.figure(figsize=(5, 5))
plt.bar(["Weekday", "Weekend"], [avg_weekday, avg_weekend])
plt.title("Average Daily Steps: Weekday vs Weekend\n(since Aug 2025)")
plt.ylabel("Steps")
plt.tight_layout()

# Save the chart.
plt.savefig("weekday_vs_weekend.png")
plt.close()

print("Saved weekday_vs_weekend.png")