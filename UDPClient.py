from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
a = 1
while a:
	message = input('Chega mais ai, patrao:').encode()
	clientSocket.sendto(message, (serverName, serverPort))
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print(modifiedMessage)
	b = input('Denovo, irmao?')
	if (b == 'Y' or b == 'y'):
		a = 1
	else:
		a = 0
clientSocket.close()