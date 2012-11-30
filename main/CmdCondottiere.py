'''
Created on 30-11-2012

@author: mikel
'''
from main import TCPCommunicator
from CommandParser import *
import random

def handle(args):
    TCPCommunicator.sendMessage(regions(random.randint(0,len(regions)-1)))
    return args.split('\n')[1:]