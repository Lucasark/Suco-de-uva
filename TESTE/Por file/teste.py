from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 12000))  
serverSocket.listen(1) 

while True:
    print ('Ready to serve...')    
    connectionSocket, addr = serverSocket.accept() 
    print ('Required connection', addr)

    try:
        message = connectionSocket.recv(1024) 
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send(b'Content-Type: image/jpeg')  
        connectionSocket.send(b'HTTP/1.0 200 OK\r\n\r\n')
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
            connectionSocket.close()
    except IOError:
        connectionSocket.send(b'404 Not Found')                       
        connectionSocket.close()                      
serverSocket.close() 