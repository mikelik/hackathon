'''
Created on 30-11-2012

@author: Przemek
'''

import CommandParser
import TCPCommunicator
import random

def handle(args):
    print 'Move: ' + CommandParser.cards
    ran = random.randint(0,len(CommandParser.cards)-1)
    resp = CommandParser.cards[ran]
    TCPCommunicator.sendMessage(resp)
    CommandParser.cards.remove(ran)
    return args[1:]
