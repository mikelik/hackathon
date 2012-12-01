'''
Created on 30-11-2012

@author: Przemek
'''

import socket
import sys
import time
import Logger

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(adress, port):   
    server_address = (adress, port)
    sock.connect(server_address)

def disconnect():
    Logger.log('closing socket')
    sock.close()

def sendMessage(message):
        message = str(message)
        Logger.log("sending message: %s" % message)
        sock.sendall(message + '\r\n')

def getMessage():
    Logger.log('reading\n')
    read = sock.recv(1024)
    if not read:
        Logger.log('no data received')
    return repr(read)
    
def getMessageWait():
    Logger.log('waiting\n')
    read = None
    for x in range(40):
        try:
            read = sock.recv(1024)
        except:
            read = ''
            print sys.exc_info()
         
        if not read:
            Logger.log('no data received')
            time.sleep(0.5)
        else:
            return read


