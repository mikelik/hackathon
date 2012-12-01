'''
Created on 30 Nov 2012

@author: Czeslaw
'''
import CommandParser
import Logger

def handle(args):
    Logger.log("Command %s::" % args[0])
    zone = args[0].split()[1]
    if 'null' not in zone:
        CommandParser.protectedZone = zone
        Logger.log("Protected zone %s::" % zone)
    else:
        CommandParser.protectedZone = None
        Logger.log("Protected zone off")

    return args[1:]
