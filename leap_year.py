year = int(input("input year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("is a leap year!")
        else:
            print("is NOT a leap year!")
    else:
        print("is a leap year!")
else:
    print("is NOT a leap year!")