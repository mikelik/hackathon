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
  
    breakLoop = False
  
    for i in range(len(CommandParser.regions)):
        if CommandParser.ourRegion[i] == 1 and not breakLoop:
            for neIdx in range(len(CommandParser.m[i])):
                if CommandParser.m[i][neIdx] == 1 and CommandParser.occupiedRegion[neIdx] == 0 and not CommandParser.isProtectedZone(neIdx):
                    currentRegion = neIdx
                    Logger.log('Found neighbour region, attacking: ' + CommandParser.regions[neIdx])
                    if random.randint(0,10) > 3:
                        breakLoop = True
                    break
                        
#-------------- AI END
    
    resp = None
    if currentRegion >= 0:
        resp = CommandParser.regions[currentRegion]              
    else:
        for s in reversed(range(len(CommandParser.regions))): # 17, 16, 15 ->sortedNeighbours
            for n in range(len(CommandParser.regions)): # regionNeighbours
                if CommandParser.regionNeighbours[n] == CommandParser.sortedNeighbours[s]:
                    if CommandParser.occupiedRegion[n] == 0 and not CommandParser.isProtectedZone(n): # empty => fight for it
                        currentRegion = n
                    
        #index = currentRegion
        #index = random.randint(0,len(CommandParser.regions)-1)
        resp = CommandParser.regions[currentRegion]
        
    #while CommandParser.occupiedRegion[CommandParser.ix(resp)] == 1:
    #    resp = CommandParser.regions[random.randint(0,len(CommandParser.regions)-1)]
        
    Logger.log( "Condottiere :%s:" % resp)
    TCPCommunicator.sendMessage(resp)
    return args[1:]
