import pandas as pd


url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Missing values per column
print("Missing values per column:\n", df.isnull().sum())

# Total missing values in the entire dataset
print("\nTotal missing values in dataset:", df.isnull().sum().sum())