import socket
import threading
import sys

#check for correct usage
if len(sys.argv != 3):
    print("Usage: clientone.py $ip $port")
    exit()

username = input("Enter your username")
host = str(sys.argv[1])
port = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(host,port)

def recieve():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "NICK":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("Error occurred. Closing connection...")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(username,input(''))
        client.send(message.encode("utf-8"))
    

recieveThread = threading.Thread(target=recieve)
recieveThread.start()

writeThread = threading.Thread(target=write)
writeThread.start()
