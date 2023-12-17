list1 = [1,1,1]
list2 = [1,1,1]
list3 = [1,1,1]

matrix = [list1, list2, list3]

print(f"{list1}\n{list2}\n{list3}")

ab = int(input("Enter a 2 digits that represents row and column:"))

a = ab // 10
b = ab % 10

if a == 1:
    if b == 1:
        matrix[0][0] = 'X'
    elif b == 2:
        matrix[0][1] = 'X'
    elif b == 3:
        matrix[0][2] = 'X'
    else:
        print("...THIS IS A 3 BY 3 MATRIX...")
elif a == 2:
    if b == 1:
        matrix[1][0] = 'X'
    elif b == 2:
        matrix[1][1] = 'X'
    elif b == 3:
        matrix[1][2] = 'X'
    else:
        print("...THIS IS A 3 BY 3 MATRIX...")
elif a == 3:
    if b == 1:
        matrix[2][0] = 'X'
    elif b == 2:
        matrix[2][1] = 'X'
    elif b == 3:
        matrix[2][2] = 'X'
    else:
        print("...THIS IS A 3 BY 3 MATRIX...")
else:
    print("\nERROR...THIS IS A 3 BY 3 MATRIX...\n")

print(f"{list1}\n{list2}\n{list3}")