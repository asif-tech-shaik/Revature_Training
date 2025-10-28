"""desc: Prime number"""

def prime_number(number):
    if number<1:
        return False
    for i in range(2,number):
        if(number%i==0):
            return False
    return True

start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))

for i in range(start,end+1):
    if(prime_number(i)):
        print(i)