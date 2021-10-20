import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

host = input("Server IP:")
port = int(input("Server Port:"))
file = input("File(Inlcude path):")

fileSize = os.path.getsize(file)

client = socket.socket()
client.connect((host, port))
print("Connected to {}:{}".format(host,port))


client.send(f"{file}{SEPARATOR}{fileSize}".encode())
progress = tqdm.tqdm(range(fileSize), f"Sending {file}", unit="B", unit_scale=True, unit_divisor=1024)
with open(file, "rb") as f:
    while True:
        bytesRead = f.read(BUFFER_SIZE)
        if not bytesRead:
            break
        client.sendall(bytesRead)
        progress.update(len(bytesRead))
client.close()
