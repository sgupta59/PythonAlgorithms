'''
Created on Sep 18, 2015

@author: sanjeev
'''

class Customer(object):
    
    """ 
        Static Variable in Customer class
    """
    count = 0
    
    """ A customer class, what the hell is:
       object
    """
    
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        Customer.count += 1
        
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def __str__(self):
        return self.name  + ',' + str(self.balance)
    
    """
        Static methods
        uses @staticmethod decorator
    """
    @staticmethod
    def type():
        print('type human')
    
    """
        Class methods
    """
    @classmethod
    def more_than_one(cls):
        return cls.count > 0
    
jess = Customer('jess', 25)
jess = Customer('jess1', 22)
print(jess)
print (Customer.count)