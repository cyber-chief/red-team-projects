import socket
import threading
import sys

#check for correct usage
if len(sys.argv)!= 3:
    print("Usage: one.py $ip $port")
    exit()

host = str(sys.argv[1])
port = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            username = nicknames[index]
            broadcast("{} left!".format(username).encode("utf-8"))
            nicknames.remove(username)
            break

def receive():
    while True:
        client, address = server.accept()
        print("{} connected to server".format(address))

        client.send('NICK'.encode("utf-8"))
        username = client.recv(1024).decode("utf-8")
        nicknames.append(username)
        clients.append(client)

        print("New User: {}".format(username))
        broadcast("New User: {}".format(username).encode("utf-8"))
        client.send("Connected to server.".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server online...")
receive()