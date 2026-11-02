
import pandas as pd

columns = [
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
print("Loading dataset for Task 4...")
df = pd.read_csv(url, names=columns, header=None, sep=",\\s+", engine="python")

print("=== Task 4: Attribute Vector Extraction ===")


def get_object_vector(row_index):
  """Returns all features for a specific individual (row) in the dataset."""
  if 0 <= row_index < len(df):
    return df.iloc[row_index]
  else:
    return "Error: Row index out of bounds!"



person_100 = get_object_vector(99)
print("Attribute Vector for the 100th person (Row Index 99):")
print(person_100)