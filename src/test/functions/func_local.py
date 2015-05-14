'''
Created on May 13, 2015

@author: sanjeev
'''
x = 50

def func(x):
    '''
        This function attempts to change a value of a global variable
    '''
    print('x is ' , x)
    x = 2 
    print('changed x to ' , x)
    
func(x)
print ('after call, x is ', x)