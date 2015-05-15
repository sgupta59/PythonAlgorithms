'''
Created on May 15, 2015

@author: sanjeev
'''

shoplist = ['apple', 'mango', 'banana']

print ('My list is ' , len(shoplist), ' long')

print ('items are: ' , end='')
for item in shoplist:
    print(item,end=' ')
    
newitem = input('\n Add anohter item: ')

shoplist.append(newitem)

print('updated list is: ', shoplist)
    
shoplist.sort()
print('sorted list is: ' , shoplist)

print('removing item: ', shoplist[0])

shoplist.remove(shoplist[0])

print('new list: ', shoplist)

fp = open('C:/temp/list.txt','w')
for item in shoplist:
    fp.write(item)
fp.close()

print('items written to file')