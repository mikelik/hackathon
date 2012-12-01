'''
Created on 30 Nov 2012

@author: Czeslaw
'''

import  CommandParser
from string import lower

def handle(args):
    print "Command BattleEnd: %s::" % args
    team = args[0].split()[1]
    if 'tie' not in team:
        CommandParser.occupiedRegion[CommandParser.ix(CommandParser.currentZone)] = 1
        if lower(team) == lower(CommandParser.ourPlayer):
            CommandParser.ourRegion[CommandParser.ix(CommandParser.currentZone)] = 1
    return args[1:]
