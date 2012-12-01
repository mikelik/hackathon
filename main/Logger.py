'''
Created on 01-12-2012

@author: Przemek
'''

def log(message):
    f1=open('./logs', 'a+')
    print message
    if type(message) is str :
        f1.write(message)
    else:
        f1.write(' '.join(message))
    f1.write('\n')
    f1.flush()
