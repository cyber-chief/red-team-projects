import socket

serverAddress = ("127.0.0.1",8443)

#create socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind socket to port
serverSocket.bind(serverAddress)
print("Server up and listening")

#listen for messages
serverSocket.listen(10)
msg, address = serverSocket.accept()

while 1:
    dataFromClient = msg.recv(10245)
    msg.sendall(dataFromClient)