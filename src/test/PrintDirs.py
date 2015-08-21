'''
Created on Jun 24, 2015

@author: sanjeev
'''

import os
import sys
import stat

dirs='C:/work/'

def printDirs(dir):
    print('Listing directory contents' + dir)
    output_file = os.path.join(dir,'output.txt')
    
    with open(output_file,'wb') as fh:
        for root, subdirs, files in os.walk(dir):
            fh.write(((' Root Directory: {}\n').format(dir)).encode('utf-8'))
            for subdir in subdirs:
                currentdir = os.path.join(root,subdir)
                fh.write((('\t Subdirectories: {} \n').format(currentdir)).encode('utf-8'))
            for file in files:
                currentfile = os.path.join(root,file)
                
                fh.write((('\t\t Files: {} \n').format(currentfile)).encode('utf-8'))


def findFiles(dirs, ext):
    print('Processing directory: {0} for extension {1}'.format(dirs,ext))
    
    output_file = os.path.join(dirs,'gtmfiles')
    
    with open(output_file,'wb') as fh:
        for root, subdirs, files in os.walk(dirs):
            for file in files:
                current_file = os.path.join(root, file)
                if current_file.endswith(ext):
                    ncurfile = os.path.normpath(current_file)
                    print('File : {}'.format(ncurfile))
                    fh.write((('File: {}').format(ncurfile)).encode('utf-8'))
                    os.chmod(ncurfile, stat.S_IWUSR)
                    os.remove(ncurfile)
    
findFiles(dirs,'.tmp')   
#printDirs(dirs)                


