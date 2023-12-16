bill = 0

size = input('Enter\n\n"S" for small pizza\n"M" for medium\nor\n"L" for Large\n')

if size == "m" or size == "M":
    bill = 200
elif size == "l" or size == "L":
    bill = 300
elif size == "s" or size == "S":
    bill = 100
else:
    print("wrong input!!!")

pepperoni = input("Pepperoni?(Y/N)")
if pepperoni == "y" or pepperoni == "Y":
    if bill == 100:
        bill += 30
    elif bill == 200 or bill == 300:
        bill += 50
elif pepperoni == "n" or pepperoni == "N":
    bill = bill
else:
    print('kindly enter "Y" or "N" for Yes or No')

cheese = input("Extra cheese?(Y/N)")
if cheese == "y" or cheese == "Y":
    bill += 20
elif cheese == "n" or cheese == "N":
    bill = bill
else:
    print('kindly enter "Y" or "N" for Yes or No')


print(f"Your bill is #{bill}")

#if size == "m" or size == "M" or size == "l" or size == "L":
