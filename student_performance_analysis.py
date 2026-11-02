import csv
from collections import Counter
from pathlib import Path


DATA_FILE = Path(__file__).with_name(
    "student_performance_updated_1000-selected-columns.csv"
)


def read_number(row, column):
    """Return a number from a CSV row, or None when the value is missing."""
    try:
        return float(row[column])
    except (KeyError, TypeError, ValueError):
        return None


def average(rows, column):
    """Calculate the average of the valid numbers in a column."""
    values = []
    for row in rows:
        value = read_number(row, column)
        if value is not None:
            values.append(value)
    if not values:
        return None
    return sum(values) / len(values)


def main():
    try:
        with DATA_FILE.open(newline="", encoding="utf-8-sig") as file:
            students = list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Dataset not found: {DATA_FILE}")
        return 1

    if not students:
        print("The dataset is empty.")
        return 1

    categories = Counter(
        (student.get("performance_category") or "").strip() or "Unknown"
        for student in students
    )

    print("Student Performance Analysis")
    print("=" * 30)
    print(f"Students in dataset: {len(students)}")
    print("\nAverage values (missing entries are skipped):")

    for column, label in (
        ("FinalGrade", "Final grade"),
        ("AttendanceRate", "Attendance rate"),
        ("StudyHoursPerWeek", "Study hours per week"),
    ):
        result = average(students, column)
        if result is None:
            print(f"- {label}: no valid values")
        else:
            print(f"- {label}: {result:.1f}")

    print("\nStudents by performance category:")
    for category, count in sorted(categories.items()):
        print(f"- {category}: {count}")

    graded_students = []
    for student in students:
        grade = read_number(student, "FinalGrade")
        if grade is not None:
            graded_students.append((student, grade))
    if graded_students:
        top_student, top_grade = max(
            graded_students, key=lambda item: item[1]
        )
        name = (top_student.get("Name") or "Unknown").strip() or "Unknown"
        print(f"\nHighest final grade: {name} ({top_grade:.1f})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
