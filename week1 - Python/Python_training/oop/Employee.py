"""Employee Salary calculation"""


class Employee:
    def __init__(self,empid, ename, bp):
        self.empid=empid
        self.ename=ename
        self.bp=bp

    def cal_allowance(self):
        return (self.bp * 0.1)+(self.bp * 0.05)

    def cal_deduction(self):
        return self.bp * 0.03

    def cal_grosspay(self):
        return self.bp + self.cal_allowance()

    def cal_netpay(self):
        return self.cal_grosspay()-self.cal_deduction()
