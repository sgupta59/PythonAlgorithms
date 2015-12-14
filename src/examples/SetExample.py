'''
Created on Oct 6, 2015

@author: sanjeev
'''

''' create a set ''' 
bri = set(['brizil', 'india', 'russia', 'russia'])

print ('set is: ' + str(bri))

print('copying a set: ' + str(bri.copy()))

# is india in set
if 'india' in bri:
    print('India True')
    
if 'china' in bri:
    print('china True')
else:
    print('china False')
    
bri1 = bri.copy()
bri1.add('china')

print('intersection ' + str(bri1 & bri))