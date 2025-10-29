
from StudentDet import StudentDet
from TeacherDetails import TeacherDetails
from finalEy import FinalEy

ccode=input('Enter ccode: ')
cname=input('Enter name: ')
rollno = int(input('Roll no: '))
name = input('Name ')
m1 = int(input('mark 1: '))
m2 = int(input('mark 2: '))
m3 = int(input('mark 3: '))

exm1=int(input('exam 1: '))
exm2=int(input('exam 2: '))

'''stud=StudentDet(ccode,cname,rollno,name,m1,m2,m3)
print(f'{stud.display()}')
print(f'\n{stud.srollno} \n{stud.sname}'
      f'\n{stud.cal_tat()} \n{stud.cal_avg()}')'''

empid=int(input('Enter emp id: '))
tname=input('Enter tname: ')
dept=input('Enter dept: ')

'''teacher=TeacherDetails(ccode,cname,empid,tname,dept)
teacher.display()'''

feedbackteacher=input('Enter feedback teacher: ')

finalEy=FinalEy(ccode,cname,rollno,name,m1,m2,m3,exm1,exm2,empid,tname,dept,feedbackteacher)

print(f'{finalEy.display()}\n'
      f'{finalEy.display()[0]}\t{finalEy.display()[1]}'
      f'\n{finalEy.srollno} \n{finalEy.sname}'
      f'\n{finalEy.cal_tat()} \n{finalEy.cal_avg()}'
      f'\n{finalEy.display()}'
      f'\n{finalEy.feedbackteacher}')

