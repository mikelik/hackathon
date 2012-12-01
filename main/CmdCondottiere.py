'''
Created on 30-11-2012

@author: mikel
'''
from main import TCPCommunicator
import CommandParser
import random
import Logger

def handle(args):
    
    
#-------------- AI 
    currentRegion = -1
  
    for i in range(len(CommandParser.regions)):
        if CommandParser.ourRegion[i] == 1:
                
                for neIdx in range(len(CommandParser.m[i])):
                    if CommandParser.m[i][neIdx] == 0:
                        currentRegion = i
                        Logger.log('Found neighbour region, attacking: ')
                        Logger.log(CommandParser.regions[i])
                        
#-------------- AI END
    
    resp = None
    if currentRegion >= 0:
        resp = CommandParser.regions[currentRegion]              
    else:
#        for i in reversed(range(len(CommandParser.regions))):
#            CommandParser.regionNeighbours.index()
#            for i in range(len(CommandParser.regions)):
#                if CommandParser.ourRegion[i] == 1:
#                    currentRegion = i
        index = random.randint(0,len(CommandParser.regions)-1)
        resp = CommandParser.regions[index]
    while CommandParser.occupiedRegion[CommandParser.ix(resp)] == 1:
        resp = CommandParser.regions[random.randint(0,len(CommandParser.regions)-1)]
    Logger.log( "Condottiere :%s:" % resp)
    TCPCommunicator.sendMessage(resp)
    return args[1:]
