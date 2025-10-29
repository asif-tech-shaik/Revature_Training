"""Pascal's Triangle"""

num=int(input("Enter a number: "))

for i in range(num):
    for space in range(num-i-1):
        print(' ',end='')
    number=1
    for j in range(i+1):
        print(number,end=' ')
        number = number * (i - j) // (j + 1)
    print()