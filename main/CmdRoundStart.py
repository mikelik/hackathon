'''
Created on 30 Nov 2012

@author: Czeslaw
'''
import Logger

def handle(args):
    Logger.log("Command RoundStart: %s::" % args)
    return args[1:]
