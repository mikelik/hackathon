'''
Created on 30 Nov 2012

@author: Czeslaw
'''


import CommandParser
import Logger

def handle(args):
    
    maxi = 0
    maxUser = ''
    maxiSecond = 0
    CommandParser.shouldThrowKeyCard = False
    
    for index in range(1, len(args)-1):
        item = args[index]
        if (item == '}'):
            return args[index+1:]
        curScore = item.split('=')[1]
        CommandParser.scoreMap[item.split('=')[0]] =curScore
        if (maxi <= curScore):
            maxiSecond = maxi
            maxUser = item.split('=')[0]
            maxi = curScore
        
        Logger.log("Command Score appended :%s:\n" % item)
    if maxUser == CommandParser.ourPlayer and maxiSecond < maxi:
        CommandParser.shouldThrowKeyCard = True
        Logger.log('Setting shouldThrowKeyCard to true, maxi=' + str(maxi) + ' maxiSecond=' + str(maxiSecond) + ' maxUser=' + maxUser)
    return ''
