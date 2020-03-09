class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance= balance
        
    def __str__(self):
        return f'Bank of America\nAccount owner:{self.owner}\nAccount balance $:{self.balance}'
    
    
    def deposit(self,dep_amt):
        
        self.balance += dep_amt
        
        print('deposit accepted: ${:,.2f}'.format(dep_amt))
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            
            self.balance -=wd_amt
            
            print('Withdrawal accepted: ${:,.2f}'.format(wd_amt))
            
        else:
            
            print('funds unavailable')
            
a=Account('Azizbek Gapurov', 10000)
print(a)            
print(a.deposit(10000))
print(a.withdraw(1100))
print(a)
