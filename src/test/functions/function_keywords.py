'''
Created on May 13, 2015

@author: sanjeev
'''

if __name__ == '__main__':
    pass

def total(*numbers, final):
    count=0
    for number in numbers:
        count += number
    count += final 
    return count

def total1(*numbers, **keys):
    count = 0
    for number in numbers:
        count += number
    for key in keys:
        count += keys[key]
    return count
    
print(total(1,2,3))
print(total1(1,2,3,final=5, new=4))