# -*- coding: utf-8 -*-
from socket import *
unitest = raw_input("Input for binary representation:")
serverName = "localhost"
serverPort = 12009
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input("Input lowercase sentence:")
clientSocket.sendto(message, (serverName, serverPort))
clientSocket.sendto(unitest, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
modifiedUni, serverAdress = clientSocket.recvfrom(2048)
print "Binary representation of " + unitest + " = " + modifiedUni
print "Lower case " + message + " = " + modifiedMessage
clientSocket.close()
