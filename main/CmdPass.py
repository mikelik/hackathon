'''
Created on 30 Nov 2012

@author: Czeslaw
'''

import Logger

def handle(args):
    Logger.log("Command Players: %s::" % args)
    #return args.split('\n')[-1]
    return args[1:]
