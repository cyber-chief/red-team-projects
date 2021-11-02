import socket
import pyfiglet
import sys
from datetime import datetime
import subprocess
import re

def findProto(socket):
    socket.send("agteadfede")
    data = socket.recv(4096)
    if data.contains("400 Bad Request"):
        return "http"
    elif data.contains("FORMERR"):
        return "DNS"
    elif data.contains("Syntax error"):
        return "ftp"
    else:
        return "unknown"

ascii_banner = pyfiglet.figlet_format("Simple OS Scanner")
print(ascii_banner)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Usage: simple-scanner.py $ip")
    exit()

print("Scanning Target: "+ target)
print("Scanning Started at: " + str(datetime.now()))

print("Scanning for OS...")

result = subprocess.check_output("ping -c 4 " + target, shell=True)
if result:
    pattern = re.compile("ttl=\d*")
    ttl = pattern.search(str(result)).group()
    hopsLeft = int(ttl.split("=")[1])
    if hopsLeft <= 64:
        print("Linux Server Detected")
    elif hopsLeft <= 128:
        print("windows Server Detected")
    else:
        print("Unknown OS Detected")
else:
    print("Server error")
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))
        if result == 0:
            protocol = findProto(s)
            print("{}/tcp : open".format(port))
        s.close()
except KeyboardInterrupt:
    sys.exit()
except socket.gaierror:
    print("/n Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("Server not responding")
    sys.exit()



    
