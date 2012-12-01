'''
Created on 30 Nov 2012

@author: Czeslaw
'''

import  CommandParser

def handle(args):
    #print "Command BattleEnd: %s::" % args
    if 'tie' not in args[0].split()[1]:
        CommandParser.occupiedRegion[CommandParser.ix(CommandParser.currentZone)] = 1
    return args[1:]
