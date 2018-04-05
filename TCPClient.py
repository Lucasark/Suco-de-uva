from socket import *
a = 1
while a:
	serverName = 'localhost'
	serverPort = 12000
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))
	sentence = input('Chega mais ai, patrao:').encode()
	clientSocket.send(sentence)
	modifiedMessage = clientSocket.recv(1024)
	print('Saindo de Jesus:', modifiedMessage)
	clientSocket.close()
	b = input('Denovo, irmao?')
	if (b == 'Y' or b == 'y'):
		a = 1
	else:
		a = 0