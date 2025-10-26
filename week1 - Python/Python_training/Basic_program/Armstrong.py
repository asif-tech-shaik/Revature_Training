'''
date: 25-10-2025
Author: Mohammmad Asif Shaik
DESC: Armstrong number
'''


numstr=input("Enter a number: ")
numlen=len(numstr)
num=int(numstr)
temp=num
sum=0
while(num>0):
    rem=num%10
    sum+=rem**numlen
    num//=10

if temp==sum:
    print('Armstrong number')
else:
    print('Not a Armstrong number')