'''
Created on May 11, 2015

@author: sanjeev
'''

x = 50

def scopeFunc(x):
    print('x is: ', x)
    x = 2
    print('now x is: ' , x)
    
    
def printMax(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a < b:
        print(a, 'is minimum')
    else:
        print(a,b, ' are equal')
    
#printMax(2,2)

scopeFunc(x)
print('x is ' , x)