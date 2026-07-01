import sys
class ATM:
    def __init__(self):
        self.Card_number=1234567898765432
        self.PIN=692008
        self.Balance=15000
        self.name="Samiksha Anwat"
        self.account_no=9988776655

    def card_check(self):
        while True:
            self.card=input("Enter a card(yes/no):")
            if self.card=="yes" or self.card=="YES":
                print("Enter card successfully")
                break
            else:
                print("Please enter card")

    def login(self):
        while True:
            self.card=int(input("Enter a card number: "))
            i=1
            while i<=3:
                self.user_pin=int(input("Enter user PIN:"))
                if self.Card_number==self.card and self.PIN==self.user_pin:
                    print("login successfully")
                    self.ATM_menu()
                    break
                else:
                    print("Enter valid pin and card number")
                    i=i+1
            print("PIN limit exceeded")

    def check_balance(self):
        while True:
            self.pin=int(input("Enter a PIN:"))
            if self.PIN==self.pin:
                print("balance fetch successfully")
                print("Balance=",self.Balance)
                break
            else:
                print("Enter valid pin")

    def withdraw_amount(self):
        while True:
            self.amt=int(input("Enter amount to withdraw:"))
            self.pin=int(input("Enter a PIN:"))
            if self.Balance<=self.amt:
                print("Balance is not sufficient to withdraw")
                break
            elif self.PIN==self.pin :
                self.Balance-=self.amt
                print("Amount withdrawn sunccessfully")
                break
            else:
                print("Incorrect PIN...! Enter valid PIN")
                break

    def deposit_amount(self):
        while True:
            self.amount=int(input("Enter amount to Deposit:"))
            self.pin=int(input("Enter a PIN:"))
            if self.amount<=0:
                print("Please enter valid amount")
                break
            elif self.pin==self.PIN:
                self.Balance+=self.amount
                print("Amount deposited successfully")
                break
            else:
                print("Please enter valid PIN")

    def user_details(self):
        print("-----User Details-----")
        print("Name=",self.name)
        print("Account numbar:",self.account_no)
        print("Card number:",self.Card_number)

    def ATM_menu(self):
        while True:
            print("1.check balance")
            print("2.withdraw amount")
            print("3.deposit amount")
            print("4.Display details")
            print("5.Exit")
            choice=int(input("Enter your choice:"))
            if choice==1:
                self.check_balance()
            elif choice==2:
                self.withdraw_amount()
            elif choice==3:
                self.deposit_amount()
            elif choice==4:
                self.user_details()
            elif choice==5:
                print("Thank you...! ")
                print("Take your card..")
                sys.exit()
            else:
                print("Please Enter valid choice")

A=ATM()
A.card_check()
A.login()
A.ATM_menu()








