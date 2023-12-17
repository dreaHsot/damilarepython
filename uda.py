names = input("Enter names separated by space:").title().split()
assignments = input("Enter the number of missing assignments:").split()
grades = input("what are the grades? seperated by space:").split()

if (len(names) != len(assignments)) or (len(grades) != len(names)):
    print("error!! kindly align the number of each items inputed...")

for i in range(0,len(names)):
    potential_grade = int(grades[i]) + (2 * int(assignments[i]))

    print(f"Hi {names[i]},\n\nThis is a reminder that you have {assignments[i]} assignments left before you graduate. Your current grade is {grades[i]} and can increase to {potential_grade} if you submit all assignments before the due date.\n\n")
