"""Palindrome"""

input=input("Enter a number: ")

revserve=input[::-1]

print(revserve)
if(input==revserve):
    print("Palindrome")
else:
    print("Not Palindrome")