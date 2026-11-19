import pandas as pd

# Load the CSV file

countries = pd.read_csv("country_gdp_2014.csv")

# Display the first five rows
print("First five rows:")
print(countries.head())

# Display the number of rows and columns
print("\nNumber of rows:", countries.shape[0])
print("Number of columns:", countries.shape[1])

# Display all column names
print("\nColumn names:")
for column in countries.columns:
    print(column)

# Two attributes in the dataset
print("\nTwo attributes:")
print("COUNTRY: The name of a country or territory.")
print("GDP (BILLIONS): The country's GDP in billions of US dollars in 2014.")
