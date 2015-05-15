'''
Created on May 14, 2015

@author: sanjeev
'''

import pickle

shoplistfile='C:/temp/shoplist.txt'

shoplist=['apple', 'mango', 'banana']

fp = open(shoplistfile,'wb')
pickle.dump(shoplist,fp)
fp.close()

del shoplist

fp = open(shoplistfile,'rb')
shoplist=pickle.load(fp)

print(shoplist)