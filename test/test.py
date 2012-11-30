'''
Created on 30-11-2012

@author: mikel
'''
import unittest
from main import TCPCommunicator


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        TCPCommunicator.connect('localhost', 9999)
        TCPCommunicator.sendMessage('test')
        TCPCommunicator.sendMessage('testmikel')
        TCPCommunicator.getMessage()
        TCPCommunicator.disconnect()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()