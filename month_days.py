def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("YEAR: "))
month = int(input("MONTH(from 1 - 12): "))
mnt_30 = [4, 6, 9, 11]

if month > 12:
    print("WRONG INPUT!!")

if leap_year(year) and month == 2:
    print("Number of days = 29")
elif not leap_year(year) and month == 2:
    print("Number of days = 28")
else:
    if month in mnt_30:
        print("Number of days = 30")
    else:
        print("Number of days = 31")
