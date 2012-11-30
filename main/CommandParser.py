'''
Created on 30-11-2012

@author: Przemek
'''

import CmdPlayers
import CmdHand
import CmdCondottiere

cards = []
regions = ['Torino','Milano','Venezia','Genova','Mantova','Parma','Modena','Ferrara','Bologna','Lucca','Firenze','Siena','Spoleto','Urbino','Ancona','Roma','Napoli']
players = []

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
            args = args[1:]

        elif 'BattleEnd' == extractCommand(args):
            print 'BattleEnd'    
            args = args[1:]
        
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
            args = args[1:]
            
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
            
