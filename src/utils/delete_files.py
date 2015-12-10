'''
Created on Aug 21, 2015

@author: sanjeev
'''
import os
import shutil

def clean_up_directory(directory, extn):
    
    for dirpath, dirnames, files in os.walk(directory):
        if dirpath.find(".git") > -1:
            continue
        # delete all directories that end with Debug or ipch
        if dirpath.endswith("Debug"):
            print('Removing directory: ' + dirpath)
            shutil.rmtree(dirpath, ignore_errors=True)
        else:
            print('Skipping path: ', dirpath)
        if dirpath.endswith("ipch"):
            print('Removing directory: ' + dirpath)
            shutil.rmtree(dirpath, ignore_errors=True)
        for file in files:
            if file.endswith('sdf') or file.endswith('suo'):
                file1 = os.path.join(dirpath,file)
                print('Removing directory: ' + file1)
                os.remove(file1)
                
def cleandir(directory):
    
    for dirpath, dirnames, files in os.walk(directory):
        
        for dir in dirnames:
            if directory == dir:
                continue
            deldir = os.path.join(dirpath, dir)
            print('Deleting: ' + deldir)
            shutil.rmtree(deldir, ignore_errors=True)
            
        for file in files:
            delfile = os.path.join(dirpath,file)
            print ('Deleting File: ' + delfile)
            shutil.rmtree(delfile, ignore_errors=True)
        
dir = "C:\\Users\\Sanjeev\\git\AlgorithmsCPP"
extn = "log"
cleandir('C:/work/profiling/')
#clean_up_directory(dir,extn)