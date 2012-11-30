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
        TCPCommunicator.connect('192.168.3.103', 50008)
        TCPCommunicator.sendMessage('test')
        print TCPCommunicator.getMessage()
        TCPCommunicator.sendMessage('testmikel')
        print TCPCommunicator.getMessage()
        TCPCommunicator.disconnect()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()