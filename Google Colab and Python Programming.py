
"""Google Colab setup and Python programming exercise."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


student_ages = [20, 21, 19, 22, 20]
print("Student ages:", student_ages)

students = pd.DataFrame(
    {
        "Name": ["Ali", "Ahmed", "Sara", "Ayesha", "Usman"],
        "Age": [20, 21, 19, 22, 20],
        "Marks": [85, 78, 92, 88, 75],
    }
)

print("\nStudent records:")
print(students)

print("\nFirst three records:")
print(students.head(3))

print("\nAverage marks:", students["Marks"].mean())

print("\nStudents with marks greater than 80:")
print(students.loc[students["Marks"] > 80, "Name"].to_list())
