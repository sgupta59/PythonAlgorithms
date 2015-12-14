'''
Created on Dec 4, 2015

@author: sanjeev
'''
from logging import FileHandler
import re 


if __name__ == '__main__':
    pass

# fobj = open('S:/sanjeev/gtidome_app/50197/CumminsDIPulse.gop','r')
# fobj_out = open ('C:/temp/abc.gop', 'w')
# for line in fobj:
#     print(line.rstrip())
#     fobj_out.write(line)
#     
# fobj.close
# fobj_out.close

# re.sub('\babc\b', 'efg', s) --> \b ... \b is word boundary.

def read_write_file(inp):
    ''' Open the file as a FileHandler '''
    inFobj = open(inp, 'r')
    outFobj = open('C:/temp/abc.gop','w')  
    
    for line in inFobj:
        #outFobj.write(line.replace('rswdata', 'rsw'))
        line = re.sub('\brswdata_item\b', 'rswdata', line) 
        outFobj.write(line)
        
    inFobj.close()
    outFobj.close()
    
read_write_file('S:/sanjeev/gtidome_app/50197/CumminsDIPulse.gop')
print ('exiting.....')