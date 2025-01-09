'''
student_grades = {'Ram': 85, 'Sham': 92, 'Ojas’': 88, 'Anay': 79}
#Find the student with the highest grade
top_student = max(student_grades, key=student_grades.get)
print(f"The student with the highest grade is {top_student} with a grade of {student_grades[top_student]}.")

#Add a new student 'Eve' with a grade of 95
student_grades['Eve'] = 95
print(student_grades)
print()

# 3. Print all students' names and grades in alphabetical order
print("Students and their grades in alphabetical order:")
for student in sorted(student_grades):
    print(f"{student}: {student_grades[student]}")


'''
# Initial dictionary of student grades
'''
student_grades = {'Ram': 85, 'Sham': 92, 'Ojas': 88, 'Anay': 79}

# 1. Find the student with the highest grade without using max()
top_student = None
highest_grade = -1
for student, grade in student_grades.items():
    if grade > highest_grade:
        highest_grade = grade
        top_student = student

print(f"The student with the highest grade is {top_student} with a grade of {highest_grade}.")

# 2. Add a new student 'Eve' with a grade of 95
student_grades['Eve'] = 95

# 3. Sort student names manually (Bubble Sort) and print them in alphabetical order
student_names = list(student_grades.keys())

# Bubble Sort
for i in range(len(student_names) - 1):
    for j in range(len(student_names) - i - 1):
        if student_names[j] > student_names[j + 1]:
            # Swap if the current name is greater than the next name
            student_names[j], student_names[j + 1] = student_names[j + 1], student_names[j]

# Print students' names and grades in alphabetical order
print("Students and their grades in alphabetical order:")
for student in student_names:
    print(f"{student}: {student_grades[student]}")
'''

#3rd approach
student_grades = {'Zoya': 99,'Ram': 85, 'Sham': 92, 'Ojas': 88, 'Anay': 79}

# Sort the dictionary by grades and store as a list of tuples
sorted_grades = sorted(student_grades.items(), key=lambda item: item[1])
# Print each student and their grade in ascending order
for name, grade in sorted_grades:
    print(f"{name}: {grade}")
# Print the student with the highest grade, which is the last item in sorted_grades
highest_student, highest_grade = sorted_grades[-1]
print(f"The student with the highest grade is: {highest_student} with a grade of {highest_grade}")

#Add a new student 'Eve' with a grade of 95
student_grades['Eve'] = 95

# Sort the dictionary by names and store as a list of tuples
sorted_grades = sorted(student_grades.items(), key=lambda item: item[0])
print("Students and their grades in alphabetical order:")
# Print each student name is alphabetical order
for name, grade in sorted_grades:
    print(f"{name}: {grade}")

'''
print()
fruits={'apple':23,'mango':34, 'cherry':233}
basket=(fruits.items())
print(basket)
basket=sorted(basket, key=lambda item: item[1], reverse=True)
for fruit,price in basket:
    print(f"{fruit}: {price}")
fname,fprice =basket[0]
print(f"Fruit with highest price is:{fname}[{fprice}]")

'''