#sum of digits
number=int(input("Enter a number: "))
sum=0

while number>0:
    digit=number % 10               # % remainder : for extracting last digit
    sum= sum+digit                  
    number=number//10               # // integer division : for removing last digit
print("Sum of digits:", sum)

#Reverse a number
number=int(input("Enter a number: "))
reverse=0

while number>0:
    digit=number % 10
    reverse=reverse * 10 + digit
    number=number//10
print("Reverse a number:", reverse)

#Palindrome 
number=int(input("Enter a number :" ))
original=number
reverse=0
while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
if original==reverse:
    print("YES it is palindrome")
else:
    print("NO not a palindrome")

#Count the digits
number=int(input("Enter a number:"))
number = abs(number)       #To support negative integers too, use abs():
count=0
if number==0:
    count=1
else:
    while number>0:
        number=number//10
        count=count+1
print("Count of the digits:", count)

# Factorial of a number
number = int(input("Enter a number:"))
fact = 1

for i in range(1, number + 1):
    fact = fact * i

print("Factorial is:", fact)

#Input: num = 38    Output: 2
#Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2     
# Since 2 has only one digit, return it.

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum = 0

            while num > 0:
                digit = num % 10
                sum = sum + digit
                num = num // 10
            
            num = sum
        return num