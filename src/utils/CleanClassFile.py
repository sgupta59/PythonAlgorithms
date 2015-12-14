'''
Created on Sep 17, 2015

@author: sanjeev
'''
import os
import shutil

def delete_class_files(dir):
    
    for rootdir, subdirs, files in os.walk(dir):
        for file in files:
            if str(file).endswith('.class'):
                fullpath = os.path.join(rootdir,file)
                if os.path.isfile(fullpath):
                    print('Removing file: ' + fullpath)
                    os.remove(fullpath)
                else:
                    print(fullpath)
            
dirs_to_clean = ['GTI3d', 'gtintegration', 'GTISoft', 'GTSuiteUI', 'jplot', 'RMS',  'Solverjni']
root_dir = 'C:/v2016/'

for dir in dirs_to_clean:
    clean_dir = os.path.join(root_dir, dir)
    delete_class_files(clean_dir)
