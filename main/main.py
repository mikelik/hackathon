'''
Created on 30-11-2012

@author: mikel
'''
import TCPCommunicator
import CommandParser
import Logger
       

if __name__ == '__main__':
    configFile = open('../startup-info', 'r')
    configText = configFile.read()
    
    configParsed = configText.split()
    server = configParsed[0].split(':')[0]
    ip = configParsed[0].split(':')[1]
    password = configParsed[1]
    
    Logger.log('version with logger: 8')
    Logger.log('password: %s' % password)

    TCPCommunicator.connect(server, int(ip))
    TCPCommunicator.sendMessage('AUTH ' + password)
    while True:
        args_string = TCPCommunicator.getMessageWait()
        Logger.log("RAW:\n%s:==========\n" % args_string)
        args_list = args_string.splitlines()
        CommandParser.parseCommand(args_list)
    #while True:
    #    if x[0] == '?':
    #        TCPCommunicator.sendMessage('Milano')

    TCPCommunicator.disconnect()
