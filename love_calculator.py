lovers_name_1 = input("Enter thr names of lovers below;\nName 1:")
lovers_name_2 = input("Name 2:")

both_names = lovers_name_1.lower() + lovers_name_2.lower()
a = (both_names.count("t"))
a += (both_names.count("r"))
a += (both_names.count("u"))
a += (both_names.count("e"))

b = (both_names.count("l"))
b += (both_names.count("o"))
b += (both_names.count("v"))
b += (both_names.count("e"))

a = str(a)
b = str(b)

c = a + b
if (a != '0'):
    love_percent = c + '%'
else:
    love_percent = b + '%'

print("The Love percentage here is",love_percent)

int_c = int(c)

