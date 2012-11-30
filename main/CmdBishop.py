'''
Created on 30-11-2012

@author: mikel
'''
from main import TCPCommunicator
import CommandParser
import random

def handle(args):
    resp = 'pass'
    print "Bishop :%s:" % resp
    TCPCommunicator.sendMessage(resp)
    return args[1:]
