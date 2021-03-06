'''
Created on 30-11-2012

@author: Przemek
'''

import CommandParser
import Logger
from copy import deepcopy

def handle(args):
    CommandParser.cards = []
    CommandParser.originalCards = []
    weAreLosing = False
    for index in range(1, len(args)-1):
        item = args[index]
        if (item == ']'):
            #print "Command Hand returning: %s::\n" % args[index+1:]
            return args[index+1:]
        CommandParser.cards.append(item)
        Logger.log("Command Hand appended :%s:\n" % item)
    CommandParser.originalCards = deepcopy(CommandParser.cards)
    return ''