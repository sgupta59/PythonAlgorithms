'''
Created on Oct 6, 2015

@author: sanjeev
'''

myDictionary = { 'key1' : 'value1' , 'key2' : 'value2' , 'key3' : 'value3'}

print ('value for key1: ' + myDictionary['key1'])

myDictionary['key4'] = 'value4'

for key, value in myDictionary.items():
    print('Key: ' + key + ' , ' + value)
    
if 'key1' in myDictionary:
    print ('Value of key1 is: ' + myDictionary['key1'])
    
    