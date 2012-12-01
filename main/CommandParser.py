'''
Created on 30-11-2012

@author: Przemek
'''

import CmdPlayers
import CmdHand
import CmdCondottiere
import CmdCurrentzone
import re
import CmdBattleStart, CmdBattleEnd, CmdMove, CmdBishop, CmdRetrieve, CmdPlayer, CmdScore, CmdRoundStart
import math


cards = []
regions = ['Torino','Milano','Venezia','Genova','Mantova','Parma','Modena','Ferrara','Bologna','Lucca','Firenze','Siena','Spoleto','Urbino','Ancona','Roma','Napoli']
players = []
scoreMap = {}

regionsMap = {'Torino': 0, 'Milano': 1, 'Venezia': 2, 'Genova': 3, 'Mantova': 4, 'Parma': 5, 'Modena': 6, 'Ferrara': 7, 'Bologna': 8,'Lucca':9,'Firenze':10,'Siena':11,'Spoleto':12,'Urbino':13,'Ancona':14,'Roma':15,'Napoli':16 }
occupiedRegion = [0]*len(regions)

ourRegion  = [0]*len(regions)
regionNeighbours = [0 for x in range(len(regions))]

currentZone = None
currentPlayer = None
ourPlayer = None

def ix(region):
    return regionsMap[region]

m = [[0 for x in range(len(regions))] for x in range(len(regions))] 
    
m[ix('Torino')][ix('Milano')]=m[ix('Milano')][ix('Torino')]=1
m[ix('Torino')][ix('Genova')]=m[ix('Genova')][ix('Torino')]=1
m[ix('Milano')][ix('Venezia')]=m[ix('Venezia')][ix('Milano')]=1
m[ix('Milano')][ix('Mantova')]=m[ix('Mantova')][ix('Milano')]=1
m[ix('Milano')][ix('Modena')]=m[ix('Modena')][ix('Milano')]=1
m[ix('Milano')][ix('Parma')]=m[ix('Parma')][ix('Milano')]=1
m[ix('Venezia')][ix('Mantova')]=m[ix('Mantova')][ix('Venezia')]=1
m[ix('Venezia')][ix('Ferrara')]=m[ix('Ferrara')][ix('Venezia')]=1
m[ix('Mantova')][ix('Modena')]=m[ix('Modena')][ix('Mantova')]=1
m[ix('Mantova')][ix('Ferrara')]=m[ix('Ferrara')][ix('Mantova')]=1
m[ix('Parma')][ix('Modena')]=m[ix('Modena')][ix('Parma')]=1
m[ix('Modena')][ix('Ferrara')]=m[ix('Ferrara')][ix('Modena')]=1
m[ix('Modena')][ix('Bologna')]=m[ix('Bologna')][ix('Modena')]=1
m[ix('Ferrara')][ix('Bologna')]=m[ix('Bologna')][ix('Ferrara')]=1
m[ix('Lucca')][ix('Firenze')]=m[ix('Firenze')][ix('Lucca')]=1
m[ix('Bologna')][ix('Firenze')]=m[ix('Firenze')][ix('Bologna')]=1
m[ix('Bologna')][ix('Urbino')]=m[ix('Urbino')][ix('Bologna')]=1
m[ix('Firenze')][ix('Urbino')]=m[ix('Urbino')][ix('Firenze')]=1
m[ix('Firenze')][ix('Spoleto')]=m[ix('Spoleto')][ix('Firenze')]=1
m[ix('Firenze')][ix('Siena')]=m[ix('Siena')][ix('Firenze')]=1
m[ix('Siena')][ix('Roma')]=m[ix('Roma')][ix('Siena')]=1
m[ix('Spoleto')][ix('Urbino')]=m[ix('Urbino')][ix('Spoleto')]=1
m[ix('Spoleto')][ix('Ancona')]=m[ix('Ancona')][ix('Spoleto')]=1
m[ix('Spoleto')][ix('Napoli')]=m[ix('Napoli')][ix('Spoleto')]=1
m[ix('Roma')][ix('Napoli')]=m[ix('Napoli')][ix('Roma')]=1

for i in range(0, len(regions)):
    for j in range(i+1, len(regions)):
        if m[i][j] == 1:
            regionNeighbours[i] += 1
            regionNeighbours[j] += 1
            
regionNeighbours.sort()
        


command = re.compile('^\s*([?\w]+)')
empty_line = re.compile('^\s*$')

def extractCommand(args):
    line = args[0]
    if (empty_line.match(line)):
        return ''
    #print "Matching :%s:" % line
    match = command.match(line)
    if match is None:
        return ''
    return match.group(1)


def parseCommand(args):
    #print '---parseCommand: %s::\n' % args
    while(len(args) > 0):
        cmd = extractCommand(args)
        if 'GameStart' == cmd:
            print '---GameStart'
            args = args[1:]
            continue
            
        if 'GameEnd' == cmd:
            print '---GameEnd'
            args = args[1:]
            continue
        
        if 'RoundStart' == cmd:
            args = CmdRoundStart.handle(args);
            continue
            
        if 'BattleStart' == cmd:
            print '---BattleStart'
            args = CmdBattleStart.handle(args);
            continue

        if 'BattleEnd' == cmd:
            args = CmdBattleEnd.handle(args);  
            continue
        
        if 'RoundEnd' == cmd:
            print '---RoundEnd'
            args = args[1:]
            continue
        
        if 'Players' == cmd:
            args = CmdPlayers.handle(args)
            continue
        
        if 'Order' == cmd:
            print '---Order'
            args = args[1:]
            continue
        
        if 'Hand' == cmd:
            args = CmdHand.handle(args);
            continue
        
        if 'Player' == cmd:
            args = CmdPlayer.handle(args)
            continue
        
        if 'CurrentZone' == cmd:
            args = CmdCurrentzone.handle(args);
            continue
            
        if '?Condottiere' == cmd:
            args = CmdCondottiere.handle(args)
            continue

        if '?Bishop' == cmd:
            args = CmdBishop.handle(args)
            continue
            
        if '?Move' == cmd:
            args = CmdMove.handle(args)
            continue
        
        if '?Retrieve' == cmd:
            args = CmdRetrieve.handle(args)
            continue
        
        if 'Pass' == cmd:
            print '---Pass'
            args = args[1:]
            continue
        
        if 'Play' == cmd:
            print '---Play'
            args = args[1:]
            continue
        
        if 'Protect' == cmd:
            print '---Protect'
            args = args[1:]
            continue
        
        if 'Retrieve' == cmd:
            print '---Retrieve'
            args = args[1:]
            continue
        
        if 'Score' == cmd:
            args = CmdScore.handle(args)
            continue
            
        if (len(args) > 0):
            print "Unhandled data :%s:" % args[0]
            print " for command :%s:\n" % cmd
            args = args[1:] 





