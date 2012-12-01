'''
Created on 30-11-2012

@author: mikel
'''
from main import TCPCommunicator
import CommandParser
import random


def handle(args):
    
    
#    for i in reversed(range(len(CommandParser.regions))):
#        CommandParser.regionNeighbours.index()
#        for i in range(len(CommandParser.regions)):
#            if CommandParser.ourRegion[i] == 1:
#                currentRegion = i
  
    currentRegion = -1
  
    for i in range(len(CommandParser.regions)):
        if CommandParser.ourRegion[i] == 1:
                
                for neIdx in range(len(CommandParser.m[i])):
                    if CommandParser.m[i][neIdx] == 0:
                        currentRegion = i
                        print 'Found neighbour region, attacking: '
                        print CommandParser.m[CommandParser.ix(i)]
    
    resp = None
    if currentRegion >= 0:
        resp = CommandParser.regions[currentRegion]              
    else:
        resp = CommandParser.regions[random.randint(0,len(CommandParser.regions)-1)]
    print "Condottiere :%s:" % resp
    while CommandParser.occupiedRegion[CommandParser.ix(resp)] == 1:
        resp = CommandParser.regions[random.randint(0,len(CommandParser.regions)-1)]
    TCPCommunicator.sendMessage(resp)
    return args[1:]
