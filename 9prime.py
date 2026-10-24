# Check for prime number
num = int(input("Enter the number: "))

if num < 2:
    print("Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Yes, Prime Number")


# Factors of a number
num = int(input("Enter the number: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")