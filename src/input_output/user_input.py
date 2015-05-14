'''
Created on May 14, 2015

@author: sanjeev
'''

def reverse(text):
    return text[::-1]

def isPalindrome(text):
    return text == reverse(text)

text = input('enter a string: ')
if (isPalindrome(text)):
    print(text, ' is a palindrome')
else:
    print(text, ' is not a palindrome')