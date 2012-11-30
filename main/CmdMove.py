'''
Created on 30-11-2012

@author: Przemek
'''

import CommandParser
import TCPCommunicator

def handle():
    print 'Move: ' + CommandParser.cards
    for card in CommandParser.cards :
        TCPCommunicator.sendMessage(card)
