'''
Created on Aug 21, 2015

@author: sanjeev
'''

import sys

def print_commandline():
    print('The command line arguments are: ')

    for i in sys.argv:
        print(i)
    
        print ('\n\n The PYTHONPATH is' , sys.path, '\n')