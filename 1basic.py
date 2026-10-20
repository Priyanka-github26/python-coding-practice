name="priyanka"
age=21
print(name)
print(age)

#Add of 2 numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=a+b
print("The sum of", a, "and", b, "is:", c)

#even or odd
num=int(input("Enter a number"))
if num%2==0:
    print("Even")
else:
    print("Odd")
    
#find largest of 3 numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a>b and a>c:
    print("a is largest number ")
elif b>a and b>c:
    print("b is largest number")
else:
    print("c is largest num")
    
#Multiplication table from 1 to 10
num=int(input("Enter the number:"))
for i in range(1,11):
    print(num,"x", i, "=" , num*i)
    

#Leetcode problem 2235 Add 2 integers
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2