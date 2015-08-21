'''
Created on Jun 26, 2015

@author: sanjeev
'''

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],  
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    
    if size < 0:
        raise ValueError('number must be non-negative')
    
    if a_kilobyte_is_1024_bytes:
        multiple = 1024
    else:
        multiple = 1000
        
    for suffix in SUFFIXES[multiple]:
        
        size /= multiple
        
        if size <= multiple:
            
            return '{0:.1f} {1}'.format(size,suffix)
        
    raise ValueError('Number is too large')

number = 1025
#print(approximate_size(number))