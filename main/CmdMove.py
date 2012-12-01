'''
Created on 30-11-2012

@author: Przemek
'''

import CommandParser
import TCPCommunicator
import random
import Logger

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
    elif 'Key' in CommandParser.cards:
        maxi = 0
        maxUser = ''
        maxiSecond = 0
        CommandParser.shouldThrowKeyCard = False
                
        for user in CommandParser.scoreMap.iterkeys():
            if (maxi <= CommandParser.scoreMap[user]):
                maxiSecond = maxi
                maxUser = user
                maxi = CommandParser.scoreMap[user]
                
        if maxUser == CommandParser.ourPlayer and maxiSecond < maxi:
            Logger.log('throw key, maxi=' + str(maxi) + ' maxiSecond=' + str(maxiSecond) + ' maxUser=' + maxUser)
            indexKey =  CommandParser.cards.index('Key')
            resp = CommandParser.cards[indexKey]
            CommandParser.cards.remove(resp)
        else:
            ran = random.randint(0,len(CommandParser.cards)-1)
            resp = CommandParser.cards[ran]
            CommandParser.cards.remove(resp)
    else:
        ran = random.randint(0,len(CommandParser.cards)-1)
        resp = CommandParser.cards[ran]
        CommandParser.cards.remove(resp)
    TCPCommunicator.sendMessage(resp)
    return args[1:]
