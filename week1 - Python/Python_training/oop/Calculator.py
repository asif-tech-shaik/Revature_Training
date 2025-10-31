from AddCalculation import AddCalculation
from oop.AgeNotEnoughError import AgeNotEnoughError

n1=int(input('Enter a number: '))
n2=int(input('Enter another number: '))
age=int(input('Enter age: '))

cal=AddCalculation(n1,n2)
try:
 print(f'{cal.add()}')
 print(f'{cal.sub()}')
 print(f'{cal.mul()}')
 res=cal.div()
 if age<18:
     raise AgeNotEnoughError('You are Minor')
except ZeroDivisionError:
    print('0 in denominator')
except IndexError:
    print('Index not available')
except AgeNotEnoughError:
    print("you are minor")
else:
    print(res)
finally:
    print('Done')


