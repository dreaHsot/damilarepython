heights = input("Enter heights separated by a comma:")
heights_list = heights.split(',')
print(heights_list)
n = 0
total = 0

for i in heights_list:
    n += 1
    total += int(i)
print(round(total / n))