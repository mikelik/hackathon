'''
Created on 30-11-2012

@author: Przemek
'''

def extractCommand(input):
    return input.split()[0]

def parseCommand(input):
    if 'GameStart' == extractCommand(input):
        print 'GameStart'

    if 'GameEnd' == extractCommand(input):
        print 'GameEnd'

    if 'RoundStart' == extractCommand(input):
        print ''
        
    if 'BattleStart' == extractCommand(input):
        print 'BattleStart'

    if 'BattleEnd' == extractCommand(input):
        print 'BattleEnd'    

    if 'RoundEnd' == extractCommand(input):
        print 'RoundEnd'

    if 'Players' == extractCommand(input):
        print 'Players'

    if 'Order' == extractCommand(input):
        print 'Order'

    if 'Hand' == extractCommand(input):
        print 'Hand'    

    if 'Player' == extractCommand(input):
        print 'Player'

    if 'CurrentZone' == extractCommand(input):
        print 'CurrentZone'

    if 'Player' == extractCommand(input):
        print 'Player'

    if 'Pass' == extractCommand(input):
        print 'Pass'    

    if 'Play' == extractCommand(input):
        print 'Play'

    if 'Protect' == extractCommand(input):
        print 'Protect'

    if 'Retrieve' == extractCommand(input):
        print 'Retrieve'

    if 'Score' == extractCommand(input):
        print 'Score'
