'''This simple code checks if any given
number is a prime number or not'''

num = int(input("Enter a natural number: "))

if num < 1:
    print(f"{num} is not a natural number")
elif num == 1:
    print("1 is not a prime number")
else:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            print(f"It is divisible by {i}")
            break
    else:
        print(f"{num} is a prime number")
