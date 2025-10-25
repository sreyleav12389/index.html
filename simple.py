# Big Python example: simple student grading system

# Function to calculate grade
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# List of students and their scores
students = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 68,
    "David": 74,
    "Eva": 58
}

# Loop through students and print their grades
for name, score in students.items():
    grade = calculate_grade(score)
    print(f"{name}: Score = {score}, Grade = {grade}")

# Bonus: calculate class average
total_score = sum(students.values())
average_score = total_score / len(students)
print(f"\nClass Average: {average_score:.2f}")
