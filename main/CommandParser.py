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
    if (len(args) == 0):
        return ''
    try:
        return args.split()[0]
    finally:
        return args[0]
    


def parseCommand(args):
    while(len(args) > 0):
        if 'GameStart' == extractCommand(args):
            print 'GameStart'
            args = ''
        
        if 'GameEnd' == extractCommand(args):
            print 'GameEnd'
        
        if 'RoundStart' == extractCommand(args):
            print ''
            
        if 'BattleStart' == extractCommand(args):
            print 'BattleStart'
        
        if 'BattleEnd' == extractCommand(args):
            print 'BattleEnd'    
        
        if 'RoundEnd' == extractCommand(args):
            print 'RoundEnd'
        
        if 'Players' == extractCommand(args):
            args = CmdPlayers.handle(args)
        
        if 'Order' == extractCommand(args):
            print 'Order'
        
        if 'Hand' == extractCommand(args):
            print 'Hand'
            CmdHand.handle(args);
        
        if 'Player' == extractCommand(args):
            print 'Player'
        
        if 'CurrentZone' == extractCommand(args):
            print 'CurrentZone'
            
        if '?Condottiere' == extractCommand(args):
            args = CmdCondottiere.handle(args)
        
        #if 'Player' == extractCommand(args):
        #    print 'Player'
        
        if 'Pass' == extractCommand(args):
            print 'Pass'    
        
        if 'Play' == extractCommand(args):
            print 'Play'
        
        if 'Protect' == extractCommand(args):
            print 'Protect'
        
        if 'Retrieve' == extractCommand(args):
            print 'Retrieve'
        
        if 'Score' == extractCommand(args):
            print 'Score'
            
        args.split('\n')[1:]
