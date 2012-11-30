'''
Created on 30-11-2012

@author: Przemek
'''

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(adress, port):   
    server_address = (adress, port)
    sock.connect(server_address)

def disconnect():
    print 'closing socket'
    sock.close()

def sendMessage(message):
        print "sending message: %s" % message
        sock.sendall(message)

def getMessage():
    print 'reading\n'
    read = sock.makefile().readline()
    print read
