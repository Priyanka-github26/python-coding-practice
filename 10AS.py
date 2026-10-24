#ARMSTRONG Problem
num = int(input("Enter a number: "))

temp = num
total = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#Code	             Meaning
#temp % 10	       Extracts the last digit
#digit ** digits   Raises the digit to the required power
#temp // 10	       Removes the last digit
#total == num	   Checks whether the calculated sum matches the original number

