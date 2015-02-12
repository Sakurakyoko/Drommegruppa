# -*- coding: utf8 -*-
from socket import *
serverPort = 12346
serverhostIP = 'localhost'
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print 'The server is ready to receive'
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode('utf-8').upper().encode('utf-8')
	serverSocket.sendto(modifiedMessage, clientAddress)
