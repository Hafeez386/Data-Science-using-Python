"""Python programming: student ages, records, and marks analysis."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ages = [20, 21, 19, 22, 20]
print("Ages of five students:", ages)

data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha", "Usman"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 78, 92, 88, 75],
}
students = pd.DataFrame(data)

print("\nStudent DataFrame:")
print(students)

print("\nFirst three records:")
print(students.head(3))

average_marks = students["Marks"].mean()
print(f"\nAverage marks: {average_marks:.2f}")

high_scorers = students.loc[students["Marks"] > 80, "Name"]
print("\nStudents who scored more than 80:")
print(high_scorers.to_list())
