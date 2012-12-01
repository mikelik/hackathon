'''
Created on 30 Nov 2012

@author: Czeslaw
'''

import  CommandParser
import Logger
from string import lower

def handle(args):
    Logger.log("Command %s::" % args[0])
    team = args[0].split()[1]
    if 'tie' not in team:
        CommandParser.occupiedRegion[CommandParser.ix(CommandParser.currentZone)] = 1
        if lower(team) == lower(CommandParser.ourPlayer):
            CommandParser.ourRegion[CommandParser.ix(CommandParser.currentZone)] = 1
    return args[1:]
