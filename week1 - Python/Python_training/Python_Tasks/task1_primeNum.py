"""desc: Prime number"""

def prime_number(n):
    if n<=1:
       return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))

for i in range(start,end+1):
    if prime_number(i):
        print(i)