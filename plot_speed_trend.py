import pandas as pd
import matplotlib.pyplot as plt

# Read the data and sort dates into chronological order.
daily = pd.read_csv("daily_summary.csv", index_col="date", parse_dates=True)
daily = daily.sort_index()

# Select walking speed.
speed = daily["HKQuantityTypeIdentifierWalkingSpeed"]

# Calculate the average over the current row and previous 29 rows.
speed_smoothed = speed.rolling(window=30).mean()

plt.figure(figsize=(12, 5))
plt.plot(
    speed.index, speed,
    alpha=0.2, linewidth=0.8, label="Daily (raw)"
)
plt.plot(
    speed_smoothed.index, speed_smoothed,
    linewidth=2, label="30-day rolling average"
)
plt.title("Walking Speed Over Time")
plt.xlabel("Date")
plt.ylabel("Walking Speed")
plt.axvline(
    pd.Timestamp("2025-08-18"),
    color="red",
    linestyle="--",
    label="Moved to campus"
)
plt.legend()
plt.tight_layout()
plt.savefig("speed_trend.png")
plt.close()

print("Saved speed_trend.png")