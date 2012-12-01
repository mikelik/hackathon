'''
Created on 01-12-2012

@author: Przemek
'''

def log(message):
    f1=open('./testfile', 'w+')
    f1.write(message)
    print message
