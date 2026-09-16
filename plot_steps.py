import matplotlib.pyplot as plt
import pandas as pd

daily = pd.read_csv("daily_summary.csv", index_col="date", parse_dates=True)

plt.figure(figsize=(12, 5))

plt.plot(daily.index, daily["HKQuantityTypeIdentifierStepCount"])

plt.title("Daily Step Count Over Time")
plt.xlabel("Date")
plt.ylabel("Steps")
plt.tight_layout()
plt.savefig("daily_steps.png")
print("Saved daily_steps.png")