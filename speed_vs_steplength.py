import pandas as pd
import matplotlib.pyplot as plt

daily = pd.read_csv("daily_summary.csv", index_col="date", parse_dates=True)

speed = daily["HKQuantityTypeIdentifierWalkingSpeed"]
step_length = daily["HKQuantityTypeIdentifierWalkingStepLength"]

# Calculate the correlation between walking speed and step length.
correlation = speed.corr(step_length)

print(f"Correlation between walking speed and step length: {correlation:.3f}")

# Plot step length on the x-axis and walking speed on the y-axis.
plt.figure(figsize=(6, 6))
plt.scatter(step_length, speed, alpha=0.3, s=10)
plt.title("Walking Speed vs. Step Length")
plt.xlabel("Step Length")
plt.ylabel("Walking Speed")
plt.tight_layout()
plt.savefig("speed_vs_steplength.png")
plt.close()

print("Saved speed_vs_steplength.png")