import socket
import threading
import sys

#check for correct usage
if len(sys.argv) != 4:
    print("Usage: one.py $ip $port $shift")
    exit()

host = str(sys.argv[1])
port = int(sys.argv[2])
shift = int(sys.argv[3])


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

def encrypt(message, shift):
    encMessage = ""

    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            encMessage += chr((ord(char) + shift-65) % 26 + 65)
        else:
            encMessage += chr((ord(char) + shift - 97) % 26 + 97)

    return encMessage

def decrypt(message, shift):
    decMessage = ""

    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            decMessage += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decMessage += chr((ord(char) - shift - 97) % 26 + 97)
        
    return decMessage

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(2048)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            username = nicknames[index]
            broadcast("{}:{}: {}".format("Server", encrypt("{username} left!", shift), shift).encode("utf-8"))
            nicknames.remove(username)
            break

def receive():
    while True:
        client, address = server.accept()
        print("{} connected to server".format(address))

        client.send("NICK".encode("utf-8"))
        username = client.recv(2048).decode("utf-8")
        nicknames.append(username)
        clients.append(client)

        print("New User: {}".format(username))
        broadcast("New User: {}: {}".format(encrypt(username, shift), shift).encode("utf-8"))
        client.send("Server: {}: {}".format(encrypt("Connected to server.", shift), shift).encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server online...")
receive()