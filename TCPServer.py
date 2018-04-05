from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
#serverSocket.listen(5)
print ("Ta pronto mane!")
while 1:
	connectionSocket,addr = serverSocket.accept()
	sentence = connectionSocket.recvfrom(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	print (sentence)
	connectionSocket.close()