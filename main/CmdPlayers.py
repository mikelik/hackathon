'''
Created on 30 Nov 2012

@author: Czeslaw
'''

from CommandParser import *
players = []

def handle(args):
    #print "Command Players: %s::" % args
    args_list = args.splitlines()
    for item in args_list:
        print "Command Players item: %s::" % item
        if (item == '['):
            continue
        if (item == ']'):
            ret_data = args.join('\n')
            print "Command Players returning: %s::" % ret_data
            return ret_data
        players.append(item)

