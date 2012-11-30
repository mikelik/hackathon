'''
Created on 30-11-2012

@author: Przemek
'''

import CmdPlayers
import CmdHand
import CmdCondottiere

cards = []
regions = ['Torino','Milano','Venezia','Genova','Mantova','Parma','Modena','Ferrara','Bologna','Lucca','Firenze','Siena','Spoleto','Urbino','Ancona','Roma','Napoli']
players = ['Torino2']

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
            args.pop()
            
        elif 'GameEnd' == extractCommand(args):
            print 'GameEnd'
            args.pop()
        
        elif 'RoundStart' == extractCommand(args):
            print 'RoundStart'
            args.pop()
            
        elif 'BattleStart' == extractCommand(args):
            print 'BattleStart'
            args.pop()

        elif 'BattleEnd' == extractCommand(args):
            print 'BattleEnd'    
        
        elif 'RoundEnd' == extractCommand(args):
            print 'RoundEnd'
        
        elif 'Players' == extractCommand(args):
            args = CmdPlayers.handle(args)
        
        elif 'Order' == extractCommand(args):
            print 'Order'
        
        elif 'Hand' == extractCommand(args):
            print 'Hand'
            args = CmdHand.handle(args);
        
        elif 'Player' == extractCommand(args):
            print 'Player'
        
        elif 'CurrentZone' == extractCommand(args):
            print 'CurrentZone'
            
        elif '?Condottiere' == extractCommand(args):
            args = CmdCondottiere.handle(args)
        
        #if 'Player' == extractCommand(args):
        #    print 'Player'
        
        elif 'Pass' == extractCommand(args):
            print 'Pass'    
        
        elif 'Play' == extractCommand(args):
            print 'Play'
        
        elif 'Protect' == extractCommand(args):
            print 'Protect'
        
        elif 'Retrieve' == extractCommand(args):
            print 'Retrieve'
        
        elif 'Score' == extractCommand(args):
            print 'Score'
            
