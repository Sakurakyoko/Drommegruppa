# -*- coding: utf-8 -*-
from socket import *
def unicodeBin(character):
    return '{0:08b}'.format(ord(character.decode('utf8')))
serverPort = 12009
# serverHostIp = "localhost"
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print "The server is ready to receive"
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    unitest, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode("utf-8").upper().encode("utf-8")
    modifiedUni = unicodeBin(unitest)
    serverSocket.sendto(modifiedMessage, clientAddress)
    serverSocket.sendto(modifiedUni, clientAddress)
