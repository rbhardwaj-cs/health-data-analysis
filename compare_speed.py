import pandas as pd

daily = pd.read_csv(
    "daily_summary.csv",
    index_col="date",
    parse_dates=True
)

speed = daily["HKQuantityTypeIdentifierWalkingSpeed"].sort_index()

move_date = pd.Timestamp("2025-08-18")
window = pd.Timedelta(days=60)

# Select equal-length periods with no overlap.
before = speed[
    (speed.index >= move_date - window)
    & (speed.index < move_date)
]

after = speed[
    (speed.index >= move_date)
    & (speed.index < move_date + window)
]

# Average the available daily values; missing values are ignored.
avg_before = before.mean()
avg_after = after.mean()

print(f"Before move: {before.count()} non-missing days out of 60")
print(f"After move:  {after.count()} non-missing days out of 60")
print(f"Average speed before: {avg_before:.3f}")
print(f"Average speed after:  {avg_after:.3f}")

if pd.notna(avg_before) and pd.notna(avg_after) and avg_before != 0:
    percent_change = (avg_after - avg_before) / avg_before * 100
    print(f"Change in average walking speed: {percent_change:+.2f}%")
else:
    print("Cannot calculate percentage change: missing data or zero baseline.")