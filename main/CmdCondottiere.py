'''
Created on 30-11-2012

@author: mikel
'''
from main import TCPCommunicator
from CommandParser import *
import random

def handle(args):
    resp = regions(random.randint(0,len(regions)-1))
    print "Condottiere :%s:" % resp
    TCPCommunicator.sendMessage(resp)
    return args[1:]
