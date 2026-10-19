#Palindrome string 
# if else condition
text=input("Enter a string:")
reverse=(text[::-1])

if text==reverse:
    print("YES It is Palindrome")
else:
    print("NOt a Palindrome")
    
#using loop
text=input("Enter a string:")
reverse=""
for i in range(len(text)-1,-1,-1):
    reverse=reverse+text[i]
if text==reverse:
    print("YES It is Palindrome")
else:
    print("NOt a Palindrome")
    