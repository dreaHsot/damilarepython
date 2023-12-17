height_list = []
n = 1
sum_height = 0

print("input height and press enter at each input;\ndouble press enter at the last height")

heights = input("Height " + str(n) + ":")
#int_heights = (heights)

while heights:
    height_list.append(heights)
    n += 1
    heights = input("Height " + str(n) + ":")
    #int_heights = (heights)

print(height_list)

for heights in height_list:
    h = float(heights)
    #2
    # print(type(h))
    sum_height += h

average_height = sum_height / (n - 1)

print(f'Average height = {average_height}')