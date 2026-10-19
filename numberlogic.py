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

#factorial of number
number=int(input("Enter a number:"))
fact=1
for i in range(1,number+1):
    fact=fact*i
print("Factorial is:", fact)