'''
Created on May 15, 2015

@author: sanjeev
'''

ab = { 'Swaroop' : 'swaroop@swaroopch.com',
      'Larry' : 'larry@wall.org',
      'Matsumoto' : 'matz@ruby-lang.org',
      'Spammer' : 'spammer@hotmail.com'
}

print('email dictionary is:', ab)

print('each listing item in dictoray is:')
for names,address in ab.items():
    print(names,address)
    
print('each item in dictoray is:')
for names in ab.items():
    print(names[0], names[1])