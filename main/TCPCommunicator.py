'''
Created on 30-11-2012

@author: Przemek
'''

import socket

def sendMessage(message):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 10000)
        sock.connect(server_address)
        print "sending message: %s" % message
        sock.sendall(message)
    finally:
        print 'closing socket'
        sock.close()

sendMessage('test')
