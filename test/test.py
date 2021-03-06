'''
Created on 30-11-2012

@author: mikel
'''
import unittest
from main import TCPCommunicator
from main import CommandParser

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


#    def testName(self):
#        TCPCommunicator.connect('localhost', 50008)
#        TCPCommunicator.sendMessage('Witojcie')
#        print TCPCommunicator.getMessage()
#        TCPCommunicator.sendMessage('testmikel')
#        print TCPCommunicator.getMessage()
#        TCPCommunicator.disconnect()

    #def testParser(self):
      #  CommandParser.parseCommand('Hand [1\n2\n3\n4\n5\n6\n7\n8\n9\n10\nCourtesan\nHeroine\nWinter\nSpring\nBishop\nDrummer\nScarecrow\nKey]')

    def testCondottiere(self):
        args = ['blue','clients=red','RoundStart 1','Hand ',['Courtesan','Key','5','4','2','Drummer','Bishop','5','3','4'],'BattleStart','1','Order',['blue','red'],'?Condottiere']
        CommandParser.parseCommand(args)

    def testRoundStart(self):
        inputArray = ['RoundStart 1', 'Hand [', 'Drummer', 'Drummer', 'Courtesan', 'Heroine', 'Spring', '4', '2', 'Heroine', 'Courtesan', 'Courtesan', ']', 'BattleStart 1', 'Order [', 'clients=red', ']', '?Condottiere']
        CommandParser.parseCommand(inputArray);
        assert(CommandParser.occupiedRegion[CommandParser.ix('Siena')] == 0)
        
    def testBattleEnd(self):
        CommandParser.occupiedRegion[CommandParser.ix('Siena')] = 0
        CommandParser.ourPlayer = 'red'
        CommandParser.parseCommand(['CurrentZone Siena','BattleEnd red'])
        
        assert(CommandParser.occupiedRegion[CommandParser.ix('Siena')] == 1)
        
    def testInitAi(self):
        CommandParser
        assert(len(CommandParser.regionNeighbours) == 17)
        CommandParser.parseCommand(['?Condottiere'])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()