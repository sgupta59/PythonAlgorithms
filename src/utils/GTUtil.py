'''
Created on Oct 22, 2015

@author: sanjeev
'''
import os

def listInstallation(home):
    print ('GTIHOME: ' + home)

#jar_name = os.path.split(os.getcwd())[0].lower().join('.jar')    
curr_dir = os.getcwd()
tup = os.path.split(os.getcwd())
jar_name = os.path.split(os.getcwd())[1].lower() + '.jar'
target_file = os.path.join('C:/temp',jar_name)
print ('Head: ' + tup[0] + ', tail: ' + tup[1].lower())
response = input("Please enter your name: ")
print('Response is: ' + response + ', in director: ' + curr_dir)