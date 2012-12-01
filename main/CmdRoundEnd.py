'''
Created on 30 Nov 2012

@author: Czeslaw
'''

import Logger

def handle(args):
    Logger.log("Command %s::" % args[0])
    return args[1:]
