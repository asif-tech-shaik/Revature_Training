class BankDetails:
    def __init__(self, custid, cname, bal):
        self.custid = custid
        self.cname = cname
        self.bal = bal

    def welcome_message(self):
        print("Welcome to Bank")

    def display_details(self):
        print(f'{self.custid} - {self.cname} - {self.bal}')