'''
Created on 30-11-2012

@author: Przemek
'''

import CommandParser

def handle(args):
    for index in range(1, len(args)-1):
        item = args[index]
        if (item == ']'):
            print "Command Hand returning: %s::\n" % args[index+1:]
            return args[index+1:]
        CommandParser.cards.append(item)
        print "Command Hand appended :%s:\n" % item
    return ''