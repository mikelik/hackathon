'''
Created on 30-11-2012

@author: mikel
'''
import unittest
from main import TCPCommunicator, CommandParser


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

    def testParser(self):
        CommandParser.parseCommand('Hand [1\n2\n3\n4\n5\n6\n7\n8\n9\n10\nCourtesan\nHeroine\nWinter\nSpring\nBishop\nDrummer\nScarecrow\nKey]')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()