'''
Created on May 14, 2015

@author: sanjeev
'''

poem = '''\
    Programming is fun
    When the work is done
    if you wnat etc
    '''
fp = open('C:/temp/test.txt', 'w')
fp.write(poem)
fp.close()

fp = open('C:/temp/test.txt','r')
while True:
    line = fp.readline()
    if len(line) == 0:
        break
    # using end='' as the line already has an newline. if end='' is not used then two newlines get added
    print(line,end='')
fp.close()
