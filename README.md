# Cleaning Data

Python data science lab exercises and sample datasets for loading, inspecting,
cleaning, and extracting information from data.

## Data exercises

```powershell
python -m pip install pandas
python task2.py
python lab2.py
```

`task2.py` reports missing values in a Washington State dataset downloaded
when the script runs. `lab2.py` loads the UCI Adult dataset and prints the
attributes for its 100th row.

The CSV and SQLite files in this repository are accompanying lab datasets and
examples.

## Student performance analysis

`student_performance_analysis.py` summarizes student grades, attendance, study
hours, and performance categories using only Python's standard library. Run it
with:

```powershell
python student_performance_analysis.py
```

The script skips missing numeric values when calculating averages and reports
students with an unknown performance category separately.
