'''
Created on 30 Nov 2012

@author: Czeslaw
'''

from CommandParser import *

def handle(args):
    print "Command zone %s::" % args
    currentZone = args[0]
    return args[1:]
