
"""Data collection and datafication using students.csv."""

import pandas as pd

# Read the CSV file
students = pd.read_csv("students.csv")

# Display the dataset
print(students)

# Display the number of rows and columns
print("\nNumber of rows:", students.shape[0])
print("Number of columns:", students.shape[1])

# Find missing values in each column
print("\nMissing values in each column:")
print(students.isnull().sum())
