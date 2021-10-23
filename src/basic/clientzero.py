import socket

serverIP = "127.0.0.1"
serverPort = 8443

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(serverIP, serverPort)

clientMsg = input("Message to server:")
data = bytes(clientMsg, "utf-8")

print("Sending message to  {0}:{1}".format(serverIP,serverPort))
clientSocket.sendall(data)

serverData = str(clientSocket.recv(1024))
print("Message from server:", str(serverData))