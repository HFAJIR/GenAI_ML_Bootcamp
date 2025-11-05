
#🌟 Exercise 1 : Student Grade Summary

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}


# Calculate averages and letter grades in one loop
student_averages = {}
student_letter_grades = {}

# Calculate average grades and create summary dictionary
for student, grades in student_grades.items():
    average = round(sum(grades) / len(grades), 2)
    student_averages[student] = average
    
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    
    student_letter_grades[student] = letter_grade

# Calculate the class average
total_average = round(sum(student_averages.values()) / len(student_averages), 2)
# Display the results
print("Student Averages:", student_averages)
print("Student Letter Grades:", student_letter_grades)
print("Class Average:", total_average)
