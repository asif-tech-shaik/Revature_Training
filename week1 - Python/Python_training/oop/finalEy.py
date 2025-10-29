from Studexcurr import Studexcurr
from TeacherDetails import TeacherDetails

class FinalEy(Studexcurr, TeacherDetails):
    def __init__(self, ccode, cname, rollno, name, m1, m2, m3,
                 exm1, exm2, empid, tname, dept, feedbackteacher):

        Studexcurr.__init__(self, ccode, cname, rollno, name, m1, m2, m3, exm1, exm2)

        TeacherDetails.__init__(self, ccode, cname, empid, tname, dept)

        self.feedbackteacher = feedbackteacher
