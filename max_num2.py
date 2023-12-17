numb = input('Enter numbers separated by space:')
numstr = numb.split()
num = []
l = 0

for i in numstr:
    num.append(int(i))
    l += 1
m = num[0]
for i in range(l):
    if num[i] > m:
        m = num[i]

print(m)