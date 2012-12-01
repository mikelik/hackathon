'''
Created on 30 Nov 2012

@author: Czeslaw
'''

import CommandParser
import Logger

def handle(args):
    Logger.log("Command BattlStart: %s::" % args[0])
    return args[1:]
