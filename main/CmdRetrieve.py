'''
Created on 30-11-2012

@author: mikel
'''
from main import TCPCommunicator
import CommandParser
import random
import Logger


def handle(args):
    #if CommandParser.weAreLosing: TODO: 
    #    resp = int(getMaxMercenaryCard())
    #else:
    resp = 'pass'
    Logger.log("Retrieve :%s:" % resp)
    TCPCommunicator.sendMessage(resp)
    return args[1:]
