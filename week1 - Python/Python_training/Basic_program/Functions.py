

def calculate(m1,m2,m3):
    total=m1+m2+m3
    aveage=total/3
    return total, aveage

sname=input("Enter your first name: ")
m1=int(input("Enter your first number: "))
m2=int(input("Enter your second number: "))
m3=int(input("Enter your third number: "))

total,aveage=calculate(m1,m2,m3)
print(f"name:{sname} Total: {total} average: {aveage}")