'''
Created on 30 Nov 2012

@author: Czeslaw
'''
import  CommandParser
import Logger


def handle(args):
    Logger.log("Command %s::" % args[0])
    CommandParser.cards = []
    return args[1:]
