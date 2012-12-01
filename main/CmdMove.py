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
        Logger.log("Our score = %s" % CommandParser.scoreMap[CommandParser.ourPlayer])
    Logger.log('Move: ')
    Logger.log(CommandParser.cards)
    resp = None
    if len(CommandParser.cards) <= 0:
        resp = 'pass'
    elif 'Key' in CommandParser.cards:
        CommandParser.maxi = 0
        CommandParser.maxUser = ''
        CommandParser.maxiSecond = 0
                
        for user in CommandParser.scoreMap.iterkeys():
            if (CommandParser.maxi <= CommandParser.scoreMap[user]):
                CommandParser.maxiSecond = CommandParser.maxi
                CommandParser.maxUser = user
                CommandParser.maxi = CommandParser.scoreMap[user]
                
        if CommandParser.maxUser == CommandParser.ourPlayer and int(CommandParser.maxiSecond) < int(CommandParser.maxi):
            Logger.log('throw key, maxi=' + str(CommandParser.maxi) + ' maxiSecond=' + str(CommandParser.maxiSecond) + ' maxUser=' + CommandParser.maxUser)
            indexKey =  CommandParser.cards.index('Key')
            resp = CommandParser.cards[indexKey]
            CommandParser.cards.remove(resp)
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
            for x in range(len(CommandParser.cards)-1) :
                if CommandParser.cards[x] == 'Heroine':
                    resp = 'Heroine'
                if CommandParser.cards[x] == 'Drummer':
                    resp = 'Drummer'
            CommandParser.cards.remove(resp)
    elif CommandParser.maxTheirsCard > CommandParser.maxOurCard and CommandParser.maxTheirsCard > 5 and 'Bishop' in CommandParser.cards:
        resp = 'Bishop'
        CommandParser.cards.remove(resp)
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
#        for x in range(len(CommandParser.cards)-1) :
#                if CommandParser.cards[x] == 'Heroine':
#                    resp = 'Heroine'
#                if CommandParser.cards[x] == 'Drummer':
#                    resp = 'Drummer'
        CommandParser.cards.remove(resp)
    TCPCommunicator.sendMessage(resp)
    return args[1:]
