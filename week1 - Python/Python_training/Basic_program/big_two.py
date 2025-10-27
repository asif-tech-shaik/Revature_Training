"""DESC: Biggest of 2 Numbers"""

number1=int(input("Enter a number: "))
number2=int(input("Enter another number: "))

if number1==number2:
    print('Both numbers are equal')
elif number1>number2:
    print(f'{number1} is greater than {number2}')
else:
    print(f'{number2} is greater than {number1}')
