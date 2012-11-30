'''
Created on 01-12-2012

@author: Przemek
'''

import CommandParser

def handle(args):
    print 'Command Player'
    CommandParser.currentPlayer=args[0].split()[1]
    print CommandParser.currentPlayer
    return args[1:]
