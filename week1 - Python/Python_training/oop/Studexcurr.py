from StudentDet import StudentDet

class Studexcurr(StudentDet):
    def __init__(self, ccode, cname, rollno, name, m1, m2, m3, exm1, exm2, **kwargs):
        super().__init__(ccode, cname, rollno, name, m1, m2, m3, **kwargs)
        self.exm1 = exm1
        self.exm2 = exm2

    def cal_ext(self):
        return self.exm1 + self.exm2
