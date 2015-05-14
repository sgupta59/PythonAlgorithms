'''
Created on May 13, 2015

@author: sanjeev
'''

'''
    function with parameters. Takes in two arguments and prints out the maximum of the two
'''
def printMax(a,b):
    if a > b:
        print('max is ', a)
    elif a == b:
        print (a,b,' are equal ')
    else:
        print('max is ', b)
        
printMax(1,2)