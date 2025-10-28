"""Employee Salary Calculator"""

from oop.Employee import Employee

empid=int(input("Enter Employee ID: "))
ename=input("Enter Employee Name: ")
bp=float(input("Enter Employee Basic pay: "))

employee = Employee(empid, ename, bp)

print(f'Emp id: {empid} \nName: {ename} \nGross pay: {employee.cal_grosspay()} \n'
      f'Net pay: {employee.cal_netpay()}' )
