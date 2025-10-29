from oop.College import College

class TeacherDetails(College):
    def __init__(self, ccode, cname, empid, tname, dept, **kwargs):
        super().__init__(ccode, cname, **kwargs)
        self.empid = empid
        self.tname = tname
        self.dept = dept

    def display_teacher(self):
        return f"Teacher ID: {self.empid}, Name: {self.tname}, Dept: {self.dept}"
