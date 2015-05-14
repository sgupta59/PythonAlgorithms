'''
Created on May 13, 2015

@author: sanjeev
'''

x = 50

def func(y):
    '''
        changes made to global variable
    '''
    global x
    print(' x before change ' , x)
    x = 25
    print(' x after change ' , x)
    
func(x)
print(' x after func call ' , x)