'''
Created on Jun 26, 2015

@author: sanjeev
'''

import xml.etree.ElementTree as etree

def tests(xmlfile):
    tree = etree.parse(xmlfile)
    root = tree.getroot()
    print('Top Level Info {}'.format(root.tag))
    for object in root.iter('object'):
        #print (object.attrib)
        if 'implicit' in object.attrib:
            print(object.attrib['id'], object.attrib['name'], object.attrib['t_id'], object.attrib.get('implicit','explicit'))
    #===========================================================================
    # attrib = root.attrib
    # for key in attrib.keys():
    #     print(key,'=', attrib[key])
    #     
    # for child in root:
    #     print('Child: ', child.tag)
    #     childattrib = child.attrib
    #     for key in childattrib.keys():
    #         print('\t', key, '=', childattrib[key])
    #===========================================================================
            
xmlfile='C:/temp/True_Implicit_Objects/4cyl/SI_4cyl_Basic.gtm'
tests(xmlfile)