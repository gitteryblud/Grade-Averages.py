def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Input
student_name = input("Enter student name: ")
# Ask for 5 grades without using loops
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
grade4 = float(input("Enter grade 4: "))
grade5 = float(input("Enter grade 5: "))

# Store grades in a list
grades = [grade1, grade2, grade3, grade4, grade5]

# Calculate average without using loops
average = sum(grades) / len(grades)

# Determine letter grade using function
letter_grade = get_letter_grade(average)

# Output
print(student_name)
print(f"Average: {average}")
print(f"Letter grade: {letter_grade}")
