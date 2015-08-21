'''
Created on Jun 23, 2015

@author: sanjeev
'''

class SchoolMember:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initializing SchoolMember: {}'.format(self.name))
        
    def tell(self):
        print('Name: "{}", Age:"{}"'.format(self.name, self.age)),
        
class Teacher(SchoolMember):
    
    def __init__(self, name,age, salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('Initialzing Teacher: {}'.format(self.name))
        
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {:d}'.format(self.salary))
        
class Student(SchoolMember):
    def __init__(self,name,age,grade):
        SchoolMember.__init__(self,name,age)
        self.grade = grade
        print('Initialzing Student: {}'.format(self.name))
        
    def tell(self):
        SchoolMember.tell(self)
        print ('Student Grade: {}'.format(self.grade))
        
t = Teacher('one', 33, 30000)
s = Student('two', 2, 6)

print()

members = [t,s]

for member in members:
    member.tell()
        