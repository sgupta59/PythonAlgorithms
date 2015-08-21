'''
Created on Aug 21, 2015

@author: sanjeev
'''
from utils.sys_module import print_commandline

if __name__ == '__main__':
    pass

def insert_at_top(items, item):
    if len(items) == 0:
        items.append(item)
        return
    
    item1 = items.pop()
    insert_at_top(items,item)
    items.append(item1)
    return
    
def reverse(items):
    if len(items) == 0:
        return
    
    item = items.pop()
    reverse(items)
    insert_at_top(items,item)
    return

print_commandline()
numbers = [1,2,3,4]
print(numbers)
reverse(numbers)
print(numbers)
