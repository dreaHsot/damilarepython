students_marks = dict()
students_grades = dict()

def mark_to_grade(student_marks):
    for student, mark in student_marks.items():
        if mark >= 91:
            students_grades[student] = 'A+'
        elif mark >= 81:
            students_grades[student] = 'A'
        elif mark >= 71:
            students_grades[student] = 'B+'
        elif mark >= 61:
            students_grades[student] = 'B'
        elif mark >= 51:
            students_grades[student] = 'C'
        elif mark >= 41:
            students_grades[student] = 'D'
        else:
            students_grades[student] = 'F'

    return students_grades

student_no = int(input("What is the total number of students: "))

for i in range(student_no):
    name = input(f"Student {i+1};\nName: ")
    score = int(input("Score: "))
    if score < 0 or score > 100:
        print("Invalid!!")
        score = int(input("Score"))
    else:
        students_marks[name] = score

print(mark_to_grade(students_marks))
