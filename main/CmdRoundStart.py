'''
Created on 30 Nov 2012

@author: Czeslaw
'''
import Logger

import  CommandParser

def handle(args):
    print "Command %s::" % args[0]
    CommandParser.cards = []
    return args[1:]
