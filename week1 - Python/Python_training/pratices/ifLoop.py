"""If Loop pratices"""

input1=int(input('Enter a number: '))

if input1>=18 and input1<=100:
    print('your old to sign up')
elif input1<=0:
    print('your born yet')
elif input1>=101:
    print('your born too old to sign up')
else:
    print('your not old to sign up')

