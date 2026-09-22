import pandas as pd
import matplotlib.pyplot as plt

# Read the data and sort it by date.
daily = pd.read_csv("daily_summary.csv", index_col="date", parse_dates=True)
daily = daily.sort_index()

distance = daily["HKQuantityTypeIdentifierDistanceWalkingRunning"]
energy = daily["HKQuantityTypeIdentifierActiveEnergyBurned"]

# Calculate rolling averages over 30 rows.
distance_smoothed = distance.rolling(window=30).mean()
energy_smoothed = energy.rolling(window=30).mean()

# Create two stacked panels with a shared date axis.
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(12, 8), sharex=True)

trip_start = pd.Timestamp("2026-05-10")  # left for India
trip_end = pd.Timestamp("2026-08-23")    # returned to USF

# Top panel: walking/running distance.
ax[0].plot(
    distance.index, distance,
    alpha=0.2, linewidth=0.8, label="Daily (raw)"
)
ax[0].plot(
    distance_smoothed.index, distance_smoothed,
    linewidth=2, label="30-day rolling average"
)
ax[0].set_title("Walking and Running Distance Over Time")
ax[0].set_ylabel("Distance (mi)")
ax[0].axvline(trip_start, color="red", linestyle="--", label="Left for India")
ax[0].axvline(trip_end, color="green", linestyle="--", label="Returned to USF")
ax[0].legend()

# Bottom panel: active energy burned.
ax[1].plot(
    energy.index, energy,
    alpha=0.2, linewidth=0.8, label="Daily (raw)"
)
ax[1].plot(
    energy_smoothed.index, energy_smoothed,
    linewidth=2, label="30-day rolling average"
)
ax[1].set_title("Active Energy Burned Over Time")
ax[1].set_ylabel("Active Energy (Cal)")
ax[1].set_xlabel("Date")
ax[1].axvline(trip_start, color="red", linestyle="--", label="Left for India")
ax[1].axvline(trip_end, color="green", linestyle="--", label="Returned to USF")
ax[1].legend()

# Save both panels in one image.
fig.tight_layout()
fig.savefig("distance_energy_trend.png")
plt.close(fig)

print("Saved distance_energy_trend.png")
