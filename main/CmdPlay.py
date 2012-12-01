'''
Created on 30 Nov 2012

@author: Czeslaw
'''

import CommandParser
import Logger

def handle(args):
    Logger.log("Command %s::" % args[0])
    Logger.log("Player %s played %s" % (CommandParser.currentPlayer, args[0].split()[1]))
    return args[1:]
