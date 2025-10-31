"""Remove Duplicates String"""

strin=input("Enter a String")

remove=''

for char in strin:
    if char not in remove:
        remove+=char

print(remove)
