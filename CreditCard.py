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
            return self._balance
            
        
cc = CreditCard('Sai Krishna' , '1st bank' , '5301 1234 2345' , 1000)
account = cc.get_account()
cust= cc.get_customer()
limt= cc.get_limit()
bal = cc.get_balance()

bal = cc.charge(500)
bal = cc.charge(300)
print(f' account: {account}\n cust: {cust}\n limt: {limt}\n bal: {bal}\n')
curr_bal = cc.make_payment(500)
curr_bal = cc.make_payment(300)
print(f' account: {account}\n cust: {cust}\n limt: {limt}\n bal: {bal}\n current_balance:{curr_bal}')
