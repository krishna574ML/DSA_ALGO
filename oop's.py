class Bank:
    
    def __init__(self ,name, accountnumber , balance = 0):
        self._name = name
        self._balance = balance
        self._accountnumber = accountnumber
    
    def account_details(self , mobile):
        self.mobile_number = mobile
        print(f"Name is {self._name} and account number is {self._accountnumber} and mobile number is {self.mobile_number}")
    
    def account_credit(self , amount):
        
        # check if the amount entered is valid or not
        if isinstance(amount,(int, float)):
            self._balance += amount
            print(f" Amount is deposited into Account {self._accountnumber} and Available balance is {self._balance}")
        else:
            print("Please enter valid amount")
    
    def account_debit(self, amount):
        if self._balance < amount:
            print(f"Account{self.accountnumber} has not enough balance to withdrawamoun, Avaible balance {self._balance} , entered amount for withdraw {amount}")
        else:
            self._balance -= amount
            print(f" Avaible balance after withdraw{self._balance}")
            
    def get_balance(self):
        print(self._balance)

user_1 = Bank('Sai Krishna' , 516012345)
user_1.account_details(7075012122)
user_1.account_credit(10000)
user_1.account_debit(10000)
user_1.get_balance()
user_1.account_credit(20000)
user_1.get_balance()