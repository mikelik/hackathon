'''
Created on 30 Nov 2012

@author: Czeslaw
'''

from main import CommandParser

def handle(args):
    print "Command BattlStart: %s::" % args
    #return args.split('\n')[-1]
    return args[1:]
