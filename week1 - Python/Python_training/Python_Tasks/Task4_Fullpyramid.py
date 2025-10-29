"""full Pyramid """

num=int(input("Enter a number: "))

for i in range(1,num+1):
    for space in range(1,num-i+1):
        print(end=' ')
    for star in range(1,i+1):
        print('*',end=' ')
    print(' ')

