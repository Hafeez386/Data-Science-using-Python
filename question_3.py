import pandas as pd

# Load the Adult Income dataset
adult_df = pd.read_csv("adult.csv")

# Task A: Load and inspect the dataset
print("First five records:")
print(adult_df.head())

# Task B: Convert gender to numbers
adult_df["gender"] = adult_df["gender"].map({"Male": 0, "Female": 1})

race_columns = pd.get_dummies(adult_df["race"], prefix="race", dtype=int)
adult_df = pd.concat([adult_df.drop("race", axis=1), race_columns], axis=1)

print("\nTransformed gender and race columns:")
columns_to_display = ["gender"] + race_columns.columns.tolist()
print(adult_df[columns_to_display].head())

# Task C: Display education levels and their education numbers
print("\nEducation levels and their corresponding educational-num:")
education_levels = adult_df[["education", "educational-num"]].drop_duplicates()
education_levels = education_levels.sort_values("educational-num")
print(education_levels.to_string(index=False))

# Task D: Count unique values and classify each attribute
age_unique_count = adult_df["age"].nunique()
fnlwgt_unique_count = adult_df["fnlwgt"].nunique()

print("\nUnique age values:", age_unique_count)
if age_unique_count < 20:
    print("Age: likely discrete/categorical")
else:
    print("Age: likely continuous/high cardinality")

print("\nUnique fnlwgt values:", fnlwgt_unique_count)
if fnlwgt_unique_count < 20:
    print("fnlwgt: likely discrete/categorical")
else:
    print("fnlwgt: likely continuous/high cardinality")

# Task E: Return all attribute values for one individual
def get_object_vecter(row_index):
    return adult_df.iloc[row_index]


print("\nAttribute vector for the 100th individual (index 99):")
print(get_object_vecter(99))
