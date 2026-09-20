import pandas as pd

raw = pd.read_csv("raw_records.csv")
raw["date"] = pd.to_datetime(raw["start_date"]).dt.date

steps_raw = raw[raw["type"] == "HKQuantityTypeIdentifierStepCount"]


readings_per_day = steps_raw.groupby("date").size()


readings_per_day.index = pd.to_datetime(readings_per_day.index)
monthly_avg = readings_per_day.groupby(readings_per_day.index.to_period("M")).mean()
print(monthly_avg)