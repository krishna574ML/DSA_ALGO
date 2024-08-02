class CreditCard:
    ''' A counsumer credit card'''
    
    def __init__(self,customer , bank , acnt , limit) -> None:
        '''Create a new credit card instance.
        
        The intial balance is Zero.
        
        customer the name of the custome('e.g., ' Sai Krishna')
        bank     the name of the bank(e.g., ' SBI')
        account  the acount identifer (e.g., '5301 1234 2345')
        limit    credit card limit(in dollars)
        '''
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

        
    def get_customer(self):
        "Return name of the customer"
        return self._customer
    
    def get_balance(self):
        '''Returm current balance '''
        return self._balance
    
    def get_bank(self):
        '''Return name of the bank'''
        return self._bank
    
    def get_limit(self):
        '''Return credit card limit'''
        return self._limit
    
    def get_account(self):
        "Return account Identifier"
        return self._account
    
    def charge(self, price):
        ''' Charge the prize of the purchase on the card'''
        
        if price + self._balance > self._limit:
            return False
        else:
            self._balance = self._balance + price
            return self._balance
        
    def make_payment(self , amount):
        if amount > self._balance and amount > self._limit:
            return False
        else:
            self._balance -= amount
            return True
            
    
    
class PerdatoryCreditCard(CreditCard):
    ''' Inherit the CreditCard clas features'''
    
    def __init__(self,customer , bank , acnt , limit , apr):
        
        super().__init__(customer , bank  , acnt , limit)  # call super constructor
        self._apr = apr
    
    def charge(self , price):
        ''' Return True if limit and card is processed
            Return False charge $5 if denied the limit is overflow
        '''
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        '''Access the montly intrest rate on outstanding balance'''
        
        if self._balance >0 :
            montly_factor = pow(1+self._apr, 1/12)
            self._balance = self._balance * montly_factor
    
    
        

credit_card = CreditCard('Sai Krishna', 'SBI', '5301 1234 2345', 1000)
print("Customer:", credit_card.get_customer())
print("Bank:", credit_card.get_bank())
print("Account:", credit_card.get_account())
print("Limit:", credit_card.get_limit())
print("Balance:", credit_card.get_balance())

# Perform some transactions
print("\nCharging $200 to the credit card...")
credit_card.charge(200)
print("Balance after charging $200:", credit_card.get_balance())

print("\nMaking a payment of $100...")
credit_card.make_payment(100)
print("Balance after payment of $100:", credit_card.get_balance())

predatory_credit_card = PerdatoryCreditCard('Sai Krishna', 'SBI', '5301 1234 2346', 1000, 0.12)
print("\nCustomer:", predatory_credit_card.get_customer())
print("Bank:", predatory_credit_card.get_bank())
print("Account:", predatory_credit_card.get_account())
print("Limit:", predatory_credit_card.get_limit())
print("Balance:", predatory_credit_card.get_balance())

# Perform some transactions
print("\nCharging $1200 to the predatory credit card...")
result, balance = predatory_credit_card.charge(1200)
print("Charge result:", result)
print("Balance after charging $1200:", balance)

print("\nCharging $500 to the predatory credit card...")
result, balance = predatory_credit_card.charge(500)
print("Charge result:", result)
print("Balance after charging $500:", balance)

print("\nProcessing monthly interest...")
predatory_credit_card.process_month()
print("Balance after processing monthly interest:", predatory_credit_card.get_balance())