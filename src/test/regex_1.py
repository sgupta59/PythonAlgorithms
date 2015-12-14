'''
Created on Dec 4, 2015

@author: sanjeev
'''

import re  

s = '100 BROAD'

print (re.sub('\bROAD$', 'RD', s))