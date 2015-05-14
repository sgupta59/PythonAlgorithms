'''
Created on May 14, 2015

@author: sanjeev
'''

year = int(input('in what year were you born in? '))
print('you entered: ' , year)
values = input('Enter x and y values separated by spaces: ')
pieces = values.split()
print ('Entered x: ', int(pieces[0]))
print ('Entered y: ', int(pieces[1]))