'''
Created on May 11, 2015

@author: sanjeev
'''

x = 50

def scopeFunc(x):
    print('x is: ', x)
    x = 2
    print('now x is: ' , x)
    

def printmax(x, y):
    ''' prints the maximum of x or y. if both are the same
        prints the message'''
    if x > y:
        print(x, ' is maximum')
        return x
    elif x < y:
        print(y, ' is maximum')
        return y
    else:
        print(x, ' and ' , y, ' are the same')
        return 'the numbers are the same'
    
print(printmax(2,2))
#print(printmax.__doc__)
#scopeFunc(x)
#print('x is ' , x)