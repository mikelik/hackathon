'''
Created on 30-11-2012

@author: mikel
'''
import TCPCommunicator

if __name__ == '__main__':
    
        configFile = open('../startup-info', 'r')
        configText = configFile.read()
        
        configParsed = configText.split()
        server = configParsed[0].split(':')[0]
        ip = configParsed[0].split(':')[1]
        password = configParsed[1]
        
        TCPCommunicator.connect(server, int(ip))
        TCPCommunicator.sendMessage('AUTH ' + password)
        x = TCPCommunicator.getMessageWait()
    
    
        while True:
            if x[0] == '?':
                TCPCommunicator.sendMessage('Milano')
                          
        
            
    
        print TCPCommunicator.getMessageWait()
        print TCPCommunicator.getMessageWait()
        print TCPCommunicator.getMessageWait()
        TCPCommunicator.disconnect()