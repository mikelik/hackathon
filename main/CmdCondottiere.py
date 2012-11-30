'''
Created on 30-11-2012

@author: mikel
'''
from main import TCPCommunicator
import CommandParser
import random

def handle(args):
    resp = CommandParser.regions[random.randint(0,len(CommandParser.regions)-1)]
    print "Condottiere :%s:" % resp
    TCPCommunicator.sendMessage(resp)
    return args[1:]
