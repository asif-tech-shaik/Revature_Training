
from oop.College import College

class StudentDet(College):
    def __init__(self,ccode, cname, srollno, sname, m1, m2, m3):
        super().__init__(ccode, cname)
        self.__srollno = srollno
        self.__sname = sname
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3

    @property
    def sname(self):
        return self.__sname

    @sname.setter
    def sname(self,name):
        self.__sname = name

    @property
    def srollno(self):
        return self.__srollno

    @srollno.setter
    def srollno(self,rollno):
        self.__srollno = rollno

    def cal_tat(self):
        return self.__m1 + self.__m2 + self.__m3

    def cal_avg(self):
        return self.cal_tat() / 3
