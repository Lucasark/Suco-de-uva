from socket import *
serverName = 'localhost'
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ("Ta pronto mane!")
while 1:
	connectionSocket, addr = serverSocket.accept()
	connectionSocket.recv(1024)
	connectionSocket.send('HTTP/1.0 200 0K\n')
	connectionSocket.send('\n')
	connectionSocket.send("""
		<html>
		<body>
		<h1>Hello World</h1>
		</body>
		</html>

	"""	)
	connectionSocket.close()