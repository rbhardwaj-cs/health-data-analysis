# Apple Health Data Analysis

Cleaning and analyzing 3+ years of my own Apple Health data — steps, distance, energy burned, and walking-quality metrics — to see what my real activity patterns actually look like, and to practice building a real data pipeline from a messy, real-world file.


## What this does

Turns a raw Apple Health export (`export.xml`, 179MB, 4M+ lines) into clean, analyzable daily data:

1. **`extract_data.py`** — streams through the 179MB XML file line-by-line (never loading the whole thing into memory) and pulls out the six health metrics this project focuses on, writing them to `raw_records.csv` (337,072 individual readings).
2. **`clean_data.py`** — aggregates those readings into one row per day (`daily_summary.csv`, 1,254 days), using `sum` for cumulative metrics (steps, distance, energy burned) and `mean` for rate metrics (walking speed, step length) — and explicitly preserves "no data that day" as missing rather than a misleading `0`.
3. **`plot_steps.py`** — visualizes daily step count over the full time range.

## Tech used

Python, `re` (regex), `pandas`, `matplotlib`, git/GitHub.

## Project structure

```
health-data-analysis/
├── extract_data.py       # XML -> raw_records.csv
├── clean_data.py         # raw_records.csv -> daily_summary.csv
├── plot_steps.py         # daily_summary.csv -> daily_steps.png
├── daily_summary.csv     # cleaned daily data (committed — aggregated, not raw)
├── daily_steps.png       # first visualization
├── .gitignore            # excludes the raw export (size + personal-data privacy)
└── README.md
```

## Setup & usage

```bash
pip install pandas matplotlib
```

Get your own export: iPhone Health app → profile icon → **Export All Health Data**, unzip it, place `export.xml` in this folder. Then run the pipeline in order:

```bash
python3 extract_data.py   # -> raw_records.csv
python3 clean_data.py     # -> daily_summary.csv
python3 plot_steps.py     # -> daily_steps.png
```

## What I found so far

Daily step count shows a clear, sustained shift starting around mid-2025 — before that, tracking is sparse and patchy (large gaps, mostly under 10K steps/day); after it, tracking is dense and consistently higher (mostly 10K–20K+ steps/day).



The honest interpretation: this is likely **both** a real behavior change (more walking as a college student) **and** a change in tracking consistency (the data source shifts to a personal iPhone right around the same time) happening together — the data alone can't fully separate the two effects, and I'm not claiming more than it shows.

## Data & privacy

`export.xml` and `raw_records.csv` are intentionally excluded from this repo (see `.gitignore`) for two reasons: they're large (179MB / 25MB), and they contain real personal health data at a fine-grained, timestamped level. `daily_summary.csv` — aggregated to daily totals — is committed, since I'm comfortable sharing that level of detail publicly.

## Limitations

- No Apple Watch data in this export — no heart rate or sleep data, only iPhone motion-sensor metrics (steps, distance, walking quality).
- Pre-mid-2025 data is sparse enough that conclusions drawn from that period alone should be treated with real skepticism.
- This is one person's data — not meant to generalize beyond my own patterns.

## What's next

- Restrict analysis to the reliably-tracked period and compare weekday vs. weekend activity.
- Explore the walking-quality metrics (speed, step length) rather than just step counts.
- More visualizations, and a clearer write-up of findings.

## Lessons learned

Memory-efficient file reading matters once "large file" stops being theoretical — 179MB is small enough to get away with sloppy habits, but the pattern (stream, don't load-all) is the one that scales. Also: a chart with a caveat you can defend is worth more than a chart with a confident claim you can't.
