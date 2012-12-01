'''
Created on 01-12-2012

@author: Przemek
'''

import CommandParser
import Logger

def handle(args):
    Logger.log("Command %s::" % args[0])
    CommandParser.currentPlayer=args[0].split()[1]
    #Logger.log(CommandParser.currentPlayer)
    return args[1:]
