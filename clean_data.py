import pandas as pd

# 1. Load the individual records
df = pd.read_csv("raw_records.csv")

# 2. Convert values to numbers; invalid entries become NaN
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# 3. Extract the calendar date from each timestamp
df["date"] = pd.to_datetime(df["start_date"]).dt.date

# 4. Choose how to summarize each measurement
SUM_TYPES = {
    "HKQuantityTypeIdentifierStepCount",
    "HKQuantityTypeIdentifierDistanceWalkingRunning",
    "HKQuantityTypeIdentifierActiveEnergyBurned",
    "HKQuantityTypeIdentifierBasalEnergyBurned",
}

MEAN_TYPES = {
    "HKQuantityTypeIdentifierWalkingSpeed",
    "HKQuantityTypeIdentifierWalkingStepLength",
}

# 5. Calculate daily totals
# min_count=1 preserves NaN when a group has no valid values
daily_sums = (
    df[df["type"].isin(SUM_TYPES)]
    .groupby(["date", "type"])["value"]
    .sum(min_count=1)
)

# 6. Calculate daily averages, skipping missing values
daily_means = (
    df[df["type"].isin(MEAN_TYPES)]
    .groupby(["date", "type"])["value"]
    .mean()
)

# 7. Combine the summaries and turn the index into columns
daily = pd.concat([daily_sums, daily_means]).reset_index()

# 8. Create one row per date and one column per measurement
wide = daily.pivot(
    index="date",
    columns="type",
    values="value",
).sort_index()

# 8b. Reindex to a complete daily calendar. pivot() only creates a row for
# a date if at least one reading exists that day - a date with ZERO readings
# of any type is silently absent, not just missing values within a row.
# Reindexing makes those dates show up explicitly as NaN rows instead.
wide.index = pd.to_datetime(wide.index)
full_calendar = pd.date_range(wide.index.min(), wide.index.max(), freq="D")
wide = wide.reindex(full_calendar)
wide.index.name = "date"

# 9. Save the table, including the date index
wide.to_csv("daily_summary.csv")

# 10. Preview the first five rows and report the number of days
print(wide.head())
print(f"\n{len(wide)} days of data")