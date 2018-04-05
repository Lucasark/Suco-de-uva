from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
a = 1
while a:
	clientSocket.connect((serverName,serverPort))
	setence = input('Chega mais ai, patrao:').encode()
	clientSocket.sendto(sentence)
	modifiedMessage = clientSocket.recvfrom(1024)
	print('Saindo de Jesus:'+modifiedMessage)
	b = input('Denovo, irmao?')
	if (b == 'Y' or b == 'y'):
		a = 1
	else:
		a = 0
clientSocket.close()