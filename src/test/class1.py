'''
Created on Jun 22, 2015

@author: sanjeev
'''


class Person:
    
    def __init__(self, name):
        self.name = name
        
    def say_hi(self):
        print('Say Hello to:', self.name)
    
p = Person('one')
q = Person('two')
'''
Prints the starting addresses of the two objects.
The difference between the two object's starting point is 160 bytes.
'''
print(p)
p.say_hi()
print(q)