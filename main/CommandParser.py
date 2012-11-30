'''
Created on 30-11-2012

@author: Przemek
'''

import CmdPlayers
import CmdHand
import CmdCondottiere
import CmdCurrentzone
import CmdBattleStart, CmdBattleEnd


cards = []
regions = ['Torino','Milano','Venezia','Genova','Mantova','Parma','Modena','Ferrara','Bologna','Lucca','Firenze','Siena','Spoleto','Urbino','Ancona','Roma','Napoli']
players = []

regionsMap = {'Torino': 0, 'Milano': 1, 'Venezia': 2, 'Genova': 3, 'Mantova': 4, 'Parma': 5, 'Modena': 6, 'Ferrara': 7, 'Bologna': 8,'Lucca':9,'Firenze':10,'Siena':11,'Spoleto':12,'Urbino':13,'Ancona':14,'Roma':15,'Napoli':16 }
occupiedRegion = [0]*len(regions)
currentZone = None

def ix(region):
    return regionsMap[region]

m = []
# vertex numbering starts from 0
for i in range(0, len(regions)):
    temp = []
    for j in range(0, len(regions)):
        temp.append(0)
        m.append(temp)
    
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



def extractCommand(args):
    line = args[0]
    if (len(line) == 0):
        return ''
    #if line regexp 
    return line.split()[0]


def parseCommand(args):
    print 'parseCommand: %s::\n' % args
    while(len(args) > 0):
        if 'GameStart' == extractCommand(args):
            print 'GameStart'
            args = args[1:]
            
        elif 'GameEnd' == extractCommand(args):
            print 'GameEnd'
            args = args[1:]
        
        elif 'RoundStart' == extractCommand(args):
            print 'RoundStart'
            args = args[1:]
            
        elif 'BattleStart' == extractCommand(args):
            print 'BattleStart'
            args = CmdBattleStart.handle(args);


        elif 'BattleEnd' == extractCommand(args):
            print 'BattleEnd' 
            args = CmdBattleEnd.handle(args);  
        
        elif 'RoundEnd' == extractCommand(args):
            print 'RoundEnd'
            args = args[1:]
        
        elif 'Players' == extractCommand(args):
            args = CmdPlayers.handle(args)
        
        elif 'Order' == extractCommand(args):
            print 'Order'
            args = args[1:]
        
        elif 'Hand' == extractCommand(args):
            print 'Hand'
            args = CmdHand.handle(args);
        
        elif 'Player' == extractCommand(args):
            print 'Player'
            args = args[1:]
        
        elif 'CurrentZone' == extractCommand(args):
            print 'CurrentZone'
            args = CmdCurrentzone.handle(args);

            
        elif '?Condottiere' == extractCommand(args):
            args = CmdCondottiere.handle(args)
        
        #if 'Player' == extractCommand(args):
        #    print 'Player'
        
        elif 'Pass' == extractCommand(args):
            print 'Pass'    
            args = args[1:]
        
        elif 'Play' == extractCommand(args):
            print 'Play'
            args = args[1:]
        
        elif 'Protect' == extractCommand(args):
            print 'Protect'
            args = args[1:]
        
        elif 'Retrieve' == extractCommand(args):
            print 'Retrieve'
            args = args[1:]
        
        elif 'Score' == extractCommand(args):
            print 'Score'
            args = args[1:]
            
