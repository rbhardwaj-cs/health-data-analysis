import pandas as pd

# Read the CSV and use dates as the row labels.
daily = pd.read_csv("daily_summary.csv", index_col="date", parse_dates=True)

# Select the step-count column.
steps = daily["HKQuantityTypeIdentifierStepCount"]

# Group the step counts by calendar month.
monthly = steps.groupby(steps.index.to_period("M"))

# Calculate the percentage of non-missing values in one month.
def calculate_completeness(group):
    return group.count() / len(group) * 100

# Run the function on each month's group.
completeness = monthly.apply(calculate_completeness)

print(completeness)