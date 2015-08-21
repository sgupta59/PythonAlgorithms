'''
Created on Aug 21, 2015

@author: sanjeev
'''

if __name__ == '__main__':
    pass

class Stack:
    def __init__(self):
        self.items=[]
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return (self.items == [])
    
    
def sum_list(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


def print_list(numbers):
    for x in numbers:
        print(x)
 
        
def reverse_list(numbers):
    if len(numbers) == 0:
        return numbers
    
    temp = numbers.pop(0)
    reverse_list(numbers)
    numbers.append(temp)
    
    return numbers
    
def insert_at_top(numbers, item):
    if len(numbers) == 0:
        numbers.append(item)
        return
    tmp = numbers.pop()
    insert_at_top(numbers,item)
    numbers.append(tmp)
    
def reverse_list_1(numbers):
    if len(numbers) == 0:
        return
    
    tmp = numbers.pop()
    reverse_list_1(numbers)
    insert_at_top(numbers,tmp)
    
 

   
numbers = [2, 4, 6, 8]

print_list(numbers)

reverse_list_1(numbers)

reverse_list(numbers)
print_list(numbers)

s = Stack()
s.push(54)
s.push(45)
s.push("+")

while not s.is_empty():
    print(s.pop(), end=" ")