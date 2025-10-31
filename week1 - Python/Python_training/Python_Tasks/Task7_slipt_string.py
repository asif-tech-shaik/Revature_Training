"""Slipt String"""


strin=input("Enter a string")

input=int(input("Enter the number"))

length=len(strin)

if(length%input!=0):
    print("It can't be divided by it")
else:
    part_leng=length//input
    part=[strin[i:i+part_leng] for i in range(0,length,part_leng)]
    print(part)
