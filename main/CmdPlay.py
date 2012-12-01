'''
Created on 30 Nov 2012

@author: Czeslaw
'''

import CommandParser
import Logger

def handle(args):
    card = args[0].split()[1];
    Logger.log("Command %s::" % args[0])
    Logger.log("Player %s played %s" % (CommandParser.currentPlayer, card))
    
    mercenaryCards = 0
    if CommandParser.currentPlayer in CommandParser.mercenaryCards.keys() :
        mercenaryCards = CommandParser.mercenaryCards[CommandParser.currentPlayer]
    if card.isdigit() :
        mercenaryCards += 1
    CommandParser.mercenaryCards[CommandParser.currentPlayer] = mercenaryCards
    Logger.log("mercenaryPoints %s : %s" %(CommandParser.currentPlayer, mercenaryCards))
    
    if CommandParser.currentPlayer == CommandParser.ourPlayer and card.isdigit():
        if CommandParser.maxOurCard < int(card):
            CommandParser.maxOurCard = int(card)
    elif card.isdigit():
        if CommandParser.maxTheirsCard < int(card):
            CommandParser.maxTheirsCard = int(card)
            
    if card == 'Winter':
        CommandParser.isWinter = True
    if card == 'Spring':
        CommandParser.isWinter = False

    return args[1:]
