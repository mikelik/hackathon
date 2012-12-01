'''
Created on 30-11-2012

@author: Przemek
'''

import CommandParser
import TCPCommunicator
import random
import Logger
from copy import copy, deepcopy


def handle(args):
    CommandParser.ourPlayer = CommandParser.currentPlayer
    Logger.log( CommandParser.scoreMap)
    if CommandParser.ourPlayer:
        print "Our score = %s" % CommandParser.scoreMap[CommandParser.ourPlayer]
    Logger.log('Move: ')
    Logger.log(CommandParser.cards)
    resp = None
    if len(CommandParser.cards) <= 0:
        resp = 'pass'
    else:
        sortedcards = deepcopy(CommandParser.cards)
        digits = []
        for x in range(len(sortedcards)-1) :
            if sortedcards[x].isdigit() :
                digits.append(sortedcards[x])
        digits.sort(key=int)
        ran = random.randint(0,len(CommandParser.cards)-1)
        resp = CommandParser.cards[ran]
        if len(digits) > 0 :
            resp = digits[len(digits)-1]
            digits.remove(resp)
        CommandParser.cards.remove(resp)
    TCPCommunicator.sendMessage(resp)
    return args[1:]
