
"""Data objects and attribute types using the Adult Income dataset."""

import pandas as pd

column_names = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education_num",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
    "native_country",
    "income",
]

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
adult = pd.read_csv(
    url,
    names=column_names,
    skipinitialspace=True,
    na_values="?",
)

# Identify attribute types
nominal_attributes = [
    "workclass",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "native_country",
]
binary_attributes = ["sex", "income"]
ordinal_attributes = ["education"]
numeric_attributes = [
    "age",
    "fnlwgt",
    "education_num",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
]

print("Nominal attributes:", nominal_attributes)
print("Binary attributes:", binary_attributes)
print("Ordinal attributes:", ordinal_attributes)
print("Numeric attributes:", numeric_attributes)

# Convert Male to 0 and Female to 1
adult["sex"] = adult["sex"].map({"Male": 0, "Female": 1})

# Show each education level and its education_num value once
education_mapping = adult[["education", "education_num"]].drop_duplicates()
education_mapping = education_mapping.sort_values("education_num")
print("\nEducation and education_num:")
print(education_mapping.to_string(index=False))

print(
    "\nEducation is ordinal because its categories have a natural order, "
    "from lower to higher educational attainment."
)
print(
    "education_num is an ordinal code, not a true interval or ratio measure. "
    "The steps between education levels are not equal measurements, and zero "
    "does not mean a complete absence of education."
)

# Replace the race column with one column for each race category
adult = pd.get_dummies(adult, columns=["race"], dtype=int)

print("\nTransformed dataset (first five rows):")
print(adult.head())

# Count unique values in age and fnlwgt
for column in ["age", "fnlwgt"]:
    unique_count = adult[column].nunique()
    print(f"\nUnique values in {column}: {unique_count}")

    if unique_count < 20:
        print("Likely Discrete/Categorical")
    else:
        print("Likely Continuous or High-Cardinality")

# Return all attributes for one person. Row indexes start at 0 in Python.
def get_object_vector(row_index):
    return adult.iloc[row_index]


# The 100th person is at index 99 because Python starts counting at 0.
person_100 = get_object_vector(99)
print("\nComplete attribute vector for the 100th person:")
print(person_100.to_string())
