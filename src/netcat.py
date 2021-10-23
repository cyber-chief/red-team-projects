import sys
import socket
import time
import subprocess

if len(sys.argv) != 3:
    print("Usage: netcat.py $hostname $port")
    exit()

hostname = sys.argv[1]
port = int(sys.argv[2])

def netcat_server(hostname, port):
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((hostname, port))
    serv.listen(10)

    client, address = serv.accept()
    client.send("#".encode())

    command = ""
    while True:
        data = s.recv(1024)
        if not data:
            break
        command += data.decode()
    output = subprocess.check_output(command, shell=True)
    client.send(output.encode())

def netcat_client(hostname, port, commands):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(commands)
    time.sleep(0.5)
    s.shutdown(socket.SHUT_WR)

    result = ""
    while True:
        data = s.recv(1024)
        if not data:
            break
        result += data.decode()
    print(result)

    if result == "exit":
        s.close()
        exit()

while True:
    commands = input("command:")
    netcat_client(hostname, port, commands)

