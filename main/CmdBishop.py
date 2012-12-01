'''
Created on 30-11-2012

@author: mikel
'''
from main import TCPCommunicator
import CommandParser
import random
import Logger

def handle(args):
    currentRegion = -1
    breakLoop = False
    for i in range(len(CommandParser.regions)):
        if CommandParser.ourRegion[i] == 1 and not breakLoop:
            for neIdx in range(len(CommandParser.m[i])):
                if CommandParser.m[i][neIdx] == 1 and CommandParser.occupiedRegion[neIdx] == 0 and neIdx != CommandParser.ix(CommandParser.currentZone) and CommandParser.protectedRegion[neIdx] == 0:
                    currentRegion = neIdx
                    Logger.log('Found neighbour region, protecting: ' + CommandParser.regions[currentRegion])
                    breakLoop = True
                    break

    if currentRegion < 0:
        for neIdx in range(len(CommandParser.regions)):
            if CommandParser.occupiedRegion[neIdx] == 0  and neIdx != CommandParser.ix(CommandParser.currentZone) and CommandParser.protectedRegion[neIdx] == 0:
                Logger.log('Found empty region, protecting: ' + CommandParser.regions[neIdx])
                currentRegion = neIdx
                break
                
    if currentRegion >= 0:
        resp = CommandParser.regions[currentRegion]
    else:
        resp = 'pass'

    Logger.log("Bishop :%s:" % resp)
    TCPCommunicator.sendMessage(resp)
    return args[1:]
