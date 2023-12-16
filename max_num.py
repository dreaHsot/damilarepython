num_list = []

numbers = input('Enter list of numbers separated by space:')
num = numbers.split()
numit = []
print(num)
for i in num:
    numit.append(int(i))
print(numit)

n = 1
m = numit[0]
l = len(numit)
while n != l:
    if m < numit[n]:
        m = numit[n]
    n += 1

print(m)