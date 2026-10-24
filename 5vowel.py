#Count Vowels
text = input("Enter a string:")
count=0
for ch in text.lower():
    if ch in "aeiou":
        count+=1
    print("No. of vowels:", count)
    
#Count Vowels and Consonants

text = input("Enter a string: ")
vowels = 0
consonants = 0

for ch in text.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("No. of vowels:", vowels)
print("No. of consonants:", consonants)
