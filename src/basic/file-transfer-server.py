import socket
import tqdm
import os

SERVER_HOST = "0.0.0.0"
SERVER_PORT = int(input("Server Port:"))

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

server = socket.socket()
server.bind((SERVER_HOST, SERVER_PORT))

server.listen(10)
print("Listening at {}:{}".format(SERVER_HOST, SERVER_PORT))

clientSocket, address = server.accept()
print("{} is connected".format(address))

receivedData = clientSocket.recv(BUFFER_SIZE).decode()
file, fileSize = receivedData.split(SEPARATOR)

filename = os.path.basename(file)
fileSize = int(fileSize)

progress = tqdm.tqdm(range(fileSize), f"Receiving {file}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "wb") as f:
    while True:
        bytesRead = clientSocket.recv(BUFFER_SIZE)
        if not bytesRead:
            break
        f.write(bytesRead)

        progress.update(len(bytesRead))
clientSocket.close()
server.close()
