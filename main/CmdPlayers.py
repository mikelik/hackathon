'''
Created on 30 Nov 2012

@author: Czeslaw
'''

import CommandParser


def handle(args):
    for index in range(1, len(args)-1):
        item = args[index]
        if (item == ']'):
            #print "Command Players returning: %s::\n" % args[index+1:]
            return args[index+1:]
        CommandParser.players.append(item)
        CommandParser.scoreMap[item] = 0
        print "Command Players appended :%s:\n" % item
    return ''
