""" Vowel check"""

input=input("Enter a number: ")

vowel='aeiouAEIOU'

count=0
for char in input:
    if char in vowel:
        print(char)
        count+=1

print(count)
