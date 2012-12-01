'''
Created on 30 Nov 2012

@author: Czeslaw
'''


import CommandParser
import Logger

def handle(args):
    for index in range(1, len(args)-1):
        item = args[index]
        if (item == '}'):
            return args[index+1:]
        CommandParser.scoreMap[item.split('=')[0]] = item.split('=')[1]
        Logger.log("Command Score appended :%s:\n" % item)
    return ''
