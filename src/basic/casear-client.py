import socket
import threading
import sys

#check for correct usage
if len(sys.argv) != 4:
    print("Usage: clientone.py $ip $port $initialShift")
    exit()

username = str(input("Enter your username:"))
host = str(sys.argv[1])
port = int(sys.argv[2])
shift = int(sys.argv[3])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))

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


def recieve():
    while True:
        try:
            message = client.recv(2048).decode("utf-8")

            if message == "NICK":
               
                client.send(username.encode("utf-8"))
            else:
                username, message, shift = message.split(":")
                decMessage = decrypt(message, shift)
                print(decMessage)
        except:
            print("Error occurred. Closing connection...")
            client.close()
            break

def write():
    while True:
        decMessage = input('Message:')
        message = "{}: {}:{}".format(username,encrypt(decMessage,shift), shift)
        client.send(message.encode("utf-8"))
    

recieveThread = threading.Thread(target=recieve)
recieveThread.start()

writeThread = threading.Thread(target=write)
writeThread.start()
