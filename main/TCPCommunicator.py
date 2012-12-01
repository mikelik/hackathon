'''
Created on 30-11-2012

@author: Przemek
'''

import socket
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(adress, port):   
    server_address = (adress, port)
    sock.connect(server_address)

def disconnect():
    print 'closing socket'
    sock.close()

def sendMessage(message):
        print "sending message: %s" % message
        sock.sendall(message + '\r\n')

def getMessage():
    print 'reading\n'
    read = sock.recv(1024)
    if not read:
        print 'no data received'
    return repr(read)
    
def getMessageWait():
    print 'waiting\n'
    read = None
    for x in range(50):
        try:
            read = sock.recv(1024)
        except:
            print sys.exc_info()
         
        if not read:
            print 'no data received'
            time.sleep(1)
        else:
            return read

    
    