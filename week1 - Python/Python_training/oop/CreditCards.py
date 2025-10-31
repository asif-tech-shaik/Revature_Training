from typing import final

from Bankdetails import BankDetails

class CreditCard(BankDetails):
    def __init__(self, custid, cname, bal, creditscore, status):
        super().__init__(custid, cname, bal)
        self.creditscore = creditscore
        self.status = status

    def welcome_message(self):
        print(f'Welcome to Bank, {self.cname}')

    def display_cc_details(self):
        print(f'{self.creditscore} - {self.status}')