import os


os.system('clear')

def add(digits):
    total = 0
    for i in digits:
        total += float(i)
    return total

def subtract(digits):
    total = float(digits[0]) - float(digits[1])
    return total

def multiply(digits):
    total = float(digits[0]) * float(digits[1])
    return total

def divide(digits):
    total = float(digits[0]) / float(digits[1])
    return total

q = 'y'

while q == 'y':
    print("\n*****SIMPLE CALCULATIONS(+, -, *, /)*****\n***ONE OPERATION AT A TIME***\n")
    task = input()

    if '+' in task:
        digits = task.split('+')
        print(add(digits))
    elif '-' in task:
        digits = task.split('-')
        print(subtract(digits))
    elif '*' in task:
        digits = task.split('*')
        print(multiply(digits))
    elif '/' in task:
        digits = task.split('/')
        print(divide(digits))
    else:
        print("SYNTHAX ERROR!!!\nInput a basic operation to perform")

    q = input("enter 'y' to do another simple calculation: ").lower()
