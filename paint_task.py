'''1 bucket of paint will cover 7 sq meter space
This code is to calculate the number of paint
buckets needed for a wall depending on the area'''

import math

def multiply(length, breadth):
    return length * breadth

def calc(area, c = 7):
    return math.ceil(area / c)
    
length = int(input("Input the length of the wall: "))
breadth = int(input("Input the breadth of the wall: "))

area = multiply(length, breadth)
total = calc(area)

print(f"Total number of paint buckets needed is {total}")
