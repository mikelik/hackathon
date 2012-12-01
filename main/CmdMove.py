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
    ptsHands = CommandParser.potentialPointsInHand() 
    Logger.log('Potential points in hand: ' + str(ptsHands))
    maxPossiblePts = ptsHands + int(CommandParser.scoreMap[CommandParser.ourPlayer])
    Logger.log('Potentially maximum points to gain in round: ' + str(maxPossiblePts))
    keyMax = max(CommandParser.scoreMap, key=CommandParser.scoreMap.get)
        
    valueMax = CommandParser.scoreMap[keyMax]
    
    if keyMax != CommandParser.ourPlayer and int(valueMax) > int(maxPossiblePts):
        CommandParser.weAreLosing = True
        Logger.log("weAreLosing = True - raczej nie wygramy tej rundy, top value in round: " + str(valueMax))
        


    resp = None
    if len(CommandParser.cards) <= 0:
        resp = 'pass'
    elif CommandParser.weAreLosing:
        resp = 'pass'
        # if 'Scarecrow' in CommandParser:
        Logger.log("weAreLosing - tryin to get back my cards")
        #resp = 'Scarecrow'
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
            for x in range(len(sortedcards)) :
                if sortedcards[x].isdigit() :
                    digits.append(sortedcards[x])
            digits.sort(key=int)
            ran = random.randint(0,len(CommandParser.cards)-1)
            resp = CommandParser.cards[ran]
            if len(digits) > 0 :
                resp = digits[len(digits)-1]
                digits.remove(resp)
            for x in range(len(CommandParser.cards)) :
                if CommandParser.cards[x] == 'Heroine':
                    resp = 'Heroine'
                if CommandParser.cards[x] == 'Drummer':
                    resp = 'Drummer'
                if CommandParser.cards[x] == 'Winter':
                    resp = 'Winter'
            CommandParser.cards.remove(resp)
    elif CommandParser.maxTheirsCard > CommandParser.maxOurCard and CommandParser.maxTheirsCard > 5 and 'Bishop' in CommandParser.cards:
        resp = 'Bishop'
        CommandParser.cards.remove(resp)
    else:
        sortedcards = deepcopy(CommandParser.cards)
        digits = []
        for x in range(len(sortedcards)) :
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
