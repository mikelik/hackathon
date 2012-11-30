'''
Created on 30-11-2012

@author: Przemek
'''

import CommandParser
import TCPCommunicator
import random

def handle(args):
    print 'Move: '
    print CommandParser.cards
    resp = None
    if len(CommandParser.cards) <= 0:
        resp = 'pass'
    else:
        ran = random.randint(0,len(CommandParser.cards)-1)
        resp = CommandParser.cards[ran]
        CommandParser.cards.remove(resp)
    TCPCommunicator.sendMessage(resp)
    return args[1:]
