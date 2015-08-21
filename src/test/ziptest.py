'''
Created on Jun 26, 2015

@author: sanjeev
'''

import zipfile

def ziptests(infile):
    print('The input file is: {}'.format(infile))
    zf = zipfile.ZipFile(infile,'r')
    filelist = zf.namelist()
    for file in filelist:
        print('{}'.format(file))
    
zinfile='C:\Temp\Integrated_Crank_Chain_Cam.gdx'
ziptests(zinfile)