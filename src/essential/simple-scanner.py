import socket
import pyfiglet
import sys
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Simple Scanner")
print(ascii_banner)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Usage: simple-scanner.py $ip")
    exit()

print("Scanning Target: "+ target)
print("Scanning Started at: " + str(datetime.now()))

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))
        if result == 0:
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
