'''
Created on 30 Nov 2012

@author: Czeslaw
'''

import CommandParser

def handle(args):
    print "Command zone %s::" % args
    CommandParser.currentZone = args[0].split()[1]
    return args[1:]
