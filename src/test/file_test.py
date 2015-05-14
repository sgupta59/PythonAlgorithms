'''
Created on May 14, 2015

@author: sanjeev
'''

fp = open('S:/sanjeev/gtidome_app/50197/CumminsDIPulse.gop','r')
#print ('file pointer: ' , fp)
contents = fp.read()
print ('contents: ', contents)
wfp = open('S:/sanjeev/gtidome_app/50197/CumminsDIPulse1.gop','w')
wfp.write(contents)
wfp.close()