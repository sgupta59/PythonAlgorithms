'''
Created on Sep 30, 2015

@author: sanjeev
'''
import re 

def read_file(filename):
    f = open(filename,'r')
    out = open('C:/Users/sanjeev/jarfiles.txt', 'w')
    id = 0
    jarlist =  dict()
    for line in f:
        # print(line)
        jarlist[id] = line
        id = id + 1
    for keys,values in jarlist.items():
        if re.search(r'jar', values):
            out.writelines('{}:{}\n'.format(keys,values))
    
    f.close()
    out.close()
    
filename='C:/Users/sanjeev/output.log'
read_file(filename)
    