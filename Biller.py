import random

billables = []
print("Enter the names of billables, then press enter\nPress enter twice at the last name:")

index = 1
name = input(str(index) + ':')
while name:
    index +=1
    billables.append(name)
    name = input(str(index) + ":")

random.shuffle(billables)
chosen = random.choice(billables)
chosen2 = billables[0]

print(billables)
print("The chosen person is: " + chosen)
print("Another chosen person is: " + chosen2)