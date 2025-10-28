
from StudentDet import StudentDet

ccode=input('Enter ccode: ')
cname=input('Enter name: ')
rollno = int(input('Roll no: '))
name = input('Name ')
m1 = int(input('mark 1: '))
m2 = int(input('mark 2: '))
m3 = int(input('mark 3: '))

stud=StudentDet(ccode,cname,rollno,name,m1,m2,m3)
print(f'{stud.display()}')
print(f'\n{stud.srollno} \n{stud.sname}'
      f'\n{stud.cal_tat()} \n{stud.cal_avg()}')
