
num=int(input('Enter a number: '))

num1=1
for i in range(1,num+1):
    for j in range(i):
        print(num1,end=' ')
        num1+=1
    print()
