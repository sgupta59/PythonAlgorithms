'''
Created on May 6, 2015

@author: sanjeev
'''

if __name__ == '__main__':
    pass

import humansize

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],  
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
si_suffixes = humansize.SUFFIXES[1000]
print('1000{0[0]} = 1{0[1]}'.format(si_suffixes))

wordlist = ["red", "green", "blue"]
wordlist2 = list(wordlist)

# can not convert list to string implictly
# print("words: " + wordlist2)

# tuples
typle1 = ('red', 'green', 'blue')
#print("item: " + typle1[0])

#sets
set1 = {"abc", "efg", "abc"}
print (set1)
set2 = set("hello")
print(set2)

# dictionary
dict1 = {'ga' : 'irish', 'de' : 'german'}
print (dict1)
pairs = [( 'ga' , 'Irish' ), ( 'de' ,'German' )]
dict2 = (pairs)
print (dict2)

# print
print("abc")
