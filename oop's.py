class Bank:
    
    def __init__(self ,name, accountnumber , balance = 0):
        self.name = name
        self.balance = balance
        self.accountnumber = accountnumber
    
    def account_details(self , mobile):
        self.mobile_number = mobile
        print(f"Name is {self.name} and account number is {self.accountnumber} and mobile number is {self.mobile_number}")
    
    def account_credit(self , amount):
        self.credit = amount
        
        # check if the amount entered is valid or not
        if isinstance(self.credit,(int, float)):
            self.balance += self.credit
            print(f" Amount is deposited into Account {self.accountnumber} and Available balance is {self.balance}")
        else:
            print("Please enter valid amount")
    
    def account_debit(self, amount):
        self.debit = amount
        
        if self.balance < self.debit:
            print(f"Account{self.accountnumber} has not enough balance to withdrawamoun, Avaible balance {self.balance} , entered amount for withdraw {self.debit}")
        else:
            self.balance -= self.debit
            print(f" Avaible balance after withdraw{self.balance}")
            
    def get_balance(self):
        print(self.balance)

user_1 = Bank('Sai Krishna' , 516012345)
user_1.account_details(7075012122)
user_1.account_credit(10000)
user_1.account_debit(10000)
user_1.get_balance()