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
        #for dirname in dirnames:
        if dirpath.endswith("Debug"):
            shutil.rmtree(dirpath, ignore_errors=True)
        if dirpath.endswith("ipch"):
            shutil.rmtree(dirpath, ignore_errors=True)
                
dir = "C:\\Users\\Sanjeev\\git\AlgorithmsCPP"
extn = "log"

clean_up_directory(dir,extn)