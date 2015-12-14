'''
Created on Oct 6, 2015

@author: sanjeev
'''

def listTests():
    myStringList = ['1', '2', '3', '4']
    print('My String List: ' + str(myStringList))
    del myStringList[0]
    print('My String List after removing first item: ' + str(myStringList))
    myStringList1 = myStringList[:]
    del myStringList1[0]
    print('My String List1 after removing first item: ' + str(myStringList1))
    
listTests()